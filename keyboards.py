from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Оставить заявку'), KeyboardButton(text='Личный кабинет')],
    [KeyboardButton(text='О нас'), KeyboardButton(text='Контакты')]
], resize_keyboard=True)


async def inline_main_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text='Категории товаров', callback_data='product_categories'),
        InlineKeyboardButton(text='Заявка', callback_data='application'),
        InlineKeyboardButton(text='Личный кабинет', callback_data='personal_account'),
        InlineKeyboardButton(text='Информация о компании', callback_data='information'),
        InlineKeyboardButton(text='Контакты', callback_data='contacts')
    )
    return keyboard.adjust(1).as_markup()

async def inline_catalog_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Категории товаров', callback_data='product_categories')]
    ])

categories = ['категория1', 'категория2', 'категория3', 'Другое']

async def inline_categories():
    keyboard = InlineKeyboardBuilder()
    for category in categories:
        keyboard.add(InlineKeyboardButton(text=category, callback_data=f"category_{category}"))
    return keyboard.adjust(2).as_markup()

async def inline_product_controls():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Добавить в корзину', callback_data='add_to_cart')],
        [InlineKeyboardButton(text='<- пред', callback_data='prev'),
         InlineKeyboardButton(text='1', callback_data='page'),
         InlineKeyboardButton(text='след ->', callback_data='next')],
        [InlineKeyboardButton(text='Вернуться', callback_data='back_to_categories')]
    ])

async def inline_application_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Заявка', callback_data='application')]
    ])

async def inline_applications():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Создать заявку', callback_data='create_application')],
        [InlineKeyboardButton(text='Мои заявки', callback_data='my_applications')]
    ])

async def inline_profile_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Личный кабинет', callback_data='personal_account')]
    ])

async def inline_profile_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Изменить данные', callback_data='edit_profile')],
        [InlineKeyboardButton(text='Пригласить друга', callback_data='invite_friend')],
        [InlineKeyboardButton(text='Корзина', callback_data='cart')]
    ])

async def inline_info_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Информация о компании', callback_data='information')]
    ])

async def inline_contacts_button():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Контакты', callback_data='contacts')]
    ])

