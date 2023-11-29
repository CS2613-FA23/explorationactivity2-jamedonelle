# PyMuPDF

I decided to do my second exploration project on PyMuPDF. I selected this package since my sister had asked me if I could make a small application that could help her translate english PDFs to french to help her in preparing her work for her students.

## About
PyMuPDF is a high performance library for data extraction, analysis or manipulation for PDF documents that was created in about 2012.[1] This library has many different uses and supports many different types of files. This library gives users the ability to rasterize pdf pages images to help developers manipulate the file at a pixel level. [2] It was designed to be fast and memory efficient for wokring with large PDF files. [3]

## Functionality

```
pdf_document = fitz.open(self.pdf_path)
```
Above you will find the open function used in my sample program. This functions takes a file path to a pdf file and returns a PDF object we use to manipulate.

```
page = pdf_document.load_page(self.page_number - 1)
```
The load_page functions gives developers the ability to load a page object from a given pdf document object. The function is 0-indexed, meaning the pages numbers begins at 0 similar to arrays.

## Influence

This library further helped me understand how powerful python really is. Python has so many free to use packages that it's mind boggling. I make the life of the developer super easy when trying to create small apps, where they might not be too worried about performance, but instead of pure functionality and quick iterations.

## Experience

I would recommend this libary for any type of manipulate for PDF files. It is blistering fast and is very robust in uses. I mainly only used it to extract text and rasterize pages, but this barely scratches the surface of what this library can help with you accomplish.

## References

[1] https://github.com/pymupdf/PyMuPDF

[2] https://pymupdf.readthedocs.io/en/latest/the-basics.html#supported-file-types

[3] https://gggauravgandhi.medium.com/handling-pdf-files-in-python-using-pymupdf-ba0b0b12ddc4



