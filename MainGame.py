from Live import load_game, welcome
from Score import add_score
#print(welcome("Guy"))
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def start_all(name: str):
    print(welcome(name))
    result, difficulty = load_game()
    if result:
        new_score = add_score(difficulty)
    else:
        new_score = "Did not win this time, sorry!"
    return {'Score ' + str(new_score) + '!'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5012, log_level="info")
