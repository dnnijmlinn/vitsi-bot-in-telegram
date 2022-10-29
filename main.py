from gettext import dpgettext
import requests
import random
import telebot
from telebot import types 
from bs4 import BeautifulSoup as b

URL = 'https://www.vitsienvitsit.fi/vitsit/'
API_KEY = '###########'
def parser(url):
    r = requests.get(url)

    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('p', class_='vitsiUnselectable')

    return [c.text for c in anekdots]

list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "kirjoita jotain, niin lähetän vitsin")


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.isdigit:
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'write something and Ill send you a joke.')

bot.polling(none_stop=True)


