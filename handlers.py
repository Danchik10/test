from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    keyboard = await kb.inline_main_menu()
    await message.answer("Приветствуем вас в нашем магазине мебели! Ниже вы найдете основные разделы для работы с ботом:", reply_markup=keyboard)


@router.message(Command("help"))
async def help_handler(message: Message):
    help_text = (
        "📋 Доступные команды:\n"
        "/start — Начать работу с ботом\n"
        "/catalog — Перейти к каталогу товаров\n"
        "/order — Оставить заявку мастеру\n"
        "/info — Информация о компании\n"
        "/contacts — Контактные данные\n"
        "/profile — Главное меню навигации"
    )
    await message.answer(help_text)


@router.message(Command("catalog"))
@router.message(lambda message: message.text == "Каталог")
async def show_catalog_menu(message: Message):
    keyboard = await kb.inline_catalog_button()
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@router.callback_query(F.data == 'product_categories')
async def show_categories(callback: CallbackQuery):
    await callback.answer()
    keyboard = await kb.inline_categories()
    await callback.message.edit_text(
        "Советуем вам ознакомиться с категорией 'другое'. Там вы сможете найти уникальные товары и товары, категории которых нет в списке:",
        reply_markup=keyboard)

@router.callback_query(F.data.startswith('category_'))
async def show_products(callback: CallbackQuery):
    await callback.answer()
    keyboard = await kb.inline_product_controls()
    await callback.message.edit_text("Тут будут примеры работ для выбранной категории", reply_markup=keyboard)


@router.message(Command("order"))
@router.message(lambda message: message.text == "Оставить заявку")
async def show_order_menu(message: Message):
    keyboard = await kb.inline_application_button()
    await message.answer("Нажмите кнопку ниже для подачи заявки", reply_markup=keyboard)

@router.callback_query(F.data == 'application')
async def application_menu(callback: CallbackQuery):
    await callback.answer()
    keyboard = await kb.inline_applications()
    await callback.message.edit_text(
        "Здесь вы можете напрямую подать заявку мастеру на изготовление со своими пожеланиями",
        reply_markup=keyboard)


@router.message(lambda message: message.text == "Личный кабинет")
async def show_profile_menu(message: Message):
    keyboard = await kb.inline_profile_button()
    await message.answer("Ваш личный кабинет", reply_markup=keyboard)

@router.callback_query(F.data == 'personal_account')
async def profile(callback: CallbackQuery):
    await callback.answer()
    keyboard = await kb.inline_profile_menu()
    await callback.message.edit_text("Профиль\nИмя: \nТелефон: \nБонусы", reply_markup=keyboard)


@router.message(Command("info"))
@router.message(lambda message: message.text == "О нас")
async def info(message: Message):
    keyboard = await kb.inline_info_button()
    await message.answer("Информация о компании:", reply_markup=keyboard)

@router.callback_query(F.data == 'information')
async def info_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("")


@router.message(Command("contacts"))
@router.message(lambda message: message.text == "Контакты")
async def contacts(message: Message):
    keyboard = await kb.inline_contacts_button()
    await message.answer("Контакты:", reply_markup=keyboard)

@router.callback_query(F.data == 'contacts')
async def contacts_callback(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("")


@router.message(Command("profile"))
async def full_profile(message: Message):
    keyboard = await kb.inline_main_menu()
    await message.answer("Навигация:", reply_markup=keyboard)
