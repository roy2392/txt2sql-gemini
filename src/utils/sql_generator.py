import google.generativeai as genai
from typing import Optional

class SQLGenerator:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-pro')
        self.table_schema = """
        Table name: users
        Columns:
        - id (SERIAL PRIMARY KEY)
        - name (VARCHAR)
        - lastname (VARCHAR)
        - age (INTEGER)
        - height (FLOAT)
        - weight (FLOAT)
        """
    
    async def generate_sql(self, question: str) -> str:
        prompt = f"""
        Given the following PostgreSQL table schema:
        {self.table_schema}

        Generate a SQL query to answer this question: {question}

        Rules:
        1. Only generate SELECT queries
        2. Return only the SQL query, nothing else
        3. Use proper SQL syntax for PostgreSQL
        4. Make sure the query is secure and doesn't contain any harmful operations
        """
        
        response = await self.model.generate_content_async(prompt)
        sql_query = response.text.strip()
        
        # Basic validation
        if not sql_query.upper().startswith('SELECT'):
            raise ValueError("Generated query must be a SELECT statement")
        
        return sql_query
