from config import BOT_TOKEN
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp: Dispatcher = Dispatcher(bot, storage=storage)
