from ai.core import fake_ai, save_history, handle_command
from storage import save_user, load_user


def run_chat():
    user_id = "u1"
    state = load_user(user_id)

    print("Bot is running... (type 'exit' to quit)")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        cmd = handle_command(user_input, state)
        if cmd:
            print(f"Bot: {cmd}")
            continue

        reply = fake_ai(user_input, state)

        save_history(state, user_input, reply)
        save_user(user_id, state)

        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chat()
