function sendText() {
    let text = document.getElementById("text").value;

    if (text.trim() === "") {
        alert("Please enter some text.");
        return;
    }

    fetch("http://127.0.0.1:5000/predict_text", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = "Result: " + data.result;
    })
    .catch(err => {
        document.getElementById("result").innerHTML = "Error: " + err;
    });
}

function sendPDF() {
    let file = document.getElementById("pdfFile").files[0];

    if (!file) {
        alert("Please upload a PDF file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:5000/predict_pdf", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerHTML = "Result: " + data.result;
    })
    .catch(err => {
        document.getElementById("result").innerHTML = "Error: " + err;
    });
}
