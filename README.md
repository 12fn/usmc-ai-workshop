# USMC AI Workshop — Barebones Chatbot

A tiny, hackable AI chatbot for the USMC AI "vibecoding" workshop. You'll get a working chatbot
running on your machine in a few minutes — then make it your own, with an AI coding agent doing
the heavy lifting.

## What's in here
- `app.py` — the whole backend (~50 lines): it sends your message plus a data file to an AI
  model and returns the reply. It uses the **OpenAI API format**, so it works with many models.
- `templates/index.html` + `static/` — the simple chat web page. Colors live in one clearly
  marked block at the top of `static/style.css`.
- `meu_logistics_data.csv` — example data the bot answers questions about. Swap it for your own.
- `instructions.md` — a setup recipe your AI agent runs **for** you.
- `.opencode/commands/prd.md` — a `/prd` command that turns an idea into a plan, then builds it.

## What you'll do — step by step

### 1. Install opencode (the AI coding agent)
- **macOS / Linux:** `curl -fsSL https://opencode.ai/install | bash`
- **Windows:** `scoop install opencode`  (or `npm install -g opencode-ai`)

opencode comes with free models built in, so it works right away.

### 2. Let the agent set everything up
Make a folder for your work, open a terminal in it, and run `opencode`. Then type this one line:

> Clone https://github.com/12fn/usmc-ai-workshop into this folder and follow its instructions.md

The agent installs the **VSCodium** editor, unlocks the workshop AI key (already sealed in the
repo — nothing for you to type), installs everything, and starts the chatbot.

At the end it opens the **VSCodium** editor and asks you to **run `opencode` in VSCodium's
built-in terminal** (Terminal → New Terminal, or Ctrl+`). Do that — now you're working in a real
editor where you can **watch files change as they're edited**, and opencode is running on the
powerful **Claude** model. Work inside VSCodium from here on.

(Already have the repo open? Just run `opencode` inside it and say: *follow instructions.md*.)

### 3. Use the chatbot
It's running at **http://127.0.0.1:7860** — open that in your browser and ask it questions about
the MEU logistics data.

### 4. Make it yours — two easy paths
- **Change how it looks (no coding):** open `static/style.css`, change the colors in the
  `THEME` block at the very top, save, and refresh the page.
- **Change what it does:** open `app.py` and edit `SYSTEM_PROMPT` (the bot's job/personality),
  or swap `meu_logistics_data.csv` for your own data.

Not sure how? Just tell opencode what you want in plain English — e.g. *"make the chat bubbles
blue and rename it to Supply Buddy"* — and let it make the change for you.

### 5. Build your own idea
Have a bigger idea? In opencode, type:

> /prd

It asks you a few simple questions, writes a clear plan (a PRD) into the `prds/` folder, and then
builds it for you step by step — starting from this chatbot's scaffolding.

## A note on the key
The workshop AI key is shared and short-lived. You don't type it or see it — it's sealed
(encrypted) in the repo and the agent unlocks it for you. After the workshop it's switched off.

---

## For the operator (running the workshop)
The attendee flow above needs zero key-typing because the key is **sealed in the repo**, not
pasted. Here's how to set that up and keep it safe:

1. **Make a dedicated, capped key.** Create a fresh Anthropic API key just for this session with a
   hard spend limit. (Don't reuse a long-lived key.)
2. **Seal it into the repo** (the raw key is never committed — only an encrypted blob, which
   GitHub secret-scanning ignores, so it won't be auto-revoked):
   ```
   pip install cryptography
   python3 scripts/seal_key.py "<workshop-password>"   # paste the sk-ant-... key at the prompt
   git add workshop-key.enc && git commit -m "seal workshop key" && git push
   ```
3. **Put the same `<workshop-password>` into `instructions.md` Step 4** (replace
   `WORKSHOP_PASSWORD_HERE`). The password being public is fine — its only protection job is to
   keep the key out of automated secret-scanners; the real safety is operational (next line).
4. **During the session:** watch the key's usage in the Anthropic console; the spend cap is your
   backstop.
5. **Right after the session:** **revoke the key.** That instantly makes `workshop-key.enc` inert,
   regardless of who has the repo. Re-seal a new key next time.

The unlock writes the key into `.env` (the chatbot, via python-dotenv) and into opencode's own
credential store `~/.local/share/opencode/auth.json` (opencode does NOT read `.env`).
