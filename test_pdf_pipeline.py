
from src.components.pdf_loader import PDFLoader
from src.components.preprocessor import Preprocessor

pdf_path = "data/raw/geeta.pdf"

loader = PDFLoader(pdf_path)
raw_text = loader.extract_text()

preprocessor = Preprocessor()
cleaned_text = preprocessor.clean_text(raw_text)

print(cleaned_text[:10000000])  # preview first 1000 characters