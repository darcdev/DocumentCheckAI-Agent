from fastapi import FastAPI
import uvicorn
from src.config.settings import Settings

app = FastAPI()

settings = Settings()

print(settings.getConfigVariables())


@app.get("/")
async def root():
    return {"message": "Hello World"}
