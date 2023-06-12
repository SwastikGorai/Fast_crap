from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)
database = databases.Database(DATABASE_URL) # <- this database variable is used in app\app.py as db
engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
