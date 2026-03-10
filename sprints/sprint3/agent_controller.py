# agent_controller.py
import os
import requests
from ocr_tool import OCRTool
from gemini_tool import GeminiTutor

class AgentController:
    def __init__(self):
        self.server_url = "http://127.0.0.1:8000/predict"
        # Initialize our local tools
        self.ocr = OCRTool()
        self.tutor = GeminiTutor()

    def check_guardrail(self, image_path: str) -> bool:
        """UC Step 2 & 4: Sends image to local PyTorch server to verify it's academic."""
        try:
            with open(image_path, "rb") as f:
                files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
                response = requests.post(self.server_url, files=files)
            
            if response.status_code == 200:
                result = response.json()
                print(f"👁️ Vision Check: Detected '{result['category_name']}'")
                return result['is_academic']
            else:
                print(f"❌ Server Error: {response.text}")
                return False
        except requests.exceptions.ConnectionError:
            print("❌ Error: PyTorch server is not running. Please run 'python server.py' first.")
            return False

    def process_request(self, image_path: str) -> str:
        """The main flow integration combining all steps."""
        print(f"\n🚀 Agent starting process for: {image_path}")

        # 1. Guardrail Check (UC Step 4 & UC Alt Flow A)
        print("➡️ Step 1: Validating image content...")
        is_valid = self.check_guardrail(image_path)
        
        if not is_valid:
            # Alt Flow: Invalid Image
            return "⛔ [AGENT STOP] Image rejected. Content does not appear to be an academic document."

        # 2. Text Extraction (UC Step 5)
        print("➡️ Step 2: Extracting text via EasyOCR...")
        extracted_text = self.ocr.extract_text(image_path)
        
        # Alt Flow: Blurry Text / No Text Found
        if not extracted_text or len(extracted_text.strip()) < 3:
            return "⚠️ [AGENT STOP] Extraction failed. The text is too blurry or no text was found. Please retake the photo."
        
        print(f"   [Text Found]: '{extracted_text[:50]}...'")

        # 3. Gemini Reasoning (UC Step 6 & RQ-03)
        print("➡️ Step 3: Consulting Gemini Tutor...")
        explanation = self.tutor.generate_explanation(extracted_text)
        
        return explanation