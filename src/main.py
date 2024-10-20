import uvicorn
from fastapi import FastAPI

app_config = {
    "title": "BankAuth",
    "version": "1.0.0",
    "docs_url": "/bank-auth",
}

app = FastAPI(**app_config)


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)
