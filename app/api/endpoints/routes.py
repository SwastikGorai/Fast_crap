from fastapi import APIRouter, HTTPException
from typing import List
from app.models.diag_center import Diagnostics
from app.models.tests import Test
import Schemas.schemas as schemas


router = APIRouter()


@router.post('/diagnostics', response_description="Add new Diagnostics", response_model=schemas.Diagnostics)
async def add_disgnostic(review: schemas.DiagnosticsCreate) -> dict:
    await review.create()
    return {"message": "Disgnostic added successfully"}

@router.get('/diagnostics/{id}', response_description="Get a single Diagnostics", response_model=schemas.Diagnostics)
async def get_disgnostic(id: int) -> dict:
    review = await Diagnostics.get(id)
    return review
