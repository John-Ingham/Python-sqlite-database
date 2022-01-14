# Don't need this using Django
# 
# 

import sqlite3

conn = sqlite3.connect('candidate.db') #file or in memory database

c = conn.cursor()

# c.execute("""CREATE TABLE candidates (
#                           name text,
#                           candidate_ref text)
#                           """)

# c.execute("""CREATE TABLE candidate_scores (
#                           candidate_ref text,
#                           scores real)
#                           """)

# c.execute("INSERT INTO candidates VALUES ('Test candidate', 'ref001')")  # basic insertion - works
# c.execute("INSERT INTO candidates VALUES ('{}', '{}'".format())

c.execute("SELECT * FROM candidates WHERE name='Test candidate'")  ## selects from db

print(c.fetchone())   ## fetches one matching result

#print(c.fetchall())  - this will fetch all entries that match the sql criteria given

conn.commit()  ## commits (??) save step?

conn.close() #  closes connection to the db