import cv2
import pytesseract
import os
from dotenv import load_dotenv

load_dotenv()
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

# Load and process image
image = cv2.imread('sources/image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract text
text = pytesseract.image_to_string(gray)
print("Detected Text:\n", text)