from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from ai.core import fake_ai
from state_manager import get_user_state
import os
from storage import save_all_users

print("FILES:", os.listdir("."))

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    state = get_user_state(req.user_id)

    if "history" not in state:
        state["history"] = []

    reply = fake_ai(req.message, state)

    # 👉 lưu history
    state["history"].append({
        "user": req.message,
        "bot": reply
    })

    save_all_users()

    return {
        "reply": reply,
        "history": state["history"]  # 👈 thêm cái này
    }


@app.get("/history/{user_id}")
def get_history(user_id: str):
    state = get_user_state(user_id)
    return state["history"]


# 🔥 PHẢI Ở CUỐI
app.mount("/", StaticFiles(directory=".", html=True), name="static")
