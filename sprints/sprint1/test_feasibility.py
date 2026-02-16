import os
import easyocr
from google import genai
from dotenv import load_dotenv

# Load API Key from .env file
load_dotenv()
API_KEY = ""

def test_ocr():
    print("\n--- 1. Testing EasyOCR (Local) ---")
    try:
        # Check if test image exists
        if not os.path.exists("test.png"):
            print("❌ Error: 'test.png' not found. Please add an image file to test.")
            return None
        
        print("Loading OCR Model (this may take a minute first time)...")
        reader = easyocr.Reader(['en'], gpu=False) # Force CPU
        result = reader.readtext("test.png", detail=0)
        text = " ".join(result)
        
        if text:
            print(f"✅ OCR Success! Extracted: '{text[:50]}...'")
            return text
        else:
            print("⚠️ OCR ran but found no text.")
            return ""
    except Exception as e:
        print(f"❌ OCR Failed: {e}")
        return None

def test_gemini(extracted_text):
    print("\n--- 2. Testing Google Gemini (Cloud) ---")
    if not API_KEY:
        print("❌ Error: GOOGLE_API_KEY not found in .env file.")
        return

    try:
        client = genai.Client(api_key=API_KEY)
        
        # Simple Prompt
        prompt = f"Explain this text briefly: {extracted_text}" if extracted_text else "Say hello!"
        
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        print(f"✅ Gemini Success! Response: {response.text[:100]}...")
    except Exception as e:
        print(f"❌ Gemini Failed: {e}")

if __name__ == "__main__":
    text_result = test_ocr()
    if text_result is not None:

        test_gemini(text_result)
