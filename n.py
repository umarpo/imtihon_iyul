from telebot import TeleBot
from keyboards import *

token = "7205750098:AAHeSMbsfBzynLhVxXoEwPgBMqAb9MssTJs1q"
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    print("Bot ishlashni boshladi")
    chat_id = message.chat.id
    bot.send_message(chat_id, "Assalomu aleykum online_market botimizga xush kelibsiz. tilni tanlang", reply_markup=general_languange())

@bot.callback_query_handler(func=lambda call:True)
def select_languange(call):
    chat_id = call.message.chat.id

    if call.data == "uz":
        bot.send_message(chat_id, "Siz uzbek tilini tanladingiz. Endi menu ni tanlang", reply_markup=general_menu())
        bot.register_next_step_handler(call.message, main_manu)

    if call.data == "ru":
        bot.send_message(chat_id, "Siz rus tilini tanladingiz. Endi menu ni tanlang", reply_markup=general_menu())
        bot.register_next_step_handler(call.message, main_manu)

    if call.data == "en":
        bot.send_message(chat_id, "Siz ingiliz tilini tanladingiz. Endi menu ni tanlang", reply_markup=general_menu())
        bot.register_next_step_handler(call.message, main_manu)


def main_manu(message):
    chat_id = message.chat.id
    if message.text == "Computers":
        bot.send_message(chat_id, "Bu bo'lim hozircha ishlamayapdi")

    if message.text == "Television":
        bot.send_message(chat_id, "Bu bo'lim hozircha ishlamayapdi")

    if message.text == "Printers":
        bot.send_message(chat_id, "Bu bo'lim hozircha ishlamayapdi")

    if message.text == "orqaga":
        bot.send_message(chat_id, "orqaga qaytingiz",reply_markup=general_languange())
        bot.register_next_step_handler(message,select_languange)

bot.polling(non_stop=True)






