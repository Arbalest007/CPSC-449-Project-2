from inspect import _void
import sqlite3

#Required to create a request and response body for data
from pydantic import BaseModel
#Define FastAPI HTTP Methods
from fastapi import FastAPI

class userWord(BaseModel):
    guess: str
    valid: bool

app = FastAPI()

#Check if the word is a valid guess by comparing to predefined Words DB
@app.post('/validate/')
def validate(userInput: userWord):
    #Connect DB for word strings
    con = sqlite3.connect("words_ms.db")
    cur = con.cursor()

    #Debugging
    # print("The entered word was: " + userInput.guess)
    # a = cur.execute("SELECT * FROM t").fetchall()
    # for row in a:
    #     print(row)
    
    # #Debugging
    # a = cur.execute("SELECT 1 FROM t WHERE Words = ?", (userInput.guess,)).fetchone()
    # for row in a:
    #     print(row)

    if cur.execute("SELECT 1 FROM t WHERE Words = ?", (userInput.guess,)).fetchone():
        userInput.valid = True

        con.close()
        return userInput.valid
    else:
        userInput.valid = False

        con.close()
        return userInput.valid

#TODO - Feature to remove or add words from the Words DB
#Add a guess to the Words DB
@app.post('/add-guess/')
def add(userInput: userWord):
    print("Hello World. Adding a word here!")

#Remove a guess from the Words DB
@app.post('/remove-guess/')
def remove(userInput: userWord):
    print("Hello World. Removing a word here!")