import telebot
import bot_info
from chunk import *


token = bot_info.bot_token
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['document'])
def slicer(message):
    bot.send_message(message.chat.id, message.document)
    file_info = bot.get_file(message.document.file_id)
    file = bot.download_file(file_info.file_path)
    split_file_data = split_f(message, file, bot)
    merge_f(message, split_file_data, bot)


bot.polling(none_stop=True)