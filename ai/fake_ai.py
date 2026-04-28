import re

def fake_ai(message, profile):
    text = message.lower()

    # 👇 nhớ tên
    name_match = re.search(r"(my name is|call me|i am|i'm)\s+([a-zA-Z ]+)", text)
    if name_match:
        name = name_match.group(2).strip().title()
        return f"Nice to meet you, {name}!", {"name": name}

    # 👇 nhớ tuổi
    age_match = re.search(r"(i am|i'm)\s+(\d+)", text)
    if age_match:
        age = int(age_match.group(2))
        return f"Got it, you are {age}.", {"age": age}

    # 👇 hỏi lại
    if "who am i" in text:
        if profile["name"]:
            return f"You are {profile['name']}.", {}
        return "I don't know your name yet.", {}

    if "how old am i" in text:
        if profile["age"]:
            return f"You are {profile['age']} years old.", {}
        return "I don't know your age.", {}

    return "Tell me more...", {}