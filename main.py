import telebot, datetime, requests, logging, time

logging.basicConfig(level='INFO', filename='telebot.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MyLog')
bot = telebot.TeleBot("5800314423:AAGrbowq4JXK5koSlUNXXd2q9Joc8sF8mvk")
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
now = datetime.datetime.now()
today_9_10 = now.replace(hour=9, minute=10)


@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Привет, <b>{message.from_user.first_name}</b>.' \
            f'\nВведите или нажмите /help для справки.'
    bot.send_message(message.chat.id, hello, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    mess = f' Для записи в столовую на <u>завтра</u> отправьте свою фамилию следующим сообщением.' \
           f'\nЭту операцию необходимо проделывать каждый раз для записи: \n(/help->Фамилия).'
    answer = bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.register_next_step_handler(answer, review)


def review(message):
    save_mess_today = '&user=' + message.text + '&date=' + now.strftime('%d-%m-%Y')
    save_mess_tomorrow = '&user=' + message.text + '&date=' + tomorrow.strftime('%d-%m-%Y')
    if now < today_9_10:
        url = 'http://sqlsrv/multi/hs/Canteen/UsersList/?id=123&pp=123' + save_mess_today
        send_post = requests.get(url)

    else:
        url = 'http://sqlsrv/multi/hs/Canteen/UsersList/?id=123&pp=123' + save_mess_tomorrow
        send_post = requests.get(url)
    print(send_post)


def telega_polling():
    try:
        bot.polling(none_stop=True)
    except:
        bot.stop_polling()
        time.sleep(60)
        telega_polling()


telega_polling()
