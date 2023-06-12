from typing import List, Optional

from pydantic import BaseModel


class DiagnosticsBase(BaseModel):
    name: str
    
class DiagnosticsCreate(DiagnosticsBase):
    pass

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