import pytest
from src.utils.sql_generator import SQLGenerator

@pytest.mark.asyncio
async def test_generate_sql():
    generator = SQLGenerator()
    question = "What is the average age of users?"
    sql_query = await generator.generate_sql(question)
    assert sql_query.upper().startswith('SELECT')
    assert 'FROM users' in sql_query.upper()
