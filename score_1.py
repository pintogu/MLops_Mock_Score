from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/score", response_class=PlainTextResponse)
def score():
    return "1"
