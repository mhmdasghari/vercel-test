from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"hello": "world"}

@app.get("/cpu")
def cpu():
    end = time.time() + 5
    x = 0
    while time.time() < end:
        x += sum(i * i for i in range(10000))
    return {"x": x}
