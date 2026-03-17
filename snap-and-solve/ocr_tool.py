# ocr_tool.py
import easyocr

class OCRTool:
    def __init__(self):
        print("Initializing EasyOCR...")
        # Set gpu=True. If your PC has a compatible Nvidia GPU and CUDA, 
        # it will run much faster and smoother. If not, it safely falls back to CPU.
        self.reader = easyocr.Reader(['en'], gpu=True)

    def extract_text(self, image_path: str) -> str:
        """Reads an image file and returns the extracted text."""
        try:
            # We add parameters to boost contrast (helps with white text on black background)
            # and set paragraph=False so it stops merging different equations into one line.
            results = self.reader.readtext(
                image_path, 
                detail=0,
                paragraph=False,      # Keeps separate math lines separate
                contrast_ths=0.5,     # Adjusts contrast threshold
                adjust_contrast=0.7   # Boosts contrast for reading
            )
            
            # Join with newlines instead of spaces to preserve the math structure
            extracted_text = " \n".join(results)
            return extracted_text.strip()
        except Exception as e:
            print(f"OCRTool Error: {e}")
            return ""