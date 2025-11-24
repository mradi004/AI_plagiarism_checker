import joblib

# Load model and embedder
clf = joblib.load("backend/model/classifier.pkl")
embedder = joblib.load("backend/model/embedder.pkl")

def predict_text_type(text):
    emb = embedder.encode([text])
    pred = clf.predict(emb)[0]
    return "AI-Generated" if pred == 1 else "Human-Written"
