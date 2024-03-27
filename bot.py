import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

info = []
@bot.message_handler(commands=['start'])


def welcome(message):
    menu = types.InlineKeyboardMarkup(row_width=3)
    b1 = types.InlineKeyboardButton("ФИО",callback_data="full_name")
    b2 = types.InlineKeyboardButton("Возраст",callback_data="age")
    b3 = types.InlineKeyboardButton("телефон\имаэл",callback_data="mail")
    menu.add(b1,b2,b3)
    bot.send_message(message.chat.id,f"<b>Доборо пожаловать {message.from_user.username} </b>",parse_mode="html",reply_markup=menu)


@bot.callback_query_handler(func=lambda call:True)
def call_back(call):
    if call.data == "full_name":
        bot.send_message(call.message.chat.id,"<b>Введите ФИО(полностью)   :</b>",parse_mode='html')
    elif call.data == "age":
        bot.send_message(call.message.chat.id,"<b>ваш возраст?</b>",parse_mode='html')
    elif call.data == "mail":
        bot.send_message(call.message.chat.id,"<b>Введите телефон либо mail   :</b>",parse_mode='html')

@bot.message_handler(func=lambda message:True)

def input_info(message):
    if message.text is not None:
        info.append(message.text)
        bot.send_message(message.chat.id,"данные сохранены")
    save()
def save():
    if len(info)>=3:
        with open("customer.txt","a") as f:
            f.write(f"фио {info[0]}\n")
            f.write(f"возраст {info[1]}\n")
            f.write(f"почта\телефон {info[2]}\n")
    else:
        print("не полных данных")




bot.polling(non_stop=True)
