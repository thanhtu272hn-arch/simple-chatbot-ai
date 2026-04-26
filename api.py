from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from database import init_db
from storage import save_message, load_history, clear_history
from ai.fake_ai import fake_ai

app = FastAPI()

# init DB khi start
init_db()


class ChatRequest(BaseModel):
    user_id: str
    message: str


@app.post("/chat")
def chat(req: ChatRequest):
    reply = fake_ai(req.message)

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