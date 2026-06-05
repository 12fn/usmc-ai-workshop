# Project notes for AI agents

This repo is a **teaching scaffold** for an AI "vibecoding" workshop — a barebones chatbot people
clone and then make their own. Keep everything simple and beginner-friendly.

## Important: the example is JUST an example
`meu_logistics_data.csv` and the `SYSTEM_PROMPT` in `app.py` are a **sample** use case (Marine
Expeditionary Unit logistics). **A user's idea will often have nothing to do with logistics —
that is expected and fine.** Do NOT steer them back to the logistics example, and do NOT shoehorn
their idea into the sample data. When they want to build something else:
- replace `meu_logistics_data.csv` and the `SYSTEM_PROMPT` with THEIR topic,
- generate fresh sample data for THEIR idea if they don't have any,
- restyle the frontend as needed.
Reuse the **plumbing** (the OpenAI-format model call, the simple web page) — not the logistics
content.

## What the pieces are
- `app.py` — the backend: an OpenAI-format `chat.completions` call. `SYSTEM_PROMPT` is the brains;
  swap the data file to change the domain.
- `static/style.css` — the look; colors live in the `THEME` block at the top.
- `.env` — holds the model key (gitignored); `OPENAI_MODEL` selects the model.

## Run it
`python app.py` → http://127.0.0.1:7860

## Helping beginners
Prefer the smallest change that works, run it, and explain what you did in plain language. When
someone has a bigger idea, point them at the `/prd` command.
