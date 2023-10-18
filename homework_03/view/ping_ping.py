from fastapi import FastAPI

app = FastAPI()


@app.get("/ping/")
def make_ping():
    return {"message": "pong"}
