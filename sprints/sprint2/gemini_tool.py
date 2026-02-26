# gemini_tool.py
import os
from google import genai
from dotenv import load_dotenv

class GeminiTutor:
    def __init__(self):
        load_dotenv()
        api_key = "AIzaSyDtgoGfNrMt2PtZHpnVhzPi_KCqLs_oXxw"
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash-lite"

    def generate_explanation(self, problem_text: str) -> str:
        """Sends extracted text to Gemini for a step-by-step solution."""
        system_prompt = (
            "You are an expert, encouraging homework tutor. "
            "A student has extracted the following text from an image. "
            "Solve the problem step-by-step. Do not just give the final answer. "
            "Explain the concepts simply.\n\n"
            f"Problem Text:\n{problem_text}"
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=system_prompt
            )
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"