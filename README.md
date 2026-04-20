🤖 Simple Chatbot AI

A lightweight rule-based chatbot built with clean architecture (no ML, no over-engineering).

🚀 Features
👤 Remembers your name and age
😊 Detects feelings (sad, tired, hungry…)
💬 Simple follow-up conversation
🧠 Memory system:
/note something
/recall
❤️ Learns preferences:
“I like coffee”
“I hate mornings”
🧠 Architecture

Clean modular design:

ai/
 ├── core.py        # main logic (fake_ai)
 ├── state.py       # user state
entities.py         # extract data from input
handlers.py         # response logic
storage.py          # save/load user
main.py             # CLI app
▶️ Run
python main.py
🧪 Test
pytest
💡 Example
You: my name is Tu
Bot: Nice to meet you, Tu!

You: i am 30
Bot: Got it, you are 30 years old.

You: i am sad
Bot: What happened?

You: work is stressful
Bot: I understand. That can be tough.
📌 Commands
Command	Description
/note something	save a note
/recall	show memory
/reset	clear memory
💡 Philosophy

Don't make the bot smarter — make it fail less.

🔧 Tech
Python
Regex (entity extraction)
Rule-based intent system
🚀 Future Improvements
Add controlled context system
Improve multi-turn conversation
Add ML when enough real data
👨‍💻 Author

Built as a learning project to practice clean architecture and chatbot design.