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
        Insert INTO Words (RusWord, EngWord, IsRusToEng) VALUES 
        ('слово','word',1),
        ('пробел','space',1),
        ('кнопка','button',1),
        ('таблица','table',0),
        ('строка','string',0),
        ('запрос','request',0)
        ;
""")
conn.commit()


cur.execute("Select * from Words")
one_result = cur.fetchall()
print(one_result)
for t in one_result:
    print(t)

