from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "distilgpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


def generate_reply(prompt):
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    outputs = model.generate(
        inputs,
        max_length=100,
        do_sample=True,
        temperature=0.7,
        top_k=50
    )

    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return reply


def build_prompt(history, message):
    prompt = ""

    for msg in history[-5:]:  # lấy 5 câu gần nhất
        role = msg["role"]
        content = msg["content"]

        if role == "user":
            prompt += f"User: {content}\n"
        else:
            prompt += f"Bot: {content}\n"

    prompt += f"User: {message}\nBot:"

    return prompt
