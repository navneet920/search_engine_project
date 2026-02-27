import json
import os


class Storage:

    @staticmethod
    def save_chunks(chunks, filepath="artifacts/chunks.json"):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_chunks(filepath="artifacts/chunks.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)