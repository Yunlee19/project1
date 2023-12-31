import telebot
from telebot import types
import random

bot = telebot.TeleBot("6763387587:AAFEalaOfANRIzJxbm2R5OCxKz6IF1DWEZU")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup.add(types.KeyboardButton('🗿'), types.KeyboardButton('✂️'), types.KeyboardButton('📄'))
    bot.reply_to(message, "Добро пожаловать в игру 'Камень, ножницы, бумага'! Для игры используйте кнопки ниже:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def play_game(message):
    user_choice = message.text
    bot_choice = random.choice(['🗿', '✂️', '📄'])

    if user_choice not in ['🗿', '✂️', '📄']:
        bot.reply_to(message, "Пожалуйста, используйте кнопки для выбора камня, ножниц или бумаги.")
        return

    if user_choice == bot_choice:
        bot.reply_to(message, f"Вы выбрали {user_choice}, а бот выбрал {bot_choice}. Ничья!")
    elif (user_choice == '🗿' and bot_choice == '✂️') or (user_choice == '✂️' and bot_choice == '📄') or (user_choice == '📄' and bot_choice == '🗿'):
        bot.reply_to(message, f"Вы выбрали {user_choice}, а бот выбрал {bot_choice}. Вы победили! 🎉")
    else:
        bot.reply_to(message, f"Вы выбрали {user_choice}, а бот выбрал {bot_choice}. Бот победил! ")

bot.polling()