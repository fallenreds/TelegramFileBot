import telebot

from chunk import *
from telebot import types


token = '5543008601:AAGIRHOKP4BNJwPgGMLFziKdGbtqWBsgQEo'

bot = telebot.TeleBot(token)
#
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     mess = f'Привет,{message.from_user.first_name}'
# #     bot.send_message(message.chat.id, mess, parse_mode='html')
# #
# # @bot.message_handler()
# # def get_user_text(message):
# #     if message.text =='Hello':
# #         bot.send_message(message.chat.id, "Ты ввел хеллоу")
#
# @bot.message_handler()
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('hello', url='t.me/fallenreds'))
#     bot.send_message(message.chat.id, 'NONE', reply_markup=markup)
#
# bot.polling(none_stop=True)


@bot.message_handler(content_types=['document'])
def slice(message):
    bot.send_message(message.chat.id, message.document)
    file_info = bot.get_file(message.document.file_id)
    file = bot.download_file(file_info.file_path)
    split_file_data = split_f(message, file, bot)



bot.polling(none_stop=True)