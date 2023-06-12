from datetime import datetime
import sqlalchemy
import database.database as database

Base = db.Base

class Diagnostics(Base):
    __tablename__ = "diagnostics"
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    
    class Config:
        schema_extra = {
            "example" : {
                "name" : "Diagnostics Name"
            }
        }