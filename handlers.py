import random
from datetime import datetime


def handle_name(state):
    if state["user_name"]:
        return f"Your name is {state['user_name']}"
    return "I don't know your name yet"


def handle_age(state):
    if state["age"]:
        return f"You are {state['age']} years old"
    return "I don't know your age yet"


def handle_time():
    return f"It's {datetime.now().strftime('%H:%M:%S')}"


def handle_smalltalk(state):
    if state["user_name"]:
        return f"Hi {state['user_name']}!"
    return random.choice(["Hi!", "Hello!", "Hey!"])


def handle_feeling(state):
    if not state["feeling"]:
        return "How are you feeling?"

    if state["feeling"] in ["sad", "tired", "bad"]:
        return random.choice([
            "I'm here for you.",
            "That doesn't sound great.",
            "Hope things get better."
        ])

    return random.choice([
        "That's great!",
        "Glad to hear that.",
        "Nice!"
    ])


def handle_context(state):
    patterns = state.get("memory_patterns", [])
    notes = state.get("notes", [])
    name = state.get("user_name")
    age = state.get("age")

    # ưu tiên pattern (wow2)
    if patterns:
        return patterns[-1]

    # fallback
    if name and age:
        return f"You're {name}, {age} years old"

    if name:
        return f"You're {name}"

    if age:
        return f"You are {age} years old"

    if notes:
        return notes[-1]

    return "I don't know much about you yet"


def handle_followup(text, state):
    convo = state.get("conversation")
    if not convo:
        return None

    topic = convo.get("topic")
    step = convo.get("step")

    # STEP 1
    if topic == "feeling" and step == "ask_followup":
        state["conversation"]["step"] = "ask_reason"
        return "What happened?"

    # STEP 2
    if topic == "feeling" and step == "ask_reason":
        if len(text.split()) >= 3:
            state["conversation"]["step"] = "respond_empathy"
            return "Why do you feel that way?"

    # STEP 3
    if topic == "feeling" and step == "respond_empathy":
        if len(text.split()) >= 3:
            state["conversation"] = {"topic": None, "step": None}
            return "That sounds really tough."

    return None
