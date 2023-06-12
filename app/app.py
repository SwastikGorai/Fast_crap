from fastapi import FastAPI
app = FastAPI()
import database.database as db



@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()
