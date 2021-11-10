import re
import sqlite3


DataBaseName = 'firsttest.db'


class Words(object):
    """ """
    def __init__(self, inputstring):
        """Creating a new word from string. without comments"""
        delimiter = ' - '
        if bool(re.search('[а-яА-Я]', inputstring.split(delimiter)[0])):
            self.RusWord = inputstring.split(delimiter)[0]
            self.EngWord = inputstring.split(delimiter)[1]
        else:
            self.RusWord = inputstring.split(delimiter)[1]
            self.EngWord = inputstring.split(delimiter)[0]

        conn = sqlite3.connect(DataBaseName)
        cur = conn.cursor()
        cur.execute(f'Insert Into Words (RusWord, EngWord) VALUES ({self.RusWord}, {self.EngWord});')
        conn.commit()
        conn.close()

    def getallwords(self):
        conn = sqlite3.connect(DataBaseName)
        cur = conn.cursor()
        cur.execute('SELECT RusWord, EngWord FROM Words')
        results = cur.fetchall()
        conn.commit()
        conn.close()
        return results


word = Words()
print(word.getallwords())