from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "We Love Datascientest, and we did it. We build a CI/CD pipeline <3 8 last chance"}
