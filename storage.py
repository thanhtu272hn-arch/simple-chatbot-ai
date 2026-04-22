import json
import os

DATA_FILE = "users.json"


def load_all_users():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_all_users(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)