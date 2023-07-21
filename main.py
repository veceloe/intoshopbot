import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота
bot = Bot(token="6321093616:AAE2nNml_vYU9NAstg66JDUUv1ZhicGM-bk")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создание клавиатуры с кнопками
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    # Добавление кнопок на клавиатуру
    buttons = ["Информация о стоимости доставки", "Как высчитать цену", "Как записаться", "Информация об учетах",
               "Как производится оплата", "Нынешний курс учётов", "Контакт с менеджером"]
    # Добавление кнопок на клавиатуру
    for button in buttons:
        keyboard.add(button)
    # Отправка сообщения с клавиатурой
    await message.answer("Выберите вопрос:", reply_markup=keyboard)


# Обработка нажатия кнопок
@dp.message_handler()
async def handle_button_click(message: types.Message):
    # Обработка нажатия кнопки "Информация о стоимости доставки"
    if message.text == "Информация о стоимости доставки":
        answer = "Есть доставка до корейского адреса, ее стоимость уже входит в пост с оплатой разбора. Также есть " \
                 "доставка из Кореи до РФ к админкам, в среднем стоимость за одну карту составляет 80-90 рублей/ за " \
                 "альбом 250-400 рублей. Информацию по поводу другого стаффа уточняйте у админок. После упаковки " \
                 "вашей заявки на доставку по РФ вам необходимо будет оплатить к вам (письмо - 100 рублей; небольшая " \
                 "бандероль - 110 рублей; большая бандероль - 170 рублей)"
        await message.answer(answer)
    # Обработка нажатия кнопки "Как высчитать цену"
    elif message.text == "Как высчитать цену":
        answer = (
            "Чтобы узнать цену карты, нужно умножить 95 на цифру после запятой (0.2 = 95×2=190 рублей).\n"
            "Если карта стоит 1.0 или больше, то умножаете всё число без запятой на 95 (1.3 = 13×95=1235).\n"
            "Если после запятой две цифры, то умножаете число сначала на 10, затем на 95 (0.15: 0.15×10 = 1.5, "
            "1.5×95 = 142,5).\n"
            "Все цены без учетов (˵ •‌ ᴗ - ˵ ) ✧"
        )
        await message.answer(answer)
    # Обработка нажатия кнопки "Как записаться"
    elif message.text == "Как записаться":
        answer = "Запись происходит в комментариях.\nВам необходимо отправить в комментарии фотографию желаемого " \
                 "стаффа, который представлен в разборе. (в некоторых случаях, например, в коллективках, нужно писать " \
                 "админкам)."
        await message.answer(answer)
    # Обработка нажатия кнопки "Информация об учетах"
    elif message.text == "Информация об учетах":
        answer = "Курс может как подниматься, так и понижаться.\nЕсли будут происходить изменения, эту информацию мы " \
                 "будем обновлять здесь на кнопке \"нынешний курс учетов\".\nЕсли в разборе участвует несколько " \
                 "человек, то учеты делятся между участниками разбора. Чем больше участников разбора - тем меньше " \
                 "учеты для каждого."
        await message.answer(answer)
    # Обработка нажатия кнопки "Как производится оплата"
    elif message.text == "Как производится оплата":
        answer = "Оплата производится переводом на реквизиты, которые указаны в посте с оплатой. Админы никогда не " \
                 "присылают реквизиты в личные сообщения, только в случае оплаты доставки по РФ. После оплаты вам " \
                 "необходимо отправить в комментарии чек с номером вашей позиции (в случае, если в разборе участвует " \
                 "несколько человек. если это индивидуальный выкуп, то номер позиции указывать не нужно)."
        await message.answer(answer)
    # Обработка нажатия кнопки "Нынешний курс учётов"
    elif message.text == "Нынешний курс учётов":
        answer = "на данный момент учёты доставки до корейского адреса составляют 225 рублей."
        await message.answer(answer)
    # Обработка нажатия кнопки "Контакт с менеджером"
    elif message.text == "Не нашли ответ на вопрос":
        answer = "Если вы не нашли ответ на свой вопрос, то свяжитесь с админками:\n @meijoooo ; @Omezjhka ; " \
                 "@beomgyullove"
        await message.answer(answer)


# Запуск бота
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
