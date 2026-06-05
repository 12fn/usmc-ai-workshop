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

## 5. Switch opencode off the free model onto Claude
This repo ships `opencode.json`, which selects `anthropic/claude-sonnet-4-5` using the key
from `.env`. Tell the user: **"Restart opencode in this folder to switch from the free model
to Claude."** (It takes effect on the next opencode start.)

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
