import os
import pandas as pd
from pypdf import PdfReader

# ------------------ BASE CLASS ------------------
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)

    def file_exists(self):
        if not os.path.exists(self.file_path):
            return False
        return True

    def read_file(self):
        pass

    def process_file(self):
        pass


# ------------------ TEXT FILE PROCESSOR ------------------
class TextProcessor(FileProcessor):
    def read_file(self):
        if not self.file_exists():
            return f"Error: File '{self.filename}' not found."

        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()

    def process_file(self):
        content = self.read_file()
        if content.startswith("Error"):
            return content
        return f"Processed Text: Found {len(content.split())} words."


# ------------------ PDF FILE PROCESSOR ------------------
class PDFProcessor(FileProcessor):
    def read_file(self):
        if not self.file_exists():
            return f"Error: File '{self.filename}' not found."

        try:
            reader = PdfReader(self.file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            return f"Error reading PDF: {e}"

    def process_file(self):
        if not self.file_exists():
            return f"Error: File '{self.filename}' not found."

        try:
            reader = PdfReader(self.file_path)
            return f"Processed PDF: Extracted text from {len(reader.pages)} pages."
        except Exception as e:
            return f"Error processing PDF: {e}"


# ------------------ EXCEL FILE PROCESSOR ------------------
class ExcelProcessor(FileProcessor):
    def read_file(self):
        if not self.file_exists():
            return f"Error: File '{self.filename}' not found."

        try:
            df = pd.read_excel(self.file_path)
            return df.to_string()
        except Exception as e:
            return f"Error reading Excel: {e}"

    def process_file(self):
        if not self.file_exists():
            return f"Error: File '{self.filename}' not found."

        try:
            df = pd.read_excel(self.file_path)
            return f"Processed Excel: Found {len(df)} rows and {len(df.columns)} columns."
        except Exception as e:
            return f"Error processing Excel: {e}"


# ------------------ POLYMORPHISM IN ACTION ------------------
files = [
    TextProcessor(r"C:\Users\harsh\Documents\basics of python.txt"),
    PDFProcessor(r"C:\Users\harsh\Documents\Sri Harshith Adatravu CV.pdf"),
    ExcelProcessor(r"C:\Users\harsh\Documents\worksheet1.xlsx")  # Ensure file exists
]

for file in files:
    print(f"\n--- Currently Reading: {file.filename} ---")

    content = file.read_file()
    if content.startswith("Error"):
        print(content)
    else:
        print(content[:200] + "...")

    print(file.process_file())
    print("-" * 50)
