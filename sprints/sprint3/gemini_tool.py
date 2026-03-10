# gemini_tool.py
import os
from google import genai
from dotenv import load_dotenv

class GeminiTutor:
    def __init__(self):
        load_dotenv()
        
        # 🔒 SECURITY BEST PRACTICE: Load from .env file
        # Make sure your .env file has: GOOGLE_API_KEY=your_actual_key_here
        api_key = os.getenv("GOOGLE_API_KEY") 
        
        # If you MUST hardcode it for a quick test, uncomment the line below:
        # api_key = "Paste_Your_Real_Key_Here"

        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found. Please check your .env file.")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash-lite"

    def generate_explanation(self, problem_text: str) -> str:
        """Sends extracted text to Gemini for a step-by-step solution."""
        
        # RQ-03 Refinement: The "Tutor" Prompt
        system_prompt = (
            "You are an expert, encouraging academic tutor. "
            "A student has uploaded an image of their homework, and the text has been extracted via OCR. "
            "Your task is to help them learn, not just give them the final answer to copy. "
            "\n\nRULES:"
            "\n1. Identify the subject and core concept being tested."
            "\n2. Break the solution down into numbered, easy-to-follow steps."
            "\n3. Briefly explain the 'why' behind the first major step."
            "\n4. If the extracted text looks garbled or incomplete, kindly ask the student to clarify."
            f"\n\nExtracted Problem Text:\n{problem_text}"
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=system_prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"