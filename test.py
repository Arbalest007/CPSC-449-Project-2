from fastapi import FastAPI
import json
import sqlite3

with open('answers.json') as f:
   data = json.load(f)
   

app = FastAPI()

@app.get("/")
async def root():
    return {"test": data}
