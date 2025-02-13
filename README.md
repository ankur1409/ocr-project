# Patient Assessment OCR Project

This project extracts text from scanned patient assessment forms using OCR, structures the data into JSON format, and stores it in a SQL database.

## Requirements

- Python 3.x
- Libraries:
  - pytesseract
  - Pillow
  - sqlite3

## Setup Instructions

1. **Install Required Libraries**:
   ```bash
   pip install pytesseract Pillow
   ```

2. **Tesseract Installation**:
   - Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
   - Make sure to add Tesseract to your system's PATH.

3. **Database Setup**:
   - Run the SQL script to create the database schema:
   ```bash
   sqlite3 your_database.db < database_setup.sql
   ```

## Usage

1. Update the `image_path` variable in `ocr_processing.py` with the path to your image file.
2. Run the script:
   ```bash
   python ocr_processing.py
   ```

3. The extracted text will be printed in JSON format.

## Sample JSON Output

```json
{
    "patient_assessment": "Extracted text from the image."
}
```

## License

This project is licensed under the MIT License.
