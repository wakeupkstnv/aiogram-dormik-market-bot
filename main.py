import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton

# Замените 'YOUR_API_TOKEN' на токен вашего бота
API_TOKEN = ''

# Инициализируем бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Создадим словарь для товаров, которые будут в будущем
future_products = {
    "Кофе 3 в 1": {"price": "Неизвестна"},
    "Хлеб": {"price": 300},
    "Милка с орео))" : {'price': 1500},
    "Red-Bull": {'price': 800},
    "Tuc": {"price": 450},
    "Big-Bon": {'price': 300},
    "Булочка с маком": {'price': 240},
    # Добавьте другие товары, которые будут скоро, и их цены
}

# Создадим список товаров, которые уже есть в наличии
available_products = [
    #{"name": "Big-Bon", "phone": "87779742598", "price": 300, 'value': 1},
    {"name": "Pepsi 1л", "phone": "87779742598", "price": 550, 'value': 1},
    {"name": "Oreo 1 пачка", "phone": "87779742598", "price": 150, 'value': 6},
    {"name": "Alpen gold", "phone": "87779742598", "price": 350, 'value': 4},
    {"Milka "}
    #{"name": "Tuc", "phone": "87779742598", "price": 450, 'value': 1},
    #{"name": "Булочка с маком", "phone": "87779742598", "price": 240, 'value': 2},
    #{"name": "Хлеб", "phone": "87779742598", "price": 300, 'value': 0},
]

# Создаем клавиатуру с кнопками для товаров и кнопкой "Товары, которые будут скоро"
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=False)
for product in available_products:
    keyboard.add(KeyboardButton(product['name']))
keyboard.add(KeyboardButton("Товары, которые будут скоро"))

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    """
    Отправка приветственного сообщения и клавиатуры с кнопками для товаров
    """
    await message.answer("Привет! Выберите товар из списка ниже или нажмите 'Товары, которые будут скоро':\n\n p.s Доставляем товар сами, при заказе пишите номера корпуса, этажа и комнаты", reply_markup=keyboard)

# Обработчик нажатия на кнопку товара
@dp.message_handler(lambda message: message.text in [product['name'] for product in available_products])
async def process_product(message: types.Message):
    selected_product = next(product for product in available_products if product['name'] == message.text)
    await message.answer(f"Для заказа просто скопируйте этот текст и отправьте через личку Telegram: \n\n"
                         f"Вы выбрали товар: {selected_product['name']}\n"
                         f"Цена: {selected_product['price']}\n"
                         f"Кол-во: {selected_product['value']}\n\n"
                         f"Мой тг: @wakeupkstnv\n\n"
                         f"Чтобы обновить список товаров: /start")

# Обработчик нажатия на кнопку "Товары, которые будут скоро"
@dp.message_handler(lambda message: message.text == "Товары, которые будут скоро")
async def show_soon_products(message: types.Message):
    response = "Скоро появятся следующие товары:\n\n"
    for product_name, product_info in future_products.items():
        response += f"{product_name}:\nЦена: {product_info['price']} тг\n\n"
    await message.answer(response)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)`