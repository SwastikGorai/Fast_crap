from typing import List, Optional

from pydantic import BaseModel, Field

from database import database

Session = database.SessionLocal


class DiagnosticsBase(BaseModel):
    name: str
    
class DiagnosticsCreate(DiagnosticsBase):
    
    @classmethod
    def create(cls,db : Session = Session, data: DiagnosticsBase = DiagnosticsBase):
        diagnostics = DiagnosticsBase(**data.dict())
        db.add(diagnostics)
        db.commit()
        db.refresh(diagnostics)
        return diagnostics


class Diagnostics(DiagnosticsBase):
    id: int
    
    class Config:
        orm_mode = True
        
        
        
class TestBase(BaseModel):
    name: str
    diag_id: int
    diag : Diagnostics
    category: str
    method: str
    specimen: str
    specimen_vol: str
    run_days: str
    tat: str 
    instructions: str
    mrp: float
    
class TestCreate(TestBase):
    pass

class Test(TestBase):
    id: int
    
    class Config:
        orm_mode = True