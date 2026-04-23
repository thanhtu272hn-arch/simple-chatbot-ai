import json
import threading

FILE = "users.json"
_lock = threading.Lock()

USER_STATES = {}  # ✅ đặt tại đây

def load_all_users():
    global USER_STATES
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            USER_STATES = json.load(f)
    except:
        USER_STATES = {}

def save_all_users():
    with _lock:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(USER_STATES, f, indent=2)