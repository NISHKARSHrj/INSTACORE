import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        user_name TEXT UNIQUE NOT NULL,
        user_password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        content TEXT,
        image_path TEXT,
        timestamp TEXT    
                   
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS likes (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            post_id INTEGER
        )
    """)

    conn.commit()
    conn.close()