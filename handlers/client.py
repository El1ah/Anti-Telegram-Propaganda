from aiogram import types, Dispatcher
from create_bot import dp, bot

async def start(message : types.Message):
    await bot.send_message(message.chat.id, '<b>Welcome!</b>', parse_mode='html')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(start, commands=['start', 'help'])