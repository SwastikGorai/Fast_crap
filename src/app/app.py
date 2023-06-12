from fastapi import FastAPI
app = FastAPI()
import database.database as database # Folder database -> file database.py
from app.api.endpoints.routes import router as Router # Folder app -> folder api -> file endpoints -> file routes.py


db = database.database # file database.py -> variable database

app = FastAPI()
app.include_router(Router, prefix="/api/v1", tags = ["API"])



@app.on_event("startup")
async def startup():
    await db.connect()
    
    
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "AxxinCure API"}



@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
