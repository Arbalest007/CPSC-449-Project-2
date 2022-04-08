#Program: Project 2 - Microservice Implementation
#Authors: Tianna Cano, Patrick Lin, Raymond Magdaleno, Mark Wiedman
#Date   : 4/8/2022

# "How to initialize the databases & start the services"/"Example commands for methods"

//====Commands in File "AnswerValidation.py"====

Description: 'AnswerValidation.py' handles the database of possible answers, and is responsible for
              setting the color values of each letter for a user's given guess.
              
              /checkAnswer/   - sets color values of letters for a given guess against the daily word
              /add-answer/    - adds a new possible answer to the database
              /remove-answer/ - removes an answer from the database

1) /checkAnswer/
      The 'check-answer' command will call the "answerCheck()" function to initialize 3 empty
   containers which will be used to store the current guess's letter colors.  Firstly, a loop
   will iterate through the word and check for matching letters, and it will set those indexes to
   be green if they match the daily word.  The next loop iterates through the word again while skipping
   any previously set indexes (green indexes).  The loop will then set the indexes of yellow and gray
   letters.  The container holding all of the colors will be returned.
   
2) /add-answer/
      The 'add-answer' command will connect to the "answers.db", which is the answers database, 
   and check whether the new possible answer exists in the database or not.  If it does not
   exist in the database it will add it, otherwise it will return that the word already exists in the
   database.
   
3) /remove-answer/
      The 'remove-answer' command will connect to the "answers.db", and it will check for the given
   word to remove.  If it exists it will remove it, otherwise it will return that the value could not
   be found.

//====Commands in File "WordValidation.py"====

              /validate/     - checks if user guess is valid word
              /add-guess/    - adds a new possible guess to the database
              /remove-guess/ - removes a guess from the database

1) /validate/
      The 'validate' command will connect to the 'words_ms.db', and it will check whether a guess is a
    valid word.  It either returns true if the word is a valid guess, or false if it is invalid.
    
2) /add-guess/
      The 'add-guess' command will connect to the 'words_ms.db', and it will check through the database
    for the word that is a candidate to be added.  If it already exists it will not be added, but if it doesnt
    then it will be.

3) /remove-guess/
      The 'remove-guess' command will connect to the 'words_ms.db', and it will check through the database
    for the word that is a candidate to be deleted.  If the word cannot be found then the command will return
    that the word was unable to be deleted.  Otherwise, the command will remove the word from the database.
