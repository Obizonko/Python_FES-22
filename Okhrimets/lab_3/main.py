import uvicorn
from fastapi import FastAPI
from simulation import Simulation

app = FastAPI()
s = Simulation()

@app.get("/")
async def index():
   return {"message": s.run_and_get_log()}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)