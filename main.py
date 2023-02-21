import base64
import telebot
import datetime
import requests
import logging
import time
import os

logging.basicConfig(level='INFO', filename='telebot.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MyLog')
bot = telebot.TeleBot("5800314423:AAGrbowq4JXK5koSlUNXXd2q9Joc8sF8mvk")


@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Привет, <b>{message.from_user.first_name}</b>.' \
            f'\nВведите или нажмите /help для справки.'
    bot.send_message(message.chat.id, hello, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    mess = f' Для записи в столовую на <u>завтра</u> отправьте свои ФИО полностью как в паспорте.' \
           f'\nВводить данные нужно всегда после команды /help'
    answer = bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.register_next_step_handler(answer, review)


def review(message):
    now = datetime.datetime.now()
    today_9_10 = now.replace(hour=19, minute=10)
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    # в переменную ответ пользователя и разрезание по символу пробел на ФИО
    answer = message.text
    split = answer.split()
    try:
        save_mess1 = '&FirstName=' + split[0] + '&SecondName=' + split[1] + \
                     "&LastName=" + split[2] + '&Date=' + now.strftime('%Y%m%d')
        save_mess2 = 'Запись на сегодня закончена! Записаться можно до 9:10.\n' \
        url = 'http://sqlsrv/multi/hs/Canteen/AddList?id=123' + save_mess1
        ans = requests.get(url)
        to_user = ans.json()
        if now < today_9_10:

            talon = to_user['File']
            talon_send = str(message.chat.id)+ '-' + now.strftime('%d-%m-%Y-%H-%M') + '.pdf'
            with open(talon_send, 'wb') as f:
                f.write(base64.b64decode(talon))
            file = open(talon_send, 'rb')
            bot.send_message(message.chat.id, to_user['Answer'] + ' на ' + now.strftime('%d-%m-%Y'), parse_mode='html')
            bot.send_document(message.chat.id, file)
            file.close()
            os.remove(talon_send)
        else:
            bot.send_message(message.chat.id, save_mess2, parse_mode='html')
            print(message.text, 'не успел', now.strftime(' %H:%M'))
    except IndexError:
        bot.send_message(message.chat.id, 'Введите данные как в паспорте после /help', parse_mode='html')


def telega_polling():
    try:
        bot.polling(none_stop=True)
    except:
        bot.stop_polling()
        time.sleep(60)
        telega_polling()


telega_polling()
