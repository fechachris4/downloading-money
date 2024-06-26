import pytesseract
import pdf2image
from PIL import Image 

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() #remove leading and trailing blanks
    except Exception as e:
        print(f"Error processing image: {str(e)}") 
        # return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_path):
        pages = pdf2image.convert_from_path(pdf_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text

extract_text_from_image('tests/data/empty_pdf.pdf')
# extract_text_from_pdf('/Users/moeshakeswani/Projects/Empower_Pennies_Hackathon/test_pdf.pdf')
# print(extract_text_from_pdf('/Users/moeshakeswani/Projects/Empower_Pennies_Hackathon/test_pdf.pdf'))
# print(extract_text_from_image('/Users/moeshakeswani/Projects/Empower_Pennies_Hackathon/RBS-Bank-Statement-TemplateLab.com_.jpg'))