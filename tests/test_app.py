import os
os.environ.setdefault("OPENAI_API_KEY", "test-key")
import app as appmod


def test_build_messages_orders_system_history_user():
    msgs = appmod.build_messages([{"role": "user", "content": "earlier"},
                                  {"role": "assistant", "content": "ok"}], "now")
    assert msgs[0]["role"] == "system"
    assert "MEU LOGISTICS DATA" in msgs[0]["content"]
    assert msgs[1] == {"role": "user", "content": "earlier"}
    assert msgs[-1] == {"role": "user", "content": "now"}


def test_chat_route_returns_reply(monkeypatch):
    class FakeMsg:
        content = "stubbed answer"

    class FakeChoice:
        message = FakeMsg()

    class FakeResp:
        choices = [FakeChoice()]

    monkeypatch.setattr(appmod.client.chat.completions, "create",
                        lambda **kw: FakeResp())
    c = appmod.app.test_client()
    r = c.post("/api/chat", json={"message": "hi", "history": []})
    assert r.status_code == 200
    assert r.get_json()["reply"] == "stubbed answer"
