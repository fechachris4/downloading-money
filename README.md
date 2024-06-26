# downloading-money

This tool aims to extract text from an image or pdf into a string 

This is mostly made possible by Google's Tesseract-OCR Engine. 

Ensure that Google's Tesseract-OCR Engine and poppler is installed so that the pytesseract and pdf2image imports run 

Imports:

pytesseract: This is a Python wrapper for Google's Tesseract-OCR Engine. It allows us to use Tesseract's optical character recognition (OCR) capabilities in Python.

PIL (Pillow): This is a Python Imaging Library that provides easy access to image processing capabilities.

pdf2image: This library converts PDF files into a list of images. Each page of the PDF becomes an image that can be processed individually.

os: This module provides a way of using operating system-dependent functionality like reading or writing to the file system.

