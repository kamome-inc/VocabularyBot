import sqlite3
import aiogram
import logging
from aiogram import Bot, Dispatcher, executor, types

dbname = 'firsttest.db'


bot = Bot(token="1171530088:AAEY9EXzFxBXZm4_Bymzm18hYpm8KZjnpx8")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


GlobalState = dict()

class User(object):

    def __init__(self, user: types.user):
        # id, first_name, last_name, username
        self.Id = user.id
        self.FirstName = user.first_name
        self.LastName = user.last_name
        self.UserName = user.username

    def check_user_in_db(user_id):
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        res = cur.execute(f"Select id from User WHERE User.id = {user_id}")
        res = res.fetchall()
        conn.close()
        if not res:
            return False
        else:
            return True

    def add_user_to_db(self):
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()
        res = cur.execute(f"""Insert INTO User Values({self.Id}, '{self.FirstName}', '{self.LastName}', 
                            '{self.UserName}')""")
        conn.commit()
        conn.close()


class Status(object):
    def __init__(self):
        pass


def forall_text_message(function):
    async def some(message: types.Message):
        logging.info(f"Получено сообщение от пользователя: {message.from_user.first_name}, {message.from_user.last_name}, id =  {message.from_user.id}")
        logging.info(f"Наличие пользователя в БД: {User.check_user_in_db(message.from_user.id)}")
        if not User.check_user_in_db(message.from_user.id):
            us = User(message.from_user)
            us.add_user_to_db()
        await function(message)
    return some


@dp.message_handler(commands="start")
@forall_text_message
async def cmd_start(message: types.Message):
    GlobalState.update({message.from_user.id:""})
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text="/add", callback_data="add")
    keyboard.add(button_1)
    button_2 = types.KeyboardButton(text="/list", callback_data="list")
    keyboard.add(button_2)
    await message.answer("""Добро пожаловать в словарь! Вам доступны следующие функции:  
    Добавить новое слово - команда /add
    Просмотреть все слова - команда /list""", reply_markup=keyboard)


@dp.message_handler(commands="add")
async def add_new_word(message: types.Message):
    await message.answer("Введите новое слово", reply_markup=types.ReplyKeyboardRemove())
    state = dict()
    GlobalState.update({message.from_user.id: "adding a new word"})
    print(GlobalState)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)