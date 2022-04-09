###### Program: Project 2 - Microservice Implementation
###### Authors: Tianna Cano, Patrick Lin, Raymond Magdaleno, Mark Wiedman
###### Date   : 4/8/2022

# "How to initialize the databases & start the services"/"Example commands for methods"
- **You can clone this github repo or download and extract the folder onto your machine.**

- **It is required to run the AnswersDB.py and WordsDB.py files before running the procfile! _This is to create and initialize the databases if they do not already exist._**
<br> `$ python3 AnswersDB.py`
<br> `$ python3 WordsDB.py`

- **Then you run the procfile using foreman**
<br> `$ foreman start`
![VirtualBox_Tuffix 2020 Edition_08_04_2022_19_58_09](https://user-images.githubusercontent.com/39601543/162554364-03d65d09-02ec-4de7-83a5-5adcbb0efc2d.png)


> Commands in File "AnswerValidation.py"<br>
> Description: 'AnswerValidation.py' handles the database of possible answers, and is responsible for
              setting the color values of each letter for a user's given guess.
              
              /checkAnswer/   - sets color values of letters for a given guess against the daily word
              /change-answer/    - update future answers

1. /checkAnswer/
      The 'check-answer' command will call the "answerCheck()" function to initialize 3 empty
   containers which will be used to store the current guess's letter colors.  Firstly, a loop
   will iterate through the word and check for matching letters, and it will set those indexes to
   be green if they match the daily word.  The next loop iterates through the word again while skipping
   any previously set indexes (green indexes).  The loop will then set the indexes of yellow and gray
   letters.  The container holding all of the colors will be returned.
   
2. /change-answer/
      The 'change-answer' command will connect to the "answers.db", which is the answers database, 
   and attempt to update the row containing the specified Game ID with a new word using the UPDATE SQL command.

> Commands in File "WordValidation.py" <br>
> Description: 'WordValidation.py' handles the database of possible words, and is responsible for
              validating if a user guess is valid.

              /validate/     - checks if user guess is valid word
              /add-guess/    - adds a new possible guess to the database
              /remove-guess/ - removes a guess from the database

1. /validate/
      The 'validate' command will connect to the 'words_ms.db', and it will check whether a guess is a
    valid word.  It compares the guess against the database to see if it exists as a potential guess. It either returns true if the word is a valid guess, or false if it is invalid.
    
2. /add-guess/
      The 'add-guess' command will connect to the 'words_ms.db'. It takes in a list of words and it will check through the database
    for each word to see if it can be added.  If it already exists it will not be added, but if it doesnt
    then it will be.

3. /remove-guess/
      The 'remove-guess' command will connect to the 'words_ms.db'. It takes in a list of words and it will check through the database
    for each word to see if it can be deleted.  If the word cannot be found then the command will return
    that the word was unable to be deleted.  Otherwise, the command will remove the word from the database.
