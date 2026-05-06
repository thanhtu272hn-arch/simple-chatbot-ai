import re
from ml_model import predict_intent

def fake_ai(message, profile):
    text = message.lower()

    intent = predict_intent(text)
    print("🧠 INTENT:", intent)

    # 👇 xử lý theo intent
    if intent == "greet":
        return "Hello! 😄", {}

    if intent == "tell_name":
        name_match = re.search(r"(call me|my name is|i am|i'm)\s+([a-zA-Z ]+)", text)
        if name_match:
            name = name_match.group(2).strip().title()
            return f"Nice to meet you, {name}!", {"name": name}

    if intent == "tell_age":
        age_match = re.search(r"(\d+)", text)
        if age_match:
            age = int(age_match.group(1))
            return f"Got it, you are {age}.", {"age": age}

    if intent == "ask_name":
        if profile["name"]:
            return f"You are {profile['name']}.", {}
        return "I don't know your name yet.", {}

    return "Hmm, I’m not sure. Tell me more!", {}