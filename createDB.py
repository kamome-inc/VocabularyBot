import sqlite3
import os
dbname = 'firsttest.db'

if os.path.isfile(dbname):
    os.remove(dbname)
    print("success")
else:
    print("File doesn't exists!")

conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute("""
            Create Table Word (
            id integer primary key AUTOINCREMENT,
            RusWord text,
            EngWord text,
            Comment text,
            IsRusToEng bool);
""")

cur.execute("""
            create table User (
            Id integer primary key,
            FirstName text,
            LastName text,
            UserName text);
""")



cur.execute("""
        Insert INTO Word (RusWord, EngWord, Comment, IsRusToEng) VALUES 
        ('слово1','word1',"",1),
        ('слово2','word2',"",1),
        ('слово3','word3',"",1),
        ('слово4','word4',"",1),
        ('слово5','word5',"",1)
        
        ;
""")
conn.commit()


cur.execute("Select * from Word")
one_result = cur.fetchall()
print(one_result)
for t in one_result:
    print(t)

