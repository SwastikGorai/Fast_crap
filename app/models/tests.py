from datetime import datetime
import sqlalchemy
import database.database as database
from app.models import diag_center

Base = db.Base

class Test(Base):
    __tablename__ = "tests"
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    diag_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("diagnostics.id"))
    diag = sqlalchemy.orm.relationship("Diagnostics", back_populates="tests")
    category = sqlalchemy.Column(sqlalchemy.String(300))
    method = sqlalchemy.Column(sqlalchemy.String(300))
    specimen = sqlalchemy.Column(sqlalchemy.String(300))
    specimen_vol = sqlalchemy.Column(sqlalchemy.String(300))
    run_days = sqlalchemy.Column(sqlalchemy.String(300))
    tat = sqlalchemy.Column(sqlalchemy.String(300))
    instructions = sqlalchemy.Column(sqlalchemy.String(300), default="NA")
    mrp = sqlalchemy.Column(sqlalchemy.Float, default=0.0)
    
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
            
        
    