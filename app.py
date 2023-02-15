from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Work Out Manual"}

@app.get("/man/calculate/{weight}/{height}/{age}")
async def calculate(weight: int, height: int, age: int):
    bmr = weight * 10 + 6.25 * height - 5 * age + 5
    return {"bmr": bmr}

@app.get("/woman/calculate/{weight}/{height}/{age}")
async def calculate(weight: int, height: int, age: int):
    bmr = weight * 10 + 6.25 * height - 5 * age - 161
    return {"bmr": bmr}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')