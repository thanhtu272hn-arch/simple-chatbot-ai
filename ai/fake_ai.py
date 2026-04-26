def fake_ai(message):
    text = message.lower()

    if "hello" in text:
        return "Hi there!"
    if "name" in text:
        return "I don't know your name yet 😄"

    return "Tell me more..."