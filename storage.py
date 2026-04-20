import json
import os

DATA_DIR = "users_data"


def _get_path(user_id):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    return os.path.join(DATA_DIR, f"{user_id}.json")


def save_user(user_id, state):
    path = _get_path(user_id)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def load_user(user_id):
    path = _get_path(user_id)

    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return None


def ensure_state_schema(state):
    state.setdefault("user_name", None)
    state.setdefault("age", None)
    state.setdefault("feeling", None)
    state.setdefault("history", [])
    state.setdefault("notes", [])
    return state
