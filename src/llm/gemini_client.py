import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import List, Dict, Any

load_dotenv()

class GeminiClient:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def generate_response(
            self,
            question: str,
            sql_query: str,
            results: List[Dict[str, Any]]
    ) -> str:
        prompt = f"""
        Question: {question}
        SQL Query: {sql_query}
        Results: {results}

        Please provide a natural language response to the question based on the query results.
        Keep the response concise and focused on the data.
        """
        
        response = await self.model.generate_content_async(prompt)
        return response.text

