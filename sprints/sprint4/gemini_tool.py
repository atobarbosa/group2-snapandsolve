# gemini_tool.py
import os
from google import genai
from dotenv import load_dotenv

class GeminiTutor:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in .env file")
        
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-2.5-flash-lite"
        self.chat_session = None

    def start_session(self, problem_text: str) -> str:
        """Starts a NEW chat session with the image context."""
        
        # We pass the system instruction in the config for the new SDK
        self.chat_session = self.client.chats.create(
            model=self.model_name,
            config={
                "system_instruction": (
                    "You are an expert, encouraging academic tutor. "
                    "A student has uploaded an image of their homework. "
                    "Help them learn step-by-step. Do not give the final answer immediately. "
                    "Ask guiding questions based on the extracted text."
                )
            }
        )
        
        # Trigger the first analysis
        try:
            response = self.chat_session.send_message(
                f"Here is the extracted text from my homework: {problem_text}\nPlease analyze it and start our tutoring session."
            )
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"

    def reply_to_tutor(self, user_input: str) -> str:
        """Sends the user's reply to the existing chat."""
        if not self.chat_session:
            return "Error: Session not started."
        
        try:
            response = self.chat_session.send_message(user_input)
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"