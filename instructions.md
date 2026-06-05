# Setup instructions (for the AI agent)

You are an AI coding agent. The user has cloned this repo and asked you to follow these
instructions. Execute the steps in order. They are idempotent — safe to re-run. After each
step, briefly say what you did.

## 1. Detect the OS
Determine whether this is macOS, Windows, or Linux and use the matching commands below.

## 2. Install VSCodium (open-source IDE), if not already installed
- macOS: `brew install --cask vscodium`  (install Homebrew first if missing)
- Windows: `winget install -e --id VSCodium.VSCodium`  (or `choco install vscodium`)
- Linux: `snap install codium --classic`  (or the official VSCodium apt/rpm repo)
Then open this folder in it: `codium .`
If installation is blocked (locked-down machine), tell the user and continue — VSCodium is
optional; the chatbot still runs.

## 3. Get the workshop Claude key
Ask the user: **"Paste your workshop Claude API key (from the slide):"** Capture it.
Never echo it back and never write it into any tracked file.

## 4. Create `.env` (it is gitignored)
Copy `.env.example` to `.env` and replace BOTH `sk-ant-REPLACE_ME` placeholders with the
pasted key. Leave `OPENAI_BASE_URL` and `OPENAI_MODEL` as-is.

## 5. Move into the IDE and switch onto Claude (two birds, one move)
Combine the model switch with opening the IDE so the user can WATCH files change as they work.
This repo ships `opencode.json`, which selects a Claude model using the key from `.env`; opencode
loads that key only when it starts. Tell the user EXACTLY this:

> **1.** Press **Ctrl+C** to exit opencode here.
> **2.** In **VSCodium**, open a terminal: **View → Terminal** (or **Ctrl+`**).
> **3.** Run **`opencode`** in that terminal.

That single move (a) reopens opencode **on Claude** (it reads the key from `.env` at startup) and
(b) runs it **inside VSCodium**, so every file opencode creates or edits shows up live in the
file explorer on the left. From here on, work inside VSCodium.

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
