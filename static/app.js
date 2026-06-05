const log = document.getElementById("log");
const form = document.getElementById("f");
const input = document.getElementById("m");
const history = [];

function add(role, text) {
  const d = document.createElement("div");
  d.className = "msg " + (role === "user" ? "user" : "bot");
  d.textContent = text;
  log.appendChild(d);
  log.scrollTop = log.scrollHeight;
  return d;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = input.value.trim();
  if (!message) return;
  input.value = "";
  add("user", message);
  const pending = add("bot", "…");
  try {
    const r = await fetch("/api/chat", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ message, history }),
    });
    const data = await r.json();
    pending.textContent = data.reply;
    history.push({ role: "user", content: message });
    history.push({ role: "assistant", content: data.reply });
  } catch (err) {
    pending.textContent = "Error: " + err.message;
  }
});
