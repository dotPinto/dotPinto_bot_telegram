import os
import telebot
import urllib
from bs4 import BeautifulSoup

HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

my_secret = os.environ['API_KEY']
bot = telebot.TeleBot(my_secret)

url = 'https://www.pcmag.com/news/best-free-pc-console-games-to-claim-this-month'
req = urllib.request.Request(url=url, headers=HDR) 
page = urllib.request.urlopen(req).read()

soup = BeautifulSoup(page)

# h1 = soup.find_all('h1')
# h1 = soup.find_all('h2')
# h1 = soup.find_all('h3')
# h1 = soup.find_all('h4')
# h1 = soup.find_all('h5')
# h1 = soup.find_all('h6')




@bot.message_handler(commands=['freegames'])
def give_freegames(message):
    
    response = ''

    bot.reply_to(message, response)
