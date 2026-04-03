from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@postgres:5432/customer_db"
)

def get_engine():
    for i in range(10):
        try:
            engine = create_engine(DATABASE_URL)
            conn = engine.connect()
            conn.close()
            print("Connected to DB")
            return engine
        except Exception:
            print(f"Waiting for DB... ({i+1}/10)")
            time.sleep(2)

    raise Exception("Could not connect to DB")


engine = get_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()