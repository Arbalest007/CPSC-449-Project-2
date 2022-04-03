from typing import List
import sqlite3

#Required to create a request and response body for data
from pydantic import BaseModel
#Define FastAPI HTTP Methods
from fastapi import FastAPI, status

class answerCheck(BaseModel):
    greenIndexes: List[int] = []
    yellowIndexes: List[int] = []
    grayIndexes: List[int] = []

class answers(BaseModel):
    user: str
    server: str

class wordList(BaseModel):
    words: List[str] = None

app = FastAPI()

"""
Validate the answer to identify which letters are:
1. In the word and in the correct spot
2. In the word but in the wrong spot
3. Not in the word in any spot
"""
@app.post('/checkAnswer/')
def check(input: answers):
    #Counter to iterate through for green indexes
    greenCounter = 0

    #Debugging
    print(input.user)
    print(input.server)

    currentCheck = answerCheck()

    for character in input.user:
        # #Debugging
        # print(character)
        # print(input.server[count])
        # if (count + 1) > 4:
        #     continue
        # else:
        #     count += 1


        #If the current character equals the letter in the daily answer string at the same location then
        #add that index to greenIndexes
        if character == input.server[greenCounter]:
            #Debugging
            print(character)
            print(input.server[greenCounter])

            currentCheck.greenIndexes.append(greenCounter)
            greenCounter += 1
        else:
            greenCounter += 1

    """
    If the character exists in the daily answer string then we need to check if it was already marked as green.
    Then we can process whether or not the current index should be marked as yellow or gray depending on
    how many occurrences of this character exist in the answer.

    Example:
    If the answer is "Fewer" and the user guessed "Carer" the first "r" in "Carer" is marked gray, not
    yellow because there is only 1 "r" in the answer and we have already marked it green for the last
    index of "Carer"
    """
    for i in range(len(input.user)): 
        character = input.user[i]

        #If the index already exists as green then we skip to next one
        if not(i in currentCheck.greenIndexes):
            #If the character exists it may be yellow or gray depending on how many occurences there are in the answer
            if character in input.server:
                #Get the total # of occurences the answer has this character
                totalCount = input.server.count(character)

                greenCount = 0
                yellowCount = 0

                #Check how many times we have matched this character exactly
                for a in currentCheck.greenIndexes:
                    if input.server[a] == character:
                        greenCount += 1
                #Check how many times we have marked this character as right letter, wrong place
                for b in currentCheck.yellowIndexes:
                    if input.user[b] == character:
                        yellowCount += 1
                """
                If the total count of yellow + green indexes that represent this character are less than total
                occurences then we can mark it as yellow. Otherwise this duplicate character needs to be marked 
                gray to indicate there are no more occurences of this letter in the answer
                """
                if yellowCount + greenCount < totalCount:
                    currentCheck.yellowIndexes.append(i)
                else:
                    currentCheck.grayIndexes.append(i)
            #Otherwise mark this index as gray if the character doesn't exist in the answer
            else:
                currentCheck.grayIndexes.append(i)
    
    #Return a JSON representing what color each index of the user's guess should be
    return currentCheck

#Add answers
@app.post('/add-guess/', status_code=status.HTTP_202_ACCEPTED)
def add(addWords: wordList):
    #Connect DB
    con = sqlite3.connect("answers.db")
    cur = con.cursor()

    for i in addWords.words:
        try:
            cur.execute("INSERT INTO a VALUES(?)", (i,))
            con.commit()
        except:
            print(i + " already exists in the Answers database")
    
    con.close()

    return "Words added to DB!"

#Remove answers
@app.post('/remove-guess/', status_code=status.HTTP_202_ACCEPTED)
def remove(removeWords: wordList):
    #Connect DB
    con = sqlite3.connect("answers.db")
    cur = con.cursor()

    for i in removeWords.words:
        try:
            cur.execute("DELETE FROM a WHERE Answers = ?", (i,))
            con.commit()
        except:
            print("Unable to delete value of: " + i)
    
    con.close()

    return "Answers removed from DB!"        