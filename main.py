import telebot
from telebot import types
bot = telebot.TeleBot("5800314423:AAFytkDuFON5M5eBENHaC0Iqg7DDQz1op0I")
# отслеживание команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # отправка привет пользователю + Имя
    mess = f'Привет, <b>{message.from_user.first_name}</b>.' \
           f' Для записи на обед нажмите на <b>/add</b> или введите команду самостоятельно'
    # отправка в тот же чат по id
    bot.send_message(message.chat.id, mess, parse_mode='html')
# отслеживание /help
@bot.message_handler(commands=['add'])
def add_lunch(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1, one_time_keyboard=True)
    add_one = types.KeyboardButton('На завтра')
    add_five = types.KeyboardButton('На неделю')
    markup.add(add_one, add_five)
    bot.send_message(message.chat.id, 'Получить талон:', reply_markup=markup)

bot.polling(none_stop=True)
2