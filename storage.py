import json
import os
from threading import Lock

FILE = "data.json"
_lock = Lock()


def load_all_users():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_all_users(USER_STATES):
    with _lock:  # 🔥 tránh race condition cơ bản
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(USER_STATES, f, indent=2)
