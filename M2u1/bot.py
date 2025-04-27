import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from confing import TOKEN1 
from bot_logic import gen_pass, flip_coin, random_meme

bot = telebot.TeleBot(TOKEN1)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start."""
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.reply_to(message, " Я твой Telegram бот. Напиши что-нибудь!")
    bot.reply_to(message, 'Советую написать /help')

@bot.message_handler(commands=['hello'])
def send_hello(message):
    """Обработчик команды /hello."""
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    """Обработчик команды /bye."""
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    with open(random_meme(), 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['help'])
def send_command(message):
    """Обработчик команды /help."""
    bot.reply_to(message, 'Доступные команды: /start, /mem, /hello, /bye, ')
@bot.message_handler(func=lambda message: True)
def echo_all(message):

        bot.reply_to(message, 'я не понимаю')

bot.infinity_polling()
