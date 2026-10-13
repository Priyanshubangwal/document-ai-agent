import pytesseract

# Point exactly to your Windows Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(preprocessed_image) -> str:
    # Extract text from the cleaned image
    extracted_text = pytesseract.image_to_string(preprocessed_image)
    return extracted_text.strip()