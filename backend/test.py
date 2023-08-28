from config import get_session
from fastapi import FastAPI, Depends
from uvicorn import Server, Config

app = FastAPI()

@app.get("/")
async def root(session = Depends(get_session())):
    print(type(session))
    return 200

@app.post("/")
async def root(session = Depends(get_session())):
    print(type(session))
    return 200

async def main():
    async with get_session() as session:
        print(type(session))

if __name__ == "__main__":
    config = Config(app=app, host="0.0.0.0", port=8000)
    server = Server(config)

    from asyncio import run
    run(server.serve())
    # run(main())

