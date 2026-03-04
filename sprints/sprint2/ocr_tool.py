# ocr_tool.py
import easyocr

class OCRTool:
    def __init__(self):
        print("Initializing EasyOCR (CPU)...")
        # Initialize once to save time on subsequent calls
        self.reader = easyocr.Reader(['en'], gpu=False)

    def extract_text(self, image_path: str) -> str:
        """Reads an image file and returns the extracted text."""
        try:
            # detail=0 returns just the text list, no bounding boxes
            results = self.reader.readtext(image_path, detail=0)
            extracted_text = " ".join(results)
            return extracted_text.strip()
        except Exception as e:
            print(f"OCRTool Error: {e}")
            return ""