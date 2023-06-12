from datetime import datetime
from pydanic import BaseModel
import sqlalchemy


class Test(BaseModel):
    __tablename__ = "tests"
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    diag_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("diagnostics.id"))
    diag = sqlalchemy.orm.relationship("Diagnostics", back_populates="tests")

    
    