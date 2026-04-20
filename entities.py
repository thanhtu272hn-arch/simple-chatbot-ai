import re

INVALID_NAMES = {
    "sad", "tired", "hungry", "fine", "ok", "okay",
    "good", "bad", "happy"
}


def extract_pattern(text):
    text = text.lower().strip()

    if text.startswith("i like "):
        thing = text.replace("i like ", "", 1)
        thing = thing.split(" and ")[0]
        return f"You like {thing}"

    if text.startswith("i hate "):
        thing = text.replace("i hate ", "", 1)
        thing = thing.split(" and ")[0]
        return f"You dislike {thing}"

    if "because" in text and ("i am" in text or "i feel" in text):
        return f"You often feel this way because {text.split('because', 1)[1].strip()}"

    return None


def extract_entities(text):
    entities = {
        "name": None,
        "age": None,
        "feeling": None
    }

    # AGE
    age_match = re.search(r"\b(i am|i'm)\s+(\d{1,3})\b", text)
    if age_match:
        age = int(age_match.group(2))
        if 0 < age < 120:
            entities["age"] = age

    # NAME
    name_match = re.search(r"\b(my name is|call me)\s+([a-zA-Z ]+)", text)
    if name_match:
        raw = name_match.group(2).strip().title()

        STOP_WORDS = {"and", "i", "am"}

        clean = []
        for w in raw.split():
            if w.lower() in STOP_WORDS:
                break
            clean.append(w)

        name = " ".join(clean[:2])

        if not any(w.lower() in INVALID_NAMES for w in clean):
            entities["name"] = name

    # FEELING
    NEGATIVE = {"sad", "tired", "hungry", "bad"}
    POSITIVE = {"fine", "good", "okay", "great"}

    words = text.split()

    for w in words:
        if w in NEGATIVE:
            entities["feeling"] = w
            return entities

    for w in words:
        if w in POSITIVE:
            entities["feeling"] = w
            return entities

    return entities


def handle_pattern(text, state):
    pattern = extract_pattern(text)

    if not pattern:
        return None

    state.setdefault("memory_patterns", [])
    state["memory_patterns"].append(pattern)
    state["memory_patterns"] = state["memory_patterns"][-5:]

    if text.startswith("i like "):
        return f"Got it — {pattern.lower()}."

    if text.startswith("i hate "):
        return f"Okay — {pattern.lower()}."

    return "I see."
