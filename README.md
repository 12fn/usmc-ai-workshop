# USMC AI Workshop — Barebones Chatbot

A tiny OpenAI-API-format chatbot for the USMC AI vibecoding workshop.

**The workshop flow:** install [opencode](https://opencode.ai), then tell it:
*"clone this repo and follow instructions.md."* The agent sets up your IDE, wires the Claude
key, and runs this app.

**Two ways to play:**
- **Change how it looks** — edit the THEME colors at the top of `static/style.css`.
- **Build your own thing** — edit `app.py`: the system prompt, the data file, or the model.

**Run it yourself:**
```bash
cp .env.example .env      # paste your key into both *_API_KEY lines
pip install -r requirements.txt
python app.py             # → http://127.0.0.1:7860
```
