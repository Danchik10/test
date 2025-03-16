from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,
                           InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='оставить заявку'), KeyboardButton(text='Личный кабинет')],
    [KeyboardButton(text='о нас'), KeyboardButton(text='Контакты')]
],
                                resize_keyboard=True,
                                input_field_placeholder='')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = 'Категории товаров', callback_data='product categories')],
    [InlineKeyboardButton(text = 'Заявка', callback_data='application'),
     InlineKeyboardButton(text = 'Личный кабинет', callback_data='personal account')],
    [InlineKeyboardButton(text = 'Информация о компании', callback_data='information'),
     InlineKeyboardButton(text = 'Контакты', callback_data='contacts')]
])

categories = ['категория1', 'категория2', 'категория3', 'Другое']

async def inline_catalogs():
    keyboard = InlineKeyboardBuilder()
    for category in categories:
        keyboard.add(
            InlineKeyboardButton(
                text=category,
                callback_data=f"category_{category}"
            )
        )
    return keyboard.adjust(2).as_markup()
