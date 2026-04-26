import re

def fake_ai(message, history=None):
    text = message.lower()

    # 👇 nhớ tên
    name_match = re.search(r"(my name is|call me|i am|i'm)\s+([a-zA-Z ]+)", text)
    if name_match:
        name = name_match.group(2).strip().title()
        return f"Nice to meet you, {name}!"

    # 👇 nhớ tuổi
    age_match = re.search(r"(i am|i'm)\s+(\d+)", text)
    if age_match:
        age = age_match.group(2)
        return f"Got it, you are {age} years old."

    # 👇 hỏi lại tên
    if "who am i" in text:
        if history:
            for msg in reversed(history):
                if msg["role"] == "bot" and "Nice to meet you" in msg["content"]:
                    return "You told me your name already 😉"
        return "I don't know your name yet."

    if "hello" in text:
        return "Hi there!"

    return "Tell me more..."