import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import os
import firebase_admin
from firebase_admin import credentials, firestore
import openai

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "downloading-money",
  "client_email": os.getenv(email),
  "client_id": os.getenv(client_id),
  "auth_uri": os.getenv(auth),
  "token_uri": os.getenv(token),
  "auth_provider_x509_cert_url": os.getenv(auth_provider),
  "client_x509_cert_url": os.getenv(cert_url),
  "universe_domain": "googleapis.com"
})
firebase_admin.initialize_app(cred)

db = firestore.client()

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip() 
    except Exception as e:
        return f"Error processing image: {str(e)}"

def extract_text_from_pdf(pdf_path):
    try:
        pages = convert_from_path(pdf_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text.strip() 

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
    


def analyze_text_with_gpt(text):
    openai.api_key = os.getenv(ai_secret)
    response = openai.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": f"Extracted Text: {text}\n\nBased on the extracted text, provide suggestions on how to save money.",
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
    advice = response.choices[0].message.content
    return advice

def upload_text_to_firestore(file_path, text, advice):
    try:
        doc_ref = db.collection('extracted_texts').document()
        doc_ref.set({
            'file_path': file_path,
            'text': text,
            'advice': advice
        })
        print("Text and advice successfully uploaded to Firestore.")
    except Exception as e:
        print(f"Error uploading to Firestore: {str(e)}")



def main():
    file_path = input("Please enter the path to your file: ")
    extracted_text = process_file(file_path)
    print(extracted_text)
    if not extracted_text.startswith("Error"):
        advice = analyze_text_with_gpt(extracted_text)
        print(f"Money-saving advice: {advice}")
        upload_text_to_firestore(file_path, extracted_text, advice)

if __name__ == "__main__":
    main()
