def create_default_state():
    return {
        "user_name": None,
        "age": None,
        "feeling": None,
        "history": [],
        "notes": [],
        "memory_patterns": [],
        "conversation": {
            "topic": None,
            "step": None
        }
    }