import uvicorn
from fastapi import FastAPI
from simulation import Simulation

app = FastAPI()
s = Simulation()
s.run_simulation()

@app.get("/")
async def index():
   return {"logs": s.get_logs()}

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)