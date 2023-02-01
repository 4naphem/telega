import telebot, datetime, requests
bot = telebot.TeleBot("5800314423:AAFytkDuFON5M5eBENHaC0Iqg7DDQz1op0I")
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Привет, <b>{message.from_user.first_name}</b>.'\
            f'\nВведите или нажмите /help для справки.'
    bot.send_message(message.chat.id, hello, parse_mode='html')
@bot.message_handler(commands=['help'])
def start(message):
    mess = f' Для записи в столовую на <u>завтра</u> введите свою фамилию следующим сообщением.'\
    f'\nЭту операцию необходимо проделывать каждый раз для записи (/help->Фамилия).'
    answer = bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.register_next_step_handler(answer, review)
def review(message):
    save_mess ='&user='+ message.text +'&date='+ tomorrow.strftime('%d-%m-%Y')
    url='http://sqlsrv/multi/hs/Canteen/UsersList/?id=123&pp=123'+save_mess
    send_post = requests.get(url)
    print(send_post)

bot.polling(none_stop=True)
