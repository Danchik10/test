from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в наш магазин мебели! Здесь вы можете выбрать товары, оставить заявку на заказ и многое другое. "
        "Нажмите на кнопки ниже или введите /help для команд.",
        reply_markup=kb.main
    )


@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Посмотреть все доступные команды\n"
        "/catalog - Перейти в каталог товаров\n"
        "/order - Оставить заявку\n"
        "/info - Информация о компании\n"
        "/contacts - Контакты компании\n"
        "/profile - Главное меню"
    )


@router.message(Command("catalog"))
@router.message(lambda message: message.text == "Каталог")
async def show_catalog_menu(message: Message):
    keyboard = await kb.inline_catalog_button()
    await message.answer("Выберите опцию:", reply_markup=keyboard)

@router.callback_query(F.data == 'product_categories')
async def show_categories(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Категории товаров")
    keyboard = await kb.inline_categories()
    await callback.message.edit_text(
        "Советуем вам ознакомиться с категорией 'другое'. Там вы сможете найти уникальные товары и товары, категории которых нет в списке:",
        reply_markup=keyboard
    )

@router.callback_query(F.data.startswith('category_'))
async def show_products(callback: CallbackQuery):
    category = callback.data.split('_')[1]
    await callback.answer(f"Вы выбрали категорию: {category}")
    keyboard = await kb.inline_product_controls()
    await callback.message.edit_text("Тут будут примеры работ для выбранной категории", reply_markup=keyboard)


@router.message(Command("order"))
@router.message(lambda message: message.text == "Оставить заявку")
async def show_order_menu(message: Message):
    keyboard = await kb.inline_application_button()
    await message.answer("Нажмите кнопку ниже для подачи заявки", reply_markup=keyboard)

@router.callback_query(F.data == 'application')
async def application_menu(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Заявка")
    keyboard = await kb.inline_applications()
    await callback.message.edit_text(
        "Здесь вы можете напрямую подать заявку мастеру на изготовление со своими пожеланиями",
        reply_markup=keyboard
    )


@router.message(lambda message: message.text == "Личный кабинет")
async def show_profile_menu(message: Message):
    keyboard = await kb.inline_profile_button()
    await message.answer("Ваш личный кабинет", reply_markup=keyboard)

@router.callback_query(F.data == 'personal_account')
async def profile(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Личный кабинет")
    keyboard = await kb.inline_profile_menu()
    await callback.message.edit_text("Профиль\nИмя: \nТелефон: \nБонусы", reply_markup=keyboard)


@router.message(Command("info"))
@router.message(lambda message: message.text == "О нас")
async def info(message: Message):
    keyboard = await kb.inline_info_button()
    await message.answer("Информация о компании:", reply_markup=keyboard)

@router.callback_query(F.data == 'information')
async def info_callback(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Информация о компании")
    await callback.message.edit_text("(Здесь будет информация о компании)")


@router.message(Command("contacts"))
@router.message(lambda message: message.text == "Контакты")
async def contacts(message: Message):
    keyboard = await kb.inline_contacts_button()
    await message.answer("Контакты:", reply_markup=keyboard)

@router.callback_query(F.data == 'contacts')
async def contacts_callback(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Контакты")
    await callback.message.edit_text("(Здесь будут контакты компании)")


@router.message(Command("profile"))
async def full_profile(message: Message):
    keyboard = await kb.inline_main_menu()
    await message.answer("Навигация:", reply_markup=keyboard)

@router.callback_query(F.data == 'profile_catalog')
async def cb_profile_catalog(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Категории товаров")
    await show_catalog_menu(callback.message)

@router.callback_query(F.data == 'profile_application')
async def cb_profile_application(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Заявка")
    await show_order_menu(callback.message)

@router.callback_query(F.data == 'profile_personal')
async def cb_profile_personal(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Личный кабинет")
    await show_profile_menu(callback.message)

@router.callback_query(F.data == 'profile_info')
async def cb_profile_info(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Информация о компании")
    await info(callback.message)

@router.callback_query(F.data == 'profile_contacts')
async def cb_profile_contacts(callback: CallbackQuery):
    await callback.answer("Вы выбрали: Контакты")
    await contacts(callback.message)
