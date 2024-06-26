# Prompts the user for a file path, extracts the text into a string and prints the string or any error messages.
from lib.text_conversion import extract_text_from_image
from lib.text_conversion import extract_text_from_pdf
from lib.text_conversion import process_file
import pytest

# If given an empty image, returns an empty string
def test_empty_image_returns_empty_string():
    result = extract_text_from_image('tests/data/empty_image.jpg')
    expected = ""
    assert result == expected 

# If given an image with text, returns the text as a string
def test_returns_string_from_image():
    result = extract_text_from_image('tests/data/test_image.jpg')
    expected = "This is sample text from an image."
    assert result == expected 

# # If unable to process image file provided, throw error message
# def test_returns_image_error_message():
#     with pytest.raises(Exception) as e:
#         extract_text_from_image('tests/data/empty_pdf.pdf')
#     error_message = str(e.value)
#     assert "Error processing image" in error_message

# If given an empty pdf, returns an empty string
# def test_empty_pdf_returns_empty_string():
#     result = extract_text_from_pdf('tests/data/empty_pdf.pdf')
#     expected = ""
#     assert result == expected 

# # If given a multi page pdf with text, returns the text as a string
# def test_returns_string_from_single_page_pdf():
#     result = extract_text_from_pdf('tests/data/multi_pdf.pdf')
#     expected = "This is sample text from the first page of a\nmulti page pdf.\nThis is sample text from the second page\nof a multi page pdf."
#     assert result == expected 
