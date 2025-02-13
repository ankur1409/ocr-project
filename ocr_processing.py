import pytesseract
from PIL import Image
import json
import sqlite3

def extract_text_from_image(image_path):
    """Extract text from a given image using OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def structure_data_to_json(extracted_text):
    """Structure the extracted text into JSON format."""
    # Example structure, modify as needed
    data = {
        "patient_assessment": extracted_text
    }
    return json.dumps(data, indent=4)

def main():
    image_path = 'path_to_your_image.jpg'  # Update with your image path
    extracted_text = extract_text_from_image(image_path)
    json_output = structure_data_to_json(extracted_text)
    
    print(json_output)

if __name__ == "__main__":
    main()
