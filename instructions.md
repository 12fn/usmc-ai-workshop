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

## 3. Get the workshop Claude key
Ask the user: **"Paste your workshop Claude API key (from the slide):"** Capture it.
Never echo it back and never write it into any tracked file.

## 4. Create `.env` (it is gitignored)
Copy `.env.example` to `.env` and replace BOTH `sk-ant-REPLACE_ME` placeholders with the pasted
key (a one-liner is fine, e.g. `cp .env.example .env && sed -i '' "s/sk-ant-REPLACE_ME/<key>/g" .env`).
Leave `OPENAI_BASE_URL` and `OPENAI_MODEL` as-is.
**Do NOT open, read, `cat`, or `head` the `.env` afterward** — it holds the secret key and the
tools will block reading it (which stops you). You just wrote it, so it's correct; move on.

## 5. Install the chatbot and start it (in the BACKGROUND — do not block)
- `python3 -m venv venv`
- macOS/Linux: `source venv/bin/activate` — Windows: `venv\Scripts\activate`
- `pip install -r requirements.txt`
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
- **Operator reminder:** cap the workshop key's spend limit and revoke it after the session.

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

Why this works: relaunching opencode in this folder loads the Claude key from `.env` at startup
(you — the current free-model session — cannot switch your own model live), and running it inside
VSCodium lets the user watch every file it edits.
