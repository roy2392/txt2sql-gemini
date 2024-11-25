from pydantic import BaseModel
from typing import Optional, List, Dict, Any

class QuestionRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql_query: str
    results: List[Dict[str, Any]]
    natural_response: str
