# Setup instructions (for the AI agent)

You are an AI coding agent. The user has cloned this repo and asked you to follow these
instructions. Execute the steps in order. They are idempotent — safe to re-run. After each step,
briefly say what you did. **Do not stop early — you MUST finish with Step 7 (the handoff).**

## 1. Detect the OS
Determine whether this is macOS, Windows, or Linux and use the matching commands below.

## 2. Install AND open VSCodium (the editor), with this project loaded
Install VSCodium if it's missing, then actually OPEN it on this folder so the window is up in
front of the user — they should never have to hunt for or launch it themselves. (VSCodium looks
and works exactly like VS Code.)
- macOS: `brew install --cask vscodium` (install Homebrew first if missing). Then open it with
  `codium .`; if the `codium` command isn't found, run `open -a VSCodium "$PWD"`.
- Windows: `winget install -e --id VSCodium.VSCodium` (or `choco install vscodium`). Then open it
  with `codium .`; if `codium` isn't found, launch VSCodium and open this folder.
- Linux: `snap install codium --classic` (or the official VSCodium repo). Open with `codium .`.
Confirm the VSCodium window is now open on this project. If install is blocked on a locked-down
machine, say so and continue — the chatbot still runs from the terminal.

## 3. Install the project dependencies
Create the virtual environment and install everything (this also installs the tool used to unlock
the workshop key in Step 4):
- `python3 -m venv venv`
- macOS/Linux: `source venv/bin/activate` — Windows: `venv\Scripts\activate`
- `pip install -r requirements.txt`

## 4. Unlock the workshop AI key (nothing to type — it's sealed in this repo)
The workshop Claude key is sealed in `workshop-key.enc` (encrypted — safe to be public). Unlock it
with the workshop password; this provisions the key into BOTH places that need it, automatically:
the chatbot's `.env` AND opencode's own credential store (so opencode comes up on Claude).

```
python scripts/unlock_key.py "WORKSHOP_PASSWORD_HERE"
```

> **Operator:** replace `WORKSHOP_PASSWORD_HERE` with the same password you used in
> `scripts/seal_key.py`. It is fine for this to be public — the key is rate-limited and monitored
> during the session and rotated immediately afterward.

The script writes the key only into `.env` (gitignored) and `~/.local/share/opencode/auth.json`.
**Do NOT `cat`/open `.env` or the auth file** — they hold the secret; you just wrote them, so move
on. If unlock fails, report the error verbatim and stop (do NOT ask the user to paste a key).

## 5. Start the chatbot (in the BACKGROUND — do not block)
With the venv still active:
- Start it in the background so it keeps running and does NOT block you:
  - macOS/Linux: `nohup python app.py > /tmp/chatbot.log 2>&1 &`
  - Windows: `start "" python app.py`
- Wait ~2 seconds, then confirm it's up: `curl http://127.0.0.1:7860` (expect a response).
- **Never run `python app.py` in the foreground** — it would block you from finishing.

## 6. Tell the user what they can do
- **Use it:** open **http://127.0.0.1:7860** in a browser and chat with it.
- **Change how it looks (no coding):** edit the THEME color block at the top of `static/style.css`.
- **Change what it does:** edit `SYSTEM_PROMPT` or swap `meu_logistics_data.csv` in `app.py`.
- **Build your own idea:** type `/prd` in opencode — it interviews you, writes a plan into
  `prds/`, then builds it with you, step by step.

## 7. FINAL STEP — hand off into VSCodium on Claude (ALWAYS end here)
This is the user's ONE manual step, and it's how they move onto the powerful Claude model. ALWAYS
finish your run by printing EXACTLY this, as the very last thing you say:

> ✅ **You're all set! The chatbot is running at http://127.0.0.1:7860.**
>
> **To switch onto the powerful Claude model and keep building, do this in the VSCodium window
> that's already open:**
> **1.** Open a terminal: **Terminal → New Terminal** (or press **Ctrl + `**).
> **2.** Type **`opencode`** and press **Enter**.
>
> You're now in the editor (you'll see files change on the left) and on Claude. Ask it for
> anything — or type **`/prd`** to turn an idea into a working app.

Why this works: Step 4 wrote the Claude key into opencode's own credential store
(`~/.local/share/opencode/auth.json`), so launching opencode in this folder comes up on Claude
with no key to enter — opencode does NOT read `.env`, which is why the key goes into its
credential store (for opencode) and into `.env` separately (for the chatbot). Running it inside
VSCodium lets the user watch every file it edits.
