🧠 AI Plagiarism Checker

A lightweight and fast AI-powered plagiarism detection system that compares user-entered text with AI-generated patterns using Machine Learning + Transformer Embeddings.
The system predicts whether a text is AI-generated or Human-written with high accuracy.

🚀 Features

⚡ Real-time prediction (Human vs AI Generated)

🤖 Uses Sentence-Transformer embeddings

🧠 Machine Learning model (Logistic Regression / SVM)

🌐 Flask backend for API

🧩 Clean UI for testing text

📦 Ready for deployment

🧠 Model Pipeline
Input Text → Text Cleaning → Embedding Model → ML Classifier → Output (AI/Human)

Embedding Model Used

sentence-transformers/all-MiniLM-L6-v2

🔧 Tech Stack

Python, Flask

scikit-learn, numpy, pandas, joblib

Sentence-Transformers

HTML / CSS / JavaScript (UI)

📁 Project Structure
├── backend/
│   ├── app.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── utils/
├── templates/
├── static/
├── README.md
└── requirements.txt

🛠️ How To Run Locally
1️⃣ Clone the repo
git clone https://github.com/<your-username>/AI_plagiarism_checker.git
cd AI_plagiarism_checker

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start server
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000

📊 Results

Add your accuracy details here:

Metric	Score
Training Accuracy	XX%
Test Accuracy	XX%
F1 Score	XX%
🧩 Example Outputs

Human text:

Eating habits of people vary based on their culture and surroundings.
Prediction: Human ✔️

AI text:

The rapid advancement of artificial intelligence continues to redefine innovation.
Prediction: AI Generated 🤖

🚀 Future Enhancements

Add PDF/Text file upload

Add document similarity score (%)

Add plagiarism report export

Improve UI dashboard

👤 Developed By

Aadi Kashyap
Engineering Student | Machine Learning Enthusiast
