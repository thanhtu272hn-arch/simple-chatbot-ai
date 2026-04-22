from fastapi import FastAPI
from pydantic import BaseModel

from ai.core import fake_ai
from state_manager import get_user_state, save_state

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    state = get_user_state(req.user_id)

    reply = fake_ai(req.message, state)

    save_state()  # 🔥 save sau mỗi request

    return {
        "reply": reply,
        "user_id": req.user_id
    }