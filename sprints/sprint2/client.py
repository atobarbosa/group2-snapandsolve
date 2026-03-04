# client.py
import sys
import os
import requests

SERVER_URL = "http://127.0.0.1:8000/predict"

def check_image_with_server(image_path: str):
    """Sends the image to our local PyTorch server to see if it's a document."""
    print(f"🔍 Analyzing image locally via PyTorch: {image_path}")
    
    try:
        with open(image_path, "rb") as f:
            files = {"file": (os.path.basename(image_path), f, "image/jpeg")}
            response = requests.post(SERVER_URL, files=files)
            
        if response.status_code == 200:
            result = response.json()
            print(f"📊 Server Vision Result: {result['category_name']} (Academic: {result['is_academic']})")
            return result['is_academic']
        else:
            print(f"❌ Server Error: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to server. Is server.py running?")
        return False

def main():
    # 1. Check CLI arguments
    if len(sys.argv) < 2:
        print("Usage: python client.py <path_to_image>")
        sys.exit(1)

    image_path = sys.argv[1]

    # 2. Verify file exists
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    # 3. Test the Server Guardrail (Sprint 2 goal)
    is_academic = check_image_with_server(image_path)
    
    if is_academic:
        print("✅ Guardrail Passed: Image is academic. Proceeding to OCR/Gemini... (Sprint 3 integration)")
    else:
        print("⛔ Guardrail Failed: This image does not look like a document. Aborting to save API costs.")

if __name__ == "__main__":
    main()