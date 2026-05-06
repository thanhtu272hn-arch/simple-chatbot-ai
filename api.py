from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from mini_gpt import generate_reply, build_prompt

from database import init_db
from storage import save_message, load_history, clear_history, get_profile, save_profile

app = FastAPI()

# init DB khi start
init_db()
print("🚨 RUNNING API.PY")


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.on_event("startup")
def on_startup():
    print("🔥 INIT DB START")
    init_db()
    print("🔥 INIT DB DONE")


@app.post("/chat")
def chat(req: ChatRequest):
    history = load_history(req.user_id)

    prompt = build_prompt(history, req.message)

    reply = generate_reply(prompt)

    save_message(req.user_id, "user", req.message)
    save_message(req.user_id, "bot", reply)

    return {"reply": reply}


@app.get("/history/{user_id}")
def history(user_id: str):
    return load_history(user_id)


@app.delete("/history/{user_id}")
def delete_history(user_id: str):
    clear_history(user_id)
    return {"status": "cleared"}


# ⚠️ PHẢI đặt cuối
app.mount("/", StaticFiles(directory=".", html=True), name="static")
