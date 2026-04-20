import random
from handlers import (
    handle_name, handle_age, handle_followup, handle_time,
    handle_context, handle_feeling, handle_smalltalk)
from entities import extract_entities, extract_pattern
from ai.state import create_default_state


def normalize(text):
    text = text.lower().strip()

    replacements = {
        "what's": "what is",
        "whats": "what is",
        "i'm": "i am"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


def update_state(state, entities):
    if entities.get("name"):
        state["user_name"] = entities["name"]

    if entities.get("age") is not None:
        state["age"] = entities["age"]

    if entities.get("feeling"):
        state["feeling"] = entities["feeling"]

        # 🔥 start conversation
        state["conversation"] = {
            "topic": "feeling",
            "step": "ask_followup"
        }


def detect_intent(text):
    text = f" {text} "

    if any(x in text for x in [" what time ", " current time "]):
        return "time"

    if any(x in text for x in [" how old ", " my age "]):
        return "age"

    if any(x in text for x in [" my name ", " who am i "]):
        return "name"

    if any(x in text for x in [" sad ", " tired ", " hungry "]):
        return "feeling"

    if any(x in text for x in [" hi ", " hello ", " hey "]):
        return "smalltalk"

    if "what about me" in text:
        return "context"

    return None


def fallback(text):
    if "?" in text:
        return "That's an interesting question."
    return random.choice([
        "I see.",
        "Tell me more.",
        "Interesting..."
    ])


def save_history(state, user, bot):
    state["history"].append({"user": user, "bot": bot})

    if len(state["history"]) > 10:
        state["history"].pop(0)


def fake_ai(user_input, state):
    text = normalize(user_input)

    # 1. followup
    follow = handle_followup(text, state)
    if follow:
        return follow

    # 2. entities
    entities = extract_entities(text)
    update_state(state, entities)

    if entities.get("name"):
        return f"Nice to meet you, {state['user_name']}!"

    if entities.get("age"):
        return f"Got it, you are {state['age']} years old."

    # 3. pattern
    pattern = extract_pattern(text)
    if pattern:
        state["memory_patterns"].append(pattern)
        state["memory_patterns"] = state["memory_patterns"][-5:]

        if "like" in text:
            return "Nice! I’ll remember that."
        if "hate" in text:
            return "Got it. Noted."
        return "I see."

    # 4. intent
    intent = detect_intent(text)

    # reset convo nếu hỏi info
    if intent in ["name", "age", "time", "context"]:
        state["conversation"] = {"topic": None, "step": None}

    # 5. handler
    reply = route_intent(intent, state)
    if reply:
        return reply

    # 6. fallback
    return fallback(text)


def handle_command(user_input, state):
    text = user_input.strip()

    # /note something
    if text.startswith("/note "):
        note = text.replace("/note ", "", 1).strip()

        if note:
            state.setdefault("notes", [])  # fix
            state["notes"].append(note)
            return f"Noted: {note}"
        return "What do you want me to note?"

    # /recall
    if text == "/recall":
        notes = state.get("notes", [])
        patterns = state.get("memory_patterns", [])

        all_memory = notes + patterns

        if not all_memory:
            return "I don't remember anything yet."

        return "Here's what I remember:\n- " + "\n- ".join(all_memory)

    # /reset
    if text == "/reset":
        state.clear()
        state.update(create_default_state())
        return "Memory cleared."

    return None


def route_intent(intent, state):
    if intent == "name":
        return handle_name(state)

    if intent == "age":
        return handle_age(state)

    if intent == "time":
        return handle_time()

    if intent == "context":
        return handle_context(state)

    if intent == "smalltalk":
        return handle_smalltalk(state)

    if intent == "feeling":
        return handle_feeling(state)

    return None
