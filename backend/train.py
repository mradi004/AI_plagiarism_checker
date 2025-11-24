import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
df = pd.read_csv("C:/Users/ASUS/Desktop/AI_PLAGIARISM/datasets/data.csv")


texts = df["text"].tolist()
labels = df["label"].tolist()

# Load embedding model
embedder = SentenceTransformer("all-mpnet-base-v2")

print("Encoding embeddings...")
embeddings = embedder.encode(texts)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    embeddings, labels, test_size=0.2, random_state=42
)

# Train classifier
clf = LogisticRegression(max_iter=4000)
clf.fit(X_train, y_train)

# Ensure model folder exists
os.makedirs("model", exist_ok=True)

# Save model
joblib.dump(clf, "model/classifier.pkl")
joblib.dump(embedder, "model/embedder.pkl")

print("Training completed & model saved!")
