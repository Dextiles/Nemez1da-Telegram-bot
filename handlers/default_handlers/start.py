from telebot.types import Message
from keyboards.inline import show_instruction as btn
from loader import bot
import logging


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.first_name}!\n\n"
                          f"Это бот для проверки лиц по базе данных, "
                          f"полученной в результате анализа сайта nemez1da.ru\n\n"
                          f"Бот использует механизм парсинга 'На лету' (подробнее в инструкции)\n"
                          f"Это обеспечивает актуальность предоставляемых данных\n\n"
                          f"Перед началом работы рекомендую изучить <b>инструкцию</b>\n",
                 reply_markup=btn.get_show_instruction_button(),
                 parse_mode='HTML')
    logging.info(f'id{message.from_user.id} начал работу с ботом')

