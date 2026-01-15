from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

from score import score

app = FastAPI()


@app.get("/score", response_class=PlainTextResponse)
def get_score():
    return score()
