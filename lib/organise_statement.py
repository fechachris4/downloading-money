import re

# To fix:
# This does not work until the ocr is more accurate
# Some solutions: image pre-process the image of pdf before tesseract
# clean up the first row - 'Date type Description Paid inf Paid Out] Balance'

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

    return transactions
