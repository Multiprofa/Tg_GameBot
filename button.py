from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b_main = KeyboardButton('/Start')
b1 = KeyboardButton('/Start Adventure')
b2 = KeyboardButton('/Rules')
b3 = KeyboardButton('/Character Menu')

kb_client = ReplyKeyboardMarkup()

kb_client.add(b_main)