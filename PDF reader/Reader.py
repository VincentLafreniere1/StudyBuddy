from pypdf import PdfReader

reader = PdfReader("Data/2.1 Systèmes LTI.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[11]
text = page.extract_text()
print(text)
