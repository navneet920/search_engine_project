import re
from src.logger.logger import logging
from src.exception import CustomException
import sys

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Preprocessor:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text: str) -> str:
        """
        Clean extracted PDF text.
        """
        try:
            logging.info("Starting text cleaning process.")

            # Remove chapter summary
            text = re.sub(r'chapter summary.*?(?=\d+\.\d+|$)', '', text, flags=re.IGNORECASE | re.DOTALL)

            # Remove NOTE blocks
            text = re.sub(r'note:.*?(?=\d+\.\d+|$)', '', text, flags=re.IGNORECASE | re.DOTALL)

            # 🔹 Remove URLs (http, https, www)
            text = re.sub(r'http\S+|www\.\S+', '', text)

            # 🔹 Remove email addresses
            text = re.sub(r'\S+@\S+', '', text)

            # Fix hyphen line breaks (e.g., unright- eousness)
            text = re.sub(r'-\s+', '', text)

            # Remove stray brackets
            text = re.sub(r'[()]', '', text)

            # Remove anything inside brackets
            text = re.sub(r'\(.*?\)', '', text)

            # Remove non-letters
            text = re.sub(r'[^a-zA-Z\s]', ' ', text)

            # Remove page numbers like "Page 1"
            text = re.sub(r'Page\s+\d+', '', text)

            # Remove standalone numbers (often page numbers)
            text = re.sub(r'\n\d+\n', '\n', text)

            # Remove multiple spaces
            text = re.sub(r'\s+', ' ', text)

            # Remove special characters except punctuation
            text = re.sub(r'[^a-zA-Z0-9.,!?;:\s]', '', text)

            # Convert to lowercase
            text = text.lower()

            #  Tokenization
            tokens = word_tokenize(text)

            # Stopword removal
            tokens = [word for word in tokens if word not in self.stop_words]

            #  Lemmatization
            tokens = [self.lemmatizer.lemmatize(word) for word in tokens]

            #  Remove short tokens
            tokens = [word for word in tokens if len(word) > 2]

            cleaned_text = " ".join(tokens)

            logging.info("Text cleaning completed.")
            return text.strip()

        except Exception as e:
            logging.error("Error occurred during text cleaning.")
            raise CustomException(e, sys)
