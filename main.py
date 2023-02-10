import telebot, datetime, requests, logging, time

logging.basicConfig(level='INFO', filename='telebot.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('MyLog')
bot = telebot.TeleBot("5800314423:AAGrbowq4JXK5koSlUNXXd2q9Joc8sF8mvk")
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
now = datetime.datetime.now()
today_9_10 = now.replace(hour=20, minute=10)


@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Привет, <b>{message.from_user.first_name}</b>.' \
            f'\nВведите или нажмите /help для справки.'
    bot.send_message(message.chat.id, hello, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    mess = f' Для записи в столовую на <u>завтра</u> отправьте свои ФИО полностью как в паспорте.' \
           f'\nЭту операцию необходимо проделывать каждый раз для записи: \n(/help->Фамилия).'
    answer = bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.register_next_step_handler(answer, review)


def review(message):
    answer = message.text
    split = answer.split()
    save_mess1 = '&FirstName=' + split[0] + '&SecondName=' + split[1] + "&LastName=" + split[2] + '&Date=' + now.strftime('%Y%m%d')
    save_mess2 = 'Запись на сегодня закончена! Записаться можно до 9:10.'
    if now < today_9_10:
        url = 'http://sqlsrv/multi/hs/Canteen/AddList?id=123' + save_mess1
        ans = requests.get(url)
        print(ans.json(), ans)

    else:
        bot.send_message(message.chat.id, save_mess2 , parse_mode='html')
        requests.get(url)
        print('Нарушено расписание:', save_mess1, now.strftime('%H:%M'))



def telega_polling():
    try:
        bot.polling(none_stop=True)
    except:
        bot.stop_polling()
        time.sleep(60)
        telega_polling()


telega_polling()
