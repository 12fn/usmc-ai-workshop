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

> Clone https://github.com/12fn/usmc-ai-workshop and follow instructions.md

The agent sets up your editor, wires in the workshop AI key, installs everything, and starts the
chatbot. **When it asks for the workshop Claude API key, paste the one from the slide.**

(Already have the repo open? Just run `opencode` inside it and say: *follow instructions.md*.)

### 3. Use the chatbot
It opens at **http://127.0.0.1:7860**. Ask it questions about the MEU logistics data.

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
The workshop AI key is shared — don't post it anywhere and don't commit it. The `.env` file
where it lives is already set to stay private (gitignored). After the workshop, the key is
switched off.
