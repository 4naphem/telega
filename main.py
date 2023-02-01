import telebot, datetime, requests
from telebot import types
bot = telebot.TeleBot("5800314423:AAFytkDuFON5M5eBENHaC0Iqg7DDQz1op0I")
# отслеживание команды /start
@bot.message_handler(commands=['start'])
def start(message):
    hello = f'Привет, <b>{message.from_user.first_name}</b>.'\
            f'\nВведите или нажмите /help для справки.'
    bot.send_message(message.chat.id, hello, parse_mode='html')
@bot.message_handler(commands=['help'])
def start(message):
    # отправка привет пользователю + Имя
    mess = f' Для записи в столовую на <u>завтра</u> введите свою фамилию следующим сообщением.'\
    f'\nЭту операцию необходимо проделывать каждый раз для записи.'
    # отправка в тот же чат по id
    answer = bot.send_message(message.chat.id, mess, parse_mode='html');
    # ловим ответ пользователя
    bot.register_next_step_handler(answer, review)
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
def review(message):
    save_mess = message.text + tomorrow.strftime('%d.%m.%Y')
    print(save_mess)

bot.polling(none_stop=True)
