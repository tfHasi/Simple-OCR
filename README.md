# Simple OCR with Tesseract

A Python script to extract text from images using Tesseract OCR.

## Requirements

- Python 3.7 or higher
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (installed and added to PATH or using .env)
- Python dependencies listed in `requirements.txt`

## Setup

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   
2. **Create a .env file in the project root:**

   ```bash
   # .env
   TESSERACT_PATH="path to tesseract.exe"

3. **Add your test image inside 'sources/' directory as 'image.png'**

4. **Run the Script:**

   ```bash
   python main.py

5. **Output will be provided in the terminal**
