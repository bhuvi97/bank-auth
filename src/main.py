import uvicorn
from fastapi import FastAPI
import os

from src.login.router import login_router
from src.signup.router import signup_router

app_config = {
    "title": "BankAuth",
    "version": "1.0.0",
    "docs_url": "/bank-auth",
}

app = FastAPI(**app_config)
app.include_router(login_router)
app.include_router(signup_router)


@app.get("/", include_in_schema=True)
async def root():
    return {"Env Variable for DB_URL": os.getenv("DB_URL")}


if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8083, reload=True)
