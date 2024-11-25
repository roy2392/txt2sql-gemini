from fastapi import FastAPI, HTTPException
from .models import QuestionRequest, QueryResponse
from database.db_manager import DatabaseManager
from llm.gemini_client import GeminiClient
from utils.sql_generator import SQLGenerator

app = FastAPI()
db_manager = DatabaseManager()
gemini_client = GeminiClient()
sql_generator = SQLGenerator()

@app.post("/query", response_model=QueryResponse)
async def process_question(request: QuestionRequest):
    try:
        # Generate SQL query using Gemini
        sql_query = await sql_generator.generate_sql(request.question)
        
        # Execute query
        results = db_manager.execute_query(sql_query)
        
        # Generate natural language response
        natural_response = await gemini_client.generate_response(
                request.question, sql_query, results
        )
        
        return QueryResponse(
                sql_query=sql_query,
                results=results,
                natural_response=natural_response
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
