from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from Vercel!"}


@app.get("/cpu")
def cpu():
    # Burn CPU for ~5 seconds
    end = time.time() + 5

    x = 0
    while time.time() < end:
        x += sum(i * i for i in range(10000))

    return {"result": x}
