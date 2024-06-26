from text_conversion import process_file
from organise_statement import parse_text
from categorise_spending import categorize_transactions, transactions_to_dataframe

def main():
    file_path = input("Please enter the path to your file: ")
    extracted_text = process_file(file_path)
    if "Error" in extracted_text:
        print(extracted_text)
        return

    transactions = parse_text(extracted_text)
    categorized_transactions = categorize_transactions(transactions)
    df = transactions_to_dataframe(categorized_transactions)

    print(df)

if __name__ == "__main__":
    main()
