from fastapi import APIRouter, HTTPException
from typing import List
from app.models.diag_center import Diagnostics
from app.models.tests import Test
router = APIRouter()


@router.post('/diagnostics', response_description="Add new Diagnostics")
async def add_disgnostic(review: Diagnostics) -> dict:
    await review.create()
    return {"message": "Disgnostic added successfully"}

@router.get('/diagnostics/{id}', response_description="Get a single Diagnostics")
async def get_disgnostic(id: int) -> dict:
    review = await Diagnostics.get(id)
    return review
