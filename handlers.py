from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboard as kb

router = Router()

@router.message(Command('catalog'))
async def start(message: Message):
    await message.reply('Выберите опцию',
                        reply_markup= kb.main)


@router.message(Command('help'))
async def get_help(message : Message):
    await message.answer('Это команда /help')

@router.message(lambda message: message.text == "Каталог")
async def catalog(message: Message):
    keyboard = await kb.inline_catalogs()
    await message.answer("Советуем вам ознакомиться с категорией 'другое'. Там вы сможете найти уникальные"
                         " товары и товары, категории которых нет в списке:",
                         reply_markup=keyboard)


@router.callback_query(F.data == 'catalog')
async def catalog(callback : CallbackQuery):
    await callback.answer('Вы выбрали каталог',show_alert=True)
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_catalogs())