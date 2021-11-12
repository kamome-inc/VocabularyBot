import sqlite3
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types

DataBaseName = 'firsttest.db'



bot = Bot(token="1171530088:AAEY9EXzFxBXZm4_Bymzm18hYpm8KZjnpx8")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


class Word(object):
    """ """

    def __init__(self, *args):
        """2 or 4 or 5 args"""
        if len(args) == 4:
            self.RusWord = args[0]
            self.EngWord = args[1]
            self.Comment = args[2]
            self.IsRusToEng = args[3]
        elif len(args) == 5:
            self.RusWord = args[0]
            self.EngWord = args[1]
            self.Comment = args[2]
            self.IsRusToEng = args[3]
            self.Id = args[4]
        elif len(args) == 1:
            """Creating a new word from string. without comments"""
            delimiter = ' - '
            self.RusWord = args[0].split(delimiter)[0]
            self.EngWord = args[0].split(delimiter)[1]
            self.Comment = ""
            self.IsRusToEng = 1
        else:
            raise Exception("Неверное количество аргументов для конструктора, получено - " + str(len(args)))

    def get_word(self):
        return self.RusWord + ' - ' + self.EngWord + " " + str(self.Comment) + " " + str(self.IsRusToEng)

    def get_sql_string(self):
        return "('" + self.RusWord + "', '" + self.EngWord + "', '" + self.Comment + "', " + str(self.IsRusToEng) + ")"


def add_words_to_db(words_array):
    conn = sqlite3.connect(DataBaseName)
    cur = conn.cursor()
    request = 'Insert Into Words (RusWord, EngWord, Comment, IsRusToEng) VALUES '
    if len(words_array) > 1:
        for word in words_array[:-1]:
            request = request + word.get_sql_string() + ', '
        request = request + words_array[-1].get_sql_string() + ';'
    elif len(words_array) == 1:
        request += words_array[0].get_sql_string() + ';'
    else:
        raise Exception("Дерьмо с количеством элементов в аргументе")
    cur.execute(request)
    conn.commit()
    conn.close()


def get_words_from_db():
    conn = sqlite3.connect(DataBaseName)
    cur = conn.cursor()
    request = 'Select RusWord, EngWord, Comment, IsRusToEng, Id FROM Words'
    cur.execute(request)
    results = cur.fetchall()
    out = []
    for word in results:
        arg = list(word)
        out.append(Word(arg[0], arg[1], arg[2], arg[3], arg[4]))
    conn.close()
    return out


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="/Добавить слово")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="/Просмотреть слова")
    keyboard.add(button_2)
    await message.answer('Добро пожаловать в словарь! Вам доступны следующие функции:', reply_markup=keyboard)

#bot.send_message(1146840023, " hello world! ")




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)