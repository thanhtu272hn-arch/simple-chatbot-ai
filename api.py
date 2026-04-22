from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from ai.core import fake_ai
from state_manager import get_user_state, save_state
import os

print("FILES:", os.listdir("."))

app = FastAPI()

class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    state = get_user_state(req.user_id)
    reply = fake_ai(req.message, state)
    save_state()

    return {
        "reply": reply,
        "user_id": req.user_id
    }

# 🔥 PHẢI Ở CUỐI
app.mount("/", StaticFiles(directory=".", html=True), name="static")