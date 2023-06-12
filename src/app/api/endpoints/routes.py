from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from database.database import get_db
from app.models.diag_center import Diagnostics
from app.models.tests import Test
import Schemas.schemas as schemas



router = APIRouter()


@router.post('/diagnostics', response_description="Add new Diagnostics")
async def add_disgnostic(payload: schemas.DiagnosticsBase, db: Session = Depends(get_db)):
    new_diag = Diagnostics(**payload.dict())
    db.add(new_diag)
    db.commit()
    db.refresh(new_diag)
    return {'status': 'success', 'data': new_diag}
    
    

@router.get('/diagnostics/{id}')
async def get_disgnostic(db: Session = Depends(get_db)):
    get_diag = db.query(Diagnostics).filter(Diagnostics.id == id).first()
    return {'status': 'success', 'data': get_diag}
