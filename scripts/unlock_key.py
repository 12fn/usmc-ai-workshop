#!/usr/bin/env python3
"""RECIPE tool — the coding agent runs this to unlock the workshop key autonomously.

It decrypts `workshop-key.enc` with the workshop password, then provisions the key into the
TWO places that need it, so the attendee types nothing:
  1. `.env`  — the Flask chatbot reads it (python-dotenv).
  2. `~/.local/share/opencode/auth.json` — opencode's OWN credential store, so opencode runs
     on Claude with no `.env` dependency (opencode does NOT auto-load .env).

The key is written ONLY to those gitignored / home-dir targets and is never printed.

Usage:  python3 scripts/unlock_key.py "<workshop-password>"
"""
import base64
import json
import os
import sys
from pathlib import Path

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ROOT = Path(__file__).resolve().parent.parent
ENC_PATH = ROOT / "workshop-key.enc"


def derive(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=200_000)
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def write_env(key: str) -> None:
    """Render .env from .env.example, substituting the real key for the placeholders."""
    example = (ROOT / ".env.example").read_text()
    env = example.replace("sk-ant-REPLACE_ME", key)
    # strip the operator comment lines so .env is clean
    env = "\n".join(line for line in env.splitlines() if not line.startswith("#")).strip() + "\n"
    (ROOT / ".env").write_text(env)


def write_opencode_auth(key: str) -> None:
    """Write the key into opencode's credential store so it runs on Claude autonomously."""
    auth = Path.home() / ".local" / "share" / "opencode" / "auth.json"
    auth.parent.mkdir(parents=True, exist_ok=True)
    data = {}
    if auth.exists():
        try:
            data = json.loads(auth.read_text())
        except Exception:
            data = {}
    data["anthropic"] = {"type": "api", "key": key}
    auth.write_text(json.dumps(data, indent=2))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit('usage: python3 scripts/unlock_key.py "<workshop-password>"')
    if not ENC_PATH.exists():
        sys.exit("workshop-key.enc is missing — the operator must seal the key first (scripts/seal_key.py).")
    password = sys.argv[1]
    blob = ENC_PATH.read_bytes()
    salt, token = blob[:16], blob[16:]
    try:
        key = Fernet(derive(password, salt)).decrypt(token).decode()
    except Exception:
        sys.exit("Could not decrypt — wrong workshop password (check instructions.md).")
    write_env(key)
    write_opencode_auth(key)
    print("Provisioned the workshop model: .env (chatbot) + opencode auth (Claude). No key was printed.")


if __name__ == "__main__":
    main()
