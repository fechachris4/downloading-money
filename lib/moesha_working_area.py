import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os
import re

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

def parse_text(text):
# Assuming each transaction is on a new line, parse the transactions
    lines = text.split('\n')
    transactions = []

    for line in lines:
        # Regular expression to extract date, description, and amount
        match = re.match(r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+([\d,.]+)', line)
        if match:
            date, description, amount = match.groups()
            transactions.append({
                'date': date,
                'description': description,
                'amount': float(amount.replace(',', ''))
            })

    return lines


a = extract_text_from_image('/Users/moeshakeswani/Projects/Empower_Pennies_Hackathon/tests/data/RBS-Bank-Statement-TemplateLab.com_ copy 2.jpg')
print(parse_text(a))
# print(a)