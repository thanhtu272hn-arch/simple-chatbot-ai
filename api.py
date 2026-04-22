from fastapi import FastAPI
from pydantic import BaseModel

from ai.core import fake_ai
from ai.state import create_default_state
from storage import load_all_users, save_all_users
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_STATES = load_all_users()

class ChatRequest(BaseModel):
    user_id: str
    message: str


def get_user_state(user_id: str):
    if user_id not in USER_STATES:
        USER_STATES[user_id] = create_default_state()
    return USER_STATES[user_id]


@app.post("/chat")
def chat(req: ChatRequest):
    print("BEFORE:", USER_STATES)

    state = get_user_state(req.user_id)

    reply = fake_ai(req.message, state)

    save_all_users(USER_STATES)
    print("AFTER:", USER_STATES)

    return {"reply": reply}


# 🔥 ĐẶT CUỐI CÙNG
app.mount("/", StaticFiles(directory=".", html=True), name="static")
