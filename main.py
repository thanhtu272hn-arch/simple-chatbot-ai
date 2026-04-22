from ai.core import fake_ai, save_history, handle_command
from ai.state import create_default_state
from storage import save_all_users, load_all_users


def run_chat():
    user_id = "u1"

    # 🔥 load tất cả user
    all_users = load_all_users()

    # 🔥 lấy state riêng user
    if user_id not in all_users:
        all_users[user_id] = create_default_state()

    state = all_users[user_id]

    print("Bot is running... (type 'exit' to quit)")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break

        # 🔥 command
        cmd = handle_command(user_input, state)
        if cmd:
            print(f"Bot: {cmd}")
            continue

        # 🔥 AI
        reply = fake_ai(user_input, state)

        # 🔥 save history
        save_history(state, user_input, reply)

        # 🔥 update lại vào all_users
        all_users[user_id] = state

        # 🔥 save file
        save_all_users(all_users)

        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chat()