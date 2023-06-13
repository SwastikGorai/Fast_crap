from datetime import datetime
from sqlalchemy.orm import  relationship
from sqlalchemy import Column, ForeignKey, Integer, String, ForeignKey, Float
import database.database as database
from . import diag_center

Base = database.Base

class Test(Base):
    __tablename__ = "tests"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    diag_id = Column(Integer, ForeignKey("diagnostics.id"))
    diag = relationship("Diagnostics", backref="tests")
    category = Column(String(300))
    method = Column(String(300))
    specimen = Column(String(300))
    specimen_vol = Column(String(300))
    run_days = Column(String(300))
    tat = Column(String(300))
    instructions = Column(String(300), default="NA")
    mrp = Column(Float, default=0.0)
    
    class Settings:
        orm_mode = True
    
    class Config:
        schema_extra = {
            "example" : {
                "name" : "Test Name",
                "diag_id" : 1,
                "category" : "Test Category",
                "method" : "Test Method",
                "specimen" : "Test Specimen",
                "specimen_vol" : "Test Specimen Volume",
                "run_days" : "Test Run Days",
                "tat" : "Test TAT",
                "instructions" : "Test Instructions",
                "mrp" : 100.0
            }
        }
            
        
    