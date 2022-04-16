import telebot
import os

API_KEY = os.getenv('TOKEN')

bot = telebot.TeleBot(API_KEY, parse_mode=None)

@bot.message_handler(commands=["help", "Hello"])
def send_help_message(msg):
    bot.reply_to(msg, "Hello! This is a test bot")

@bot.message_handler(func=lambda msg: msg.from_user)
def send_help_message(msg):
    print(msg.from_user)
    bot.send_message(msg.chat.id, "Hello")

@bot.message_handler(func=lambda msg: msg.from_user)
def send_help_message(msg):
    bot.send_message(msg.chat.id, "Am good and you?")

@bot.message_handler(func=lambda msg: msg.from_user)
def send_help_message(msg):
    if msg == "am fine" or "am good" or "am great":
        bot.send_message(msg.chat.id, "Am good and you?")
    else:
        bot.send_message(msg.chat.id, "Whats wrong?😢")

bot.polling()