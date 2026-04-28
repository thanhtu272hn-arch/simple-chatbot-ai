from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from database import init_db
from storage import save_message, load_history, clear_history, get_profile, save_profile
from ai.fake_ai import fake_ai

app = FastAPI()

# init DB khi start
init_db()


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
    profile = get_profile(req.user_id)

    reply, memory_update = fake_ai(req.message, profile)

    # 💾 save memory nếu có
    if memory_update:
        save_profile(
            req.user_id,
            name=memory_update.get("name"),
            age=memory_update.get("age")
        )

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
