from ai.state import create_default_state
from storage import load_all_users, save_all_users

USER_STATES = load_all_users()


def get_user_state(user_id):
    if user_id not in USER_STATES:
        USER_STATES[user_id] = create_default_state()

    state = USER_STATES[user_id]

    # 👉 FIX quan trọng
    if "history" not in state:
        state["history"] = []

    return state


def save_state():
    save_all_users(USER_STATES)
