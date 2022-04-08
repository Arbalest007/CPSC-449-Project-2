import json
import sqlite3

#Setup DB for answer strings
con = sqlite3.connect("answers.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS a (Answers TEXT, UNIQUE(Answers))")

f = open('answers.json')
data = json.load(f)

try:
    for i in data:
        cur.execute("INSERT INTO a VALUES(?)", (i,))
        con.commit()
except:
    print("DB is already populated with pre-defined answers!")

con.close()