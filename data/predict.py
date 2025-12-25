import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load data
data = pd.read_csv("data/quotes.csv")

X = data["quote"]
y = data["label"]

# Train model
vectorizer = TfidfVectorizer(stop_words="english")
X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vectorized, y)

# Test quotes
test_quotes = [
    "Work hard and success will follow",
    "Consistency is the key to long term success",
    "Just believe and the universe will respond"
]

predictions = model.predict(vectorizer.transform(test_quotes))

for quote, label in zip(test_quotes, predictions):
    print(f'"{quote}" → {label}')
