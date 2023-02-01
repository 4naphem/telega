import telebot, datetime, requests
from telebot import types
bot = telebot.TeleBot("5800314423:AAFytkDuFON5M5eBENHaC0Iqg7DDQz1op0I")
# отслеживание команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # отправка привет пользователю + Имя
    mess = f'Привет, <b>{message.from_user.first_name}</b>.' \
           f'Для записи в столовую на <u>завтра</u> введите свою фамилию, как в паспорте'
    # отправка в тот же чат по id
    answer = bot.send_message(message.chat.id, mess, parse_mode='html');
    # ловим ответ пользователя
    bot.register_next_step_handler(answer, review)
def review(message):
    save_mess = message.text
    print(save_mess)

bot.polling(none_stop=True)
