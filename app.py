import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# ── Model config (OpenAI API format) ──────────────────────────────────────────
# The chatbot talks OpenAI-format to the "Kamiwaza-deployed model" via Anthropic's
# OpenAI-compatible endpoint. Change OPENAI_MODEL in .env to use a different model.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY", ""),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://api.anthropic.com/v1"),
)
MODEL = os.environ.get("OPENAI_MODEL", "claude-haiku-4-5-20251001")

# ── The use case: your data goes into the system prompt ───────────────────────
# ↓↓↓ TECHNICAL: change this file (and this prompt) to build your own use case ↓↓↓
with open("meu_logistics_data.csv") as f:
    DATA = f.read()

SYSTEM_PROMPT = f"""You are a logistics analyst for Marine Expeditionary Unit (MEU) operations.
Use the data below to answer questions. Always reference specific numbers with units.
--- MEU LOGISTICS DATA ---
{DATA}
--- END DATA ---
"""

app = Flask(__name__)


def build_messages(history, message):
    return [{"role": "system", "content": SYSTEM_PROMPT}, *history,
            {"role": "user", "content": message}]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    body = request.get_json(force=True) or {}
    messages = build_messages(body.get("history", []), body.get("message", ""))
    resp = client.chat.completions.create(model=MODEL, messages=messages)
    return jsonify({"reply": resp.choices[0].message.content})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=7860, debug=True)
