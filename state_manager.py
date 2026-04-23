from storage import USER_STATES

def create_default_state():
    return {
        "user_name": None,
        "history": []
    }

def get_user_state(user_id):
    if user_id not in USER_STATES:
        USER_STATES[user_id] = create_default_state()

    state = USER_STATES[user_id]

    if "history" not in state:
        state["history"] = []

    return state