from fastapi import FastAPI

app = FastAPI()


@app.post("/")
def root(text: str):
    return f"Hello {text}!"
