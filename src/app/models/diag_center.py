from datetime import datetime
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKey, Float

import database.database as database
from app.models import tests
Base = database.Base

class Diagnostics(Base):
    __tablename__ = "diagnostics"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(   String(100))
    
    class Config:
        schema_extra = {
            "example" : {
                "name" : "Diagnostics Name"
            }
        }