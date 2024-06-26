import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() #remove leading and trailing blanks
    except Exception as e:
        return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text.strip() #remove leading and trailing blanks
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

def process_file(file_path):
    if not os.path.exists(file_path):
        return f"File not found: {file_path}"

    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ['.png', '.jpg', '.jpeg']:
        return extract_text_from_image(file_path)
    elif file_extension.lower() == '.pdf':
        return extract_text_from_pdf(file_path)
    else:
        return f"Unsupported file type: {file_extension}"

def main():
    file_path = input("Please enter the path to your file: ")
    extracted_text = process_file(file_path)
    print(extracted_text)

if __name__ == "__main__":
    main()
