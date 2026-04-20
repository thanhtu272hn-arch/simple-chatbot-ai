# 🧠 Stateful Chatbot Engine (No ML)

A simple but robust chatbot designed to be predictable, debuggable, and memory-aware — without using machine learning.

> 🎯 Philosophy: Don't make it smarter — make it fail less.

---

## ❌ Problems I Faced

While building earlier versions of this bot, I ran into several real-world issues:

- ML model (LogisticRegression) misclassified intents due to small training data
- Rule-based system with scoring + boosting became unpredictable
- Different components (ML + rules + context) conflicted with each other
- Context rewriting broke user intent
- Over-engineering made debugging extremely difficult

👉 Result: the bot became *less reliable* as complexity increased

---

## ✅ Solution

I redesigned the bot using a clean and minimal architecture:


input
→ normalize
→ extract entities (regex)
→ update state
→ detect intent (simple rules)
→ handler
→ response


No scoring. No ML. No hidden logic.

---

## 🧩 Key Design Decisions

### 1. Entity-first, but controlled
- If user provides info → update state immediately
- But do NOT override strong user intent

### 2. No Machine Learning (yet)
- Small datasets lead to unreliable predictions
- Deterministic logic is easier to debug and control

### 3. One responsibility per step
- normalize → clean text
- extract → get structured data
- detect → find intent
- handler → generate response

### 4. Predictability over intelligence
- The bot should behave consistently
- Debugging should be straightforward

---

## 🧠 Features

### ✅ Memory (Stateful)
- Remembers user name, age, feeling

### ✅ Notes System

/note I like coffee
/recall
/reset


### ✅ Intent Handling
- name
- age
- time
- feeling
- smalltalk

### ✅ Clean fallback
- Handles unknown input gracefully

---

## 💬 Example


You: my name is Tu
Bot: Nice to meet you, Tu!

You: how old am I
Bot: I don't know your age yet

You: I am 30
Bot: Got it, you are 30 years old

You: what about me
Bot: You're Tu, 30 years old

You: /note I like coffee
Bot: Noted: I like coffee

You: /recall
Bot: Here's what I remember:

I like coffee

---

## ▶️ Run

```bash
python main.py
🧪 Tests

Basic tests are included:

pytest
🚀 Future Improvements
Multi-turn conversation (controlled, not messy)
Logging and debugging tools
API version (FastAPI)
Better intent coverage
Optional ML (only with real data)
🧠 What I Learned
More complexity ≠ better system
Mixing ML with rules without enough data is dangerous
Clean architecture makes debugging much easier
Real-world systems fail at integration points, not individual parts
📌 Project Goal

This project is not about building a "smart AI".

It’s about building a reliable system.

📎 Tech
Python
Regex (entity extraction)
Simple rule-based intent detection
👤 Author

Built as a learning project focused on system design, debugging, and clean architecture.