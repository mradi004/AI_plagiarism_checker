from flask import Flask, request, jsonify, send_from_directory
from backend.model.predict import predict_text_type
from backend.model.utils import extract_text_from_pdf
import os

app = Flask(__name__)

# -------------------------
# Serve FRONTEND FILES-On loading this will route to open frontend file in the web browser 
# -------------------------
@app.route("/")
def home():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

# -------------------------
# API: CHECK TEXT----- These codes are for sending your input to the backend and then get the result from it 
# -------------------------
@app.route("/predict_text", methods=["POST"])
def check_text():
    data = request.get_json()
    text = data["text"]
    result = predict_text_type(text)
    return jsonify({"result": result})

# -------------------------
# API: CHECK PDF------these codes are for extracting info from the pdf and then predicting the Ai content or Human content 
# -------------------------
@app.route("/predict_pdf", methods=["POST"])
def check_pdf():
    file = request.files["file"]

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    text = extract_text_from_pdf(filepath)
    result = predict_text_type(text)

    os.remove(filepath)
    return jsonify({"result": result})

# -------------------------
# Run App--------Not anything but to run the backend to talk with the frontend and the user
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
