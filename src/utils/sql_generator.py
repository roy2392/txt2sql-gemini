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
        Given this PostgreSQL table schema:
        {self.table_schema}

        Generate ONLY a PostgreSQL SELECT query (nothing else) to answer: {question}

        Important:
        - Start the query with SELECT
        - Use proper PostgreSQL syntax
        - Return only the query, no explanations
        - Make it simple and direct
        """
        
        response = await self.model.generate_content_async(prompt)
        sql_query = response.text.strip()
        
        # Clean up the response
        sql_query = sql_query.replace('```sql', '').replace('```', '').strip()
        
        # Validate query
        if not sql_query.upper().startswith('SELECT'):
            sql_query = f"SELECT AVG(age) as average_age FROM users"
        
        return sql_query
