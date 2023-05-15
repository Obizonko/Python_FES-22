from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

from lab2.main import Hive

app = FastAPI()


@app.get("/json")
async def root():
    hive: Hive = Hive()
    logs: list[str] = hive.run()
    return {"logs": logs}


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    hive: Hive = Hive()
    logs: list[str] = hive.run()
    logs: str = "<br>".join(logs)
    return HTMLResponse(content=f"<html><body><h1>{logs}</h1></body></html>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)