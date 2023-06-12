from fastapi import FastAPI
app = FastAPI()
import database.database as database # Folder database -> file database.py

db = database.database # file database.py -> variable database



@app.on_event("startup")
async def startup():
    await db.connect()
    
    
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "AxxinCure API"}



@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
