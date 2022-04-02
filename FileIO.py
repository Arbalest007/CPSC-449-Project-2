import fileinput
from operator import truediv
import sqlite3

from fastapi import FastAPI
#Required to create a request and response body for data
from pydantic import BaseModel

class userWord(BaseModel):
    guess: str
    valid: bool

app = FastAPI()

#TODO: Figure out where the DB creation code goes
#-----DUPLICATE Code from POST Method Below-----
# #Setup DB for word strings
# con = sqlite3.connect("words_ms.db")
# cur = con.cursor()
# cur.execute("CREATE TABLE t (Words text)")

# #Filter out the strings for Words Microservice from defined source as per Project Reqs
# #and import into sqlite3 DB
# with fileinput.input(files=('/usr/share/dict/words')) as f:
#     for line in f:
#         if line.islower():
#             if line.isascii():
#                 if len(line) <= 5:
#                     if not('\'' in line):
#                         #Debugging
#                         #print(line)

#                         #cur.execute("INSERT INTO t (Words) VALUES (?)", (line,))
#                         cur.execute("INSERT INTO t VALUES(?)", (line,))
#                         con.commit()

#                         #Debugging
#                         #print("Word has been inserted!")

@app.post('/')
def validate(userInput: userWord):
    #Setup DB for word strings
    con = sqlite3.connect("words_ms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE t (Words text)")

    #Filter out the strings for Words Microservice from defined source as per Project Reqs
    #and import into sqlite3 DB
    with fileinput.input(files=('/usr/share/dict/words')) as f:
        for line in f:
            if line.islower():
                if line.isascii():
                    if len(line) <= 5:
                        if not('\'' in line):
                            #Debugging
                            #print(line)

                            #Need to remove \n from end of string
                            cleaned_line = line.replace("\n", "")

                            #cur.execute("INSERT INTO t (Words) VALUES (?)", (line,))
                            cur.execute("INSERT INTO t VALUES(?)", (cleaned_line,))
                            con.commit()

                            #Debugging
                            #print("Word has been inserted!")

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