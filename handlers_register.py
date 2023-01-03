from aiogram import Dispatcher
from start_menu import *

def handlers_reg(dp: Dispatcher):
    dp.register_message_handler(start_menu, commands=['start'])
    dp.register_callback_query_handler(about, text=['about'])
    dp.register_callback_query_handler(menu, text=['menu'])
    dp.register_callback_query_handler(reviews, text=['reviews'])
