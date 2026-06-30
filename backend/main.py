from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def home():
    return {"message": "Hello World."}