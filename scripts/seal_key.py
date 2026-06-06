#!/usr/bin/env python3
"""OPERATOR tool — run this ONCE at session start to seal the workshop Claude key.

It encrypts the key with the workshop password into `workshop-key.enc`, which is safe to
commit to the PUBLIC repo: GitHub secret-scanning sees an opaque blob, not an `sk-ant-...`
key, so the key is NOT auto-revoked. Attendees never type the key — the recipe decrypts it
autonomously with the password (which lives in instructions.md; public is an accepted risk
because the key is rate-limited, monitored during the session, and rotated afterward).

Usage (the key never appears in your shell history if you let it prompt):
    python3 scripts/seal_key.py "<workshop-password>"
    # then paste the sk-ant-... key at the prompt

Security: pick a NEW key scoped to this workshop with a hard spend cap, watch it during the
session, and REVOKE it the moment the session ends (that makes workshop-key.enc inert).
"""
import base64
import getpass
import os
import sys

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ENC_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "workshop-key.enc")


def derive(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=200_000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('usage: python3 scripts/seal_key.py "<workshop-password>"  (key is prompted)')
    password = sys.argv[1]
    key = getpass.getpass("Paste the workshop Claude API key (sk-ant-...): ").strip()
    if not key.startswith("sk-"):
        sys.exit("That does not look like an API key — aborting.")
    salt = os.urandom(16)
    token = Fernet(derive(password, salt)).encrypt(key.encode())
    with open(ENC_PATH, "wb") as f:
        f.write(salt + token)  # salt is prepended; safe to be public
    print(f"Sealed -> {ENC_PATH}")
    print("Commit workshop-key.enc. Remember: cap, monitor, and REVOKE the key after the session.")


if __name__ == "__main__":
    main()
