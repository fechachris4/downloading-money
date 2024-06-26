import pandas as pd

def categorize_transaction(description):
    categories = {
        'Groceries': ['supermarket', 'grocery', 'market'],
        'Dining': ['restaurant', 'cafe', 'dining'],
        'Utilities': ['electric', 'water', 'gas', 'utility'],
        'Entertainment': ['movie', 'theater', 'concert', 'entertainment'],
        'Transport': ['taxi', 'uber', 'bus', 'train', 'transport'],
        # Add more categories and keywords as needed
    }

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword.lower() in description.lower():
                return category
    return 'Other'

def categorize_transactions(transactions):
    for transaction in transactions:
        transaction['category'] = categorize_transaction(transaction['description'])
    return transactions

def transactions_to_dataframe(transactions):
    return pd.DataFrame(transactions)
