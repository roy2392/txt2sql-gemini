import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            "dbname": os.getenv("POSTGRES_DB", "userdb"),
            "user": os.getenv("POSTGRES_USER", "postgres"),
            "password": os.getenv("POSTGRES_PASSWORD", "example"),
            "host": os.getenv("POSTGRES_HOST", "localhost"),
            "port": os.getenv("POSTGRES_PORT", "5432")
        }

    def get_connection(self):
        return psycopg2.connect(**self.conn_params)

    def execute_query(self, query: str):
        with self.get_connection() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(query)
                if query.strip().upper().startswith('SELECT'):
                    return [dict(row) for row in cur.fetchall()]
                return []

    def validate_query(self, query: str) -> bool:
        # Add query validation logic here
        forbidden_keywords = ['DROP', 'DELETE', 'UPDATE', 'INSERT', 'TRUNCATE']
        return not any(keyword in query.upper() for keyword in forbidden_keywords)
