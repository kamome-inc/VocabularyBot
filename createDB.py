import sqlite3
conn = sqlite3.connect('firsttest.db')
cur = conn.cursor()

cur.execute("""
            Create Table Words (
            id integer primary key AUTOINCREMENT,
            RusWord text,
            EngWord text,
            Comment text,
            IsRusToEng bool);
""")

cur.execute("""
        Insert INTO Words (RusWord, EngWord, Comment, IsRusToEng) VALUES 
        ('слово1','word1',"",1),
        ('слово2','word2',"",1),
        ('слово3','word3',"",1),
        ('слово4','word4',"",1),
        ('слово5','word5',"",1)
        
        ;
""")
conn.commit()


cur.execute("Select * from Words")
one_result = cur.fetchall()
print(one_result)
for t in one_result:
    print(t)

