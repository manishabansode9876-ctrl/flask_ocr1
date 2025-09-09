# Flask OCR App

This project is a simple web application built with Flask that allows users to upload images and extract text from them using Optical Character Recognition (OCR).

## Features

- Upload images through a web interface
- Extract text from uploaded images using OCR
- View extracted text on the web page
- Stores extracted data for later use

## Folder Structure

```
app.py
extracted_data.pkl
filepath/
requirements.txt
flask_ocr1/
    README.md
templates/
    index.html
uploads/
    img1.png
    img2.png
    ...
```

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required packages:

    ```powershell
    pip install -r requirements.txt
    ```

### Running the App

1. Run the Flask application:

    ```powershell
    python app.py
    ```

2. Open your browser and go to `http://127.0.0.1:5000/` to use the app.

## Usage

- Click "Choose File" to upload an image.
- Click "Upload" to extract text from the image.
- The extracted text will be displayed on the page.

## Dependencies

See `requirements.txt` for a list of required Python packages.

## License

This project is licensed under the MIT License.

## Author

- Your Name
