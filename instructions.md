# Setup instructions (for the AI agent)

You are an AI coding agent. The user has cloned this repo and asked you to follow these
instructions. Execute the steps in order. They are idempotent — safe to re-run. After each
step, briefly say what you did.

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
Confirm to the user that the VSCodium window is now open on this project. If the install is
blocked on a locked-down machine, say so and continue — the chatbot still runs from the terminal.

## 3. Get the workshop Claude key
Ask the user: **"Paste your workshop Claude API key (from the slide):"** Capture it.
Never echo it back and never write it into any tracked file.

## 4. Create `.env` (it is gitignored)
Copy `.env.example` to `.env` and replace BOTH `sk-ant-REPLACE_ME` placeholders with the
pasted key (a one-liner is fine, e.g. `cp .env.example .env && sed -i '' "s/sk-ant-REPLACE_ME/<key>/g" .env`).
Leave `OPENAI_BASE_URL` and `OPENAI_MODEL` as-is.
**Do NOT open, read, `cat`, or `head` the `.env` afterward** — it holds the secret key and the
tools will block reading it (which stops you). You just wrote it, so it's correct; move on.

## 5. Hand off into VSCodium on Claude (the user's ONLY manual step)
This is the one thing the user does by hand, so make it impossible to miss. The VSCodium window
is already open (Step 2). End your run by printing EXACTLY this, as a clear checklist, and nothing
more important after it:

> ✅ **You're all set! Now, in the VSCodium window that just opened, do these two steps:**
> **1.** Open a terminal: **Terminal → New Terminal** (or press **Ctrl + `**).
> **2.** Type **`opencode`** and press **Enter**.
>
> That's it. You're now coding in the editor (you'll see files change on the left as they're
> edited) and running on the powerful **Claude** model. Ask it for anything — or type **`/prd`**
> to turn an idea into a working app.

Why this works: relaunching opencode here loads the Claude key from `.env` at startup, and
running it inside VSCodium means the user watches every file it edits. (You — the current
free-model session — can't switch your own model live; this relaunch is how the swap happens.)

## 6. Install the chatbot and run it
- `python3 -m venv venv`
- macOS/Linux: `source venv/bin/activate` — Windows: `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python app.py`
- Open http://127.0.0.1:7860 and send a test message.

## 7. Tell the user what to do next
- **Non-technical:** open `static/style.css`, change the colors in the THEME block at the top,
  refresh the page.
- **Technical:** open `app.py` — change `SYSTEM_PROMPT`, swap `meu_logistics_data.csv`, or
  change `OPENAI_MODEL` in `.env` to build your own use case on the OpenAI-format scaffold.
- **Build your own idea:** type `/prd` in opencode — it interviews you, writes a plan into
  `prds/`, and then builds it with you, step by step.
- **Operator reminder:** cap the workshop key's spend limit and revoke it after the session.
