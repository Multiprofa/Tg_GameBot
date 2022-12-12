from aiogram import  types, Dispatcher
from create_bot import dp, bot


#@dp.message_handler(commands=['star', 'Rules', 'Character Menu'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Your adventure started!!', reply_markup=kb_client)

def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'rules', 'character_menu'])

# @dp.message_handler()
# async def echo_send(message: types.Message):
# await message.answer(message.text)
# await message.reply(message.text)
#await bot.send_message(message.from_user.id, message.text)

