import pytesseract
from PIL import Image
import json
import sqlite3

def extract_text_from_image(image_path):
    
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def structure_data_to_json(extracted_text):
  

    data = { extracted_text
    }
    return json.dumps(data, indent=4)

def save_json_to_file(json_data, filename):
    with open(filename , 'w') as json_file:
        json_file.write(json_data)

def main():
    image_path = "Screenshot 2024-03-19 195232.png"
    extracted_text = extract_text_from_image(image_path)
    json_output = structure_data_to_json(extracted_text)
    
    # Save the JSON output to a file
    save_json_to_file(json_output, 'extracted_data.json')
    print(f"JSON data saved to 'extracted_data.json'.")

    image_path = "Screenshot 2024-03-19 195232.png"
    extracted_text = extract_text_from_image(image_path)
    json_output = structure_data_to_json(extracted_text)
    
    print(json_output)

if __name__ == "__main__":
    main()
