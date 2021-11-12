import logging
from aiogram import Bot, Dispatcher, executor, types



bot = Bot(token="1171530088:AAEY9EXzFxBXZm4_Bymzm18hYpm8KZjnpx8")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    await message.answer('123', reply_markup=keyboard)

#bot.send_message(1146840023, " hello world! ")




if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)