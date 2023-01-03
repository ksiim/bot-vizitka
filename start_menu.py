from aiogram import types
from bot import bot
from aiogram.types import InputFile


# клавиатура для возврата в меню
return_keyboard = types.InlineKeyboardMarkup(row_width=1)
return_buttons = [types.InlineKeyboardButton(text='Отзывы', callback_data='reviews'),
                  types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu')]
return_keyboard.add(*return_buttons)

# стартовое меню
async def start_menu(msg: types.Message):
    start_buttons = [types.InlineKeyboardButton(text='Курс психосоматики', url='https://mnogomernoe-myshlenie.ru/psychosomatics'),
                     types.InlineKeyboardButton(text='Консультация', url='tg://resolve?domain=Nadira88'),
                     types.InlineKeyboardButton(text='Подписаться на мой канал', url='https://t.me/doctor_mardanova'),
                     types.InlineKeyboardButton(text='Обо мне', callback_data='about'),
                     types.InlineKeyboardButton(text='Мой instagram', url='https://www.instagram.com/doctor_mardanova/')]
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    start_keyboard.add(*start_buttons)
    start_photo = InputFile('photos\\start_menu_photo.jpg')
    await bot.send_photo(chat_id=msg.from_user.id,
                         photo=start_photo,
                         reply_markup=start_keyboard)

# текст после нажатия на кнопку "Обо мне"
async def about(call: types.CallbackQuery):
    await call.message.answer(text='Доктор интегративной медицины.\n'
                                   'Врач онколог. Остеопат.\n'
                                   'Иглорефлексотерапевт, фитотерапевт.\n'
                                   'Со-основатель, руководитель\n'
                                   'Школы Многомерного Мышления.\n'
                                   'Тренер по трансформации сознания.',
                              reply_markup=return_keyboard)

# меню, в которое мы приходим после нажатия кнопки
async def menu(call: types.CallbackQuery):
    start_buttons = [
        types.InlineKeyboardButton(text='Курс психосоматики', url='https://mnogomernoe-myshlenie.ru/psychosomatics'),
        types.InlineKeyboardButton(text='Консультация', url='tg://resolve?domain=Nadira88'),
        types.InlineKeyboardButton(text='Подписаться на мой канал', url='https://t.me/doctor_mardanova'),
        types.InlineKeyboardButton(text='Обо мне', callback_data='about'),
        types.InlineKeyboardButton(text='Мой instagram', url='https://www.instagram.com/doctor_mardanova/')]
    start_keyboard = types.InlineKeyboardMarkup(row_width=1)
    start_keyboard.add(*start_buttons)
    start_photo = InputFile('photos\\start_menu_photo.jpg')
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=start_photo,
                         reply_markup=start_keyboard)

async def reviews(call: types.CallbackQuery):
    reviews_kb = types.InlineKeyboardMarkup(row_width=3)
    links_row = [x for x in open('reviews.txt')]
    links_buttons = []
    for i in range(1, len(links_row)+1):
        if '\n' in links_row[i-1]:
            link = links_row[i-1][:-1]
            links_buttons.append(types.InlineKeyboardButton(text=f'Отзыв №{i}', url=f'{link}'))
        else:
            links_buttons.append(types.InlineKeyboardButton(text=f'Отзыв №{i}', url=f'{links_row[i-1]}'))
    links_buttons.append(types.InlineKeyboardButton(text='Вернуться в меню', callback_data='menu'))
    reviews_kb.add(*links_buttons)
    await call.message.answer(text='Ниже приложены видеоотзывы\n👇👇👇', reply_markup=reviews_kb)
