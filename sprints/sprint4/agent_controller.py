# agent_controller.py
import os
import requests
from ocr_tool import OCRTool
from gemini_tool import GeminiTutor

class AgentController:
    def __init__(self):
        self.server_url = "http://127.0.0.1:8000/predict"
        self.ocr = OCRTool()
        self.tutor = GeminiTutor()

    def check_guardrail(self, image_path: str) -> bool:
        """Sends image to local PyTorch server."""
        try:
            with open(image_path, "rb") as f:
                files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
                response = requests.post(self.server_url, files=files)
            
            if response.status_code == 200:
                result = response.json()
                print(f"👁️ Vision Check: Detected '{result['category_name']}'")
                return result['is_academic']
            return False
        except Exception:
            return False

    def start_interaction(self, image_path: str) -> str:
        """Runs the pipeline and starts the chat."""
        print(f"\n🚀 Agent starting process for: {image_path}")

        print("➡️ Step 1: Validating image content...")
        if not self.check_guardrail(image_path):
             return "⛔ [STOP] Image rejected. Not an academic document."

        print("➡️ Step 2: Extracting text via EasyOCR...")
        extracted_text = self.ocr.extract_text(image_path)
        if not extracted_text or len(extracted_text.strip()) < 3:
            return "⚠️ [STOP] Extraction failed. No readable text found."
        
        print(f"   [Text Found]: '{extracted_text[:40]}...'")

        print("➡️ Step 3: Starting Tutor Session...")
        return self.tutor.start_session(extracted_text)

    def continue_chat(self, user_input: str) -> str:
        """Passes the user's input to Gemini."""
        return self.tutor.reply_to_tutor(user_input)