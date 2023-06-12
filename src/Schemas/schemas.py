from typing import List, Optional

from pydantic import BaseModel, Field

from database import database
from app.models.diag_center import Diagnostics

class DiagnosticsBase(BaseModel):
    name: str
    
    class Config:
        arbitrary_types_allowed = True
        orm_mode = True
    
# class DiagnosticsCreate(DiagnosticsBase):
    
#     @classmethod
#     def create(cls, db : Session, data = DiagnosticsBase):
#         diagnostics = DiagnosticsBase(**data.dict())
#         db.add(diagnostics)
#         db.commit()
#         db.refresh(diagnostics)
#         return diagnostics

    
        
        
        
class TestBase(BaseModel):
    name: str
    diag_id: int
    diag : DiagnosticsBase
    category: str
    method: str
    specimen: str
    specimen_vol: str
    run_days: str
    tat: str 
    instructions: str
    mrp: float
    
    class Config:
        orm_mode = True
    
