from config import TOKEN_API
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot, storage)


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1=KeyboardButton('помощь')
b2=KeyboardButton('добавить_ссылку')
b3=KeyboardButton('удалить ссылку')
kb.add(b1).add(b2).add(b3)

HELP_COMMAND = """
/start - начать работу с ботом
/help - список команд
/add_link - добавить ссылку М.Видео для мониторинга цены
/delete - удалить ссылку
❗️напоминаю наш бот работает только с сыллками М.Видео❗️
"""

@dp.message_handler(Text(equals='помощь'))
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           parse_mode="HTML",
                           )
    await message.delete()
    
    
@dp.message_handler(Text(equals='добавить_ссылку'))
async def add_link(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Введите сслыку товара М.Видео",
                           # вот сюды бы ебануть запрос данных
                           parse_mode="HTML",
                           )
    await message.delete()
    
@dp.message_handler(Text(equals='удалить ссылку'))
async def delete_link(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Удалить ненужный товар",
                           parse_mode="HTML",
                           )
    await message.delete()
    
@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
        text="Добро пожаловать в наш Телеграмм бот! ",
        parse_mode="HTML",
        reply_markup=kb)
    await message.delete()
    

if __name__ == '__main__':
    
    executor.start_polling(dp, skip_updates=True)
    
