import telebot
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)
from confing import TOKEN1  # Убедитесь, что TOKEN1 содержит ваш токен бота
from bot_logic import gen_pass, flip_coin, random_meme

bot = telebot.TeleBot(TOKEN1)



generate_password_t_r = False

# *** Обработчики команд ***

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start."""
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    bot.reply_to(message, 'Советую написать /help')

@bot.message_handler(commands=['hello'])
def send_hello(message):
    """Обработчик команды /hello."""
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    """Обработчик команды /bye."""
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_command(message):
    """Обработчик команды /help."""
    bot.reply_to(message, 'Доступные команды: /start, /mem, /hello, /bye, /generate_password, /coin, /yesno, /miniapp, rick_rolls')  
bot.infinity_polling()
