from flask import Flask, request, render_template
import pickle
import os
from PIL import Image
import pytesseract

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure Tesseract (Windows users need this line)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import re
import pickle

# Function to extract details
def extract_details(text: str) -> dict:
    dob = re.findall(r"\d{2}[-/]\d{2}[-/]\d{4}", text)
    aadhaar = re.findall(r"\d{4}\s\d{4}\s\d{4}", text)
    pan = re.findall(r"[A-Z]{5}[0-9]{4}[A-Z]", text)
    ifsc = re.findall(r"[A-Z]{4}0\d{6}", text)

    return {
        "DOB": dob[0] if dob else None,
        "Aadhaar": aadhaar[0] if aadhaar else None,
        "PAN": pan[0] if pan else None,
        "IFSC": ifsc[0] if ifsc else None
    }

# Save function as pickle
with open("extracted_data.pkl", "wb") as f:
    pickle.dump(extract_details, f)

# Load pickle model (must contain a function like extract_details)
with open("extracted_data.pkl", "rb") as f:
    loaded_data = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None
    extracted_text = None

    if request.method == "POST":
        if "image" not in request.files:
            return "No file uploaded", 400

        file = request.files["image"]
        if file.filename == "":
            return "No selected file", 400

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # OCR extraction
        img = Image.open(filepath)
        extracted_text = pytesseract.image_to_string(img)

        # Apply pickle function
        if callable(loaded_data):
            results = loaded_data(extracted_text)  # If pickle contains function
        else:
            results = loaded_data  # If pickle is just pre-extracted data

    return render_template("index.html", results=results, text=extracted_text)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
