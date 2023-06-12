from fastapi import FastAPI
import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

ENV = load_dotenv()

app = FastAPI()
DATABASE_URL = ENV.get("DATABASE_URL")
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
