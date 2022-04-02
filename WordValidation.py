from array import array
from typing import (List, Tuple)
import sqlite3

#Required to create a request and response body for data
from pydantic import BaseModel
#Define FastAPI HTTP Methods
from fastapi import FastAPI, status

class userWord(BaseModel):
    guess: str

class wordList(BaseModel):
    words: List[str] = None

app = FastAPI()

#Check if the word is a valid guess by comparing to predefined Words DB
@app.post('/validate/', status_code=status.HTTP_200_OK)
def validate(userInput: userWord):
    #Connect DB
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
        con.close()
        return True
    else:
        con.close()
        return False

#Add guesses to the Words DB
@app.post('/add-guess/', status_code=status.HTTP_202_ACCEPTED)
def add(addWords: wordList):
    # #Debugging
    # for i in addWords.words:
    #     print(i)

    #Connect DB
    con = sqlite3.connect("words_ms.db")
    cur = con.cursor()

    for i in addWords.words:
        try:
            cur.execute("INSERT INTO t VALUES(?)", (i,))
            con.commit()
        except:
            print(i + " already exists in the Words database")
    
    con.close()

    return "Words added to DB!"

#Remove guesses from the Words DB
@app.post('/remove-guess/', status_code=status.HTTP_202_ACCEPTED)
def remove(removeWords: wordList):
    #Connect DB
    con = sqlite3.connect("words_ms.db")
    cur = con.cursor()

    for i in removeWords.words:
        try:
            cur.execute("DELETE FROM t WHERE Words = ?", (i,))
            con.commit()
        except:
            print("Unable to delete value of: " + i)
    
    con.close()

    return "Words removed from DB!"