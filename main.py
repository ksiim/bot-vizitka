from bot import dp
from aiogram import executor
from handlers_register import handlers_reg
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    handlers_reg(dp)
    executor.start_polling(dp)
