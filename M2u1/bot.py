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
import requests

bot = telebot.TeleBot(TOKEN1)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Обработчик команды /start."""
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.reply_to(message, "Я твой Telegram бот. Напиши что-нибудь!")
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
    bot.reply_to(message, 'Доступные команды: /start, /mem, /hello, /bye, /duck')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Я не понимаю')

bot.infinity_polling()

