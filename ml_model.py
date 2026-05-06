from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 🎯 training data
texts = [
    "hello", "hi", "hey", "yo",
    "who am i", "what is my name",
    "i am 35", "i'm 20", "my age is 30",
    "call me john", "my name is anna"
]

labels = [
    "greet", "greet", "greet", "greet",
    "ask_name", "ask_name",
    "tell_age", "tell_age", "tell_age",
    "tell_name", "tell_name"
]

# 🧠 model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)


def predict_intent(text):
    X_test = vectorizer.transform([text])
    return model.predict(X_test)[0]