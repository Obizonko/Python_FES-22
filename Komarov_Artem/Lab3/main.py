from fastapi import FastAPI
from BeeFactory import BeeColony, EmployedBee, InspectorBee

app = FastAPI()

@app.get("/run_bee_colony")
async def run_bee_colony():
    x = BeeColony()
    x.run()

    result = {
        "food_sources": [{"coords": source[0], "food_amount": source[1]} for source in x.food_sources],
        "employed_bees": [{"food_amount": bee.food_amount, "current_source": bee.current_source} for bee in x.employed_bees],
        "hive_food_bank": [{"source": source, "food_amount": food_amount} for source, food_amount in x.hive.food_bank.items()]
    }

    return result
