from time import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop
import requests

bot = telepot.Bot('5586501093:AAF77HEZZjP8Qbx2kjTAlqHHBCO0ewO2N8o')
# bot.getMe()

def send_to_telegram(message):

    apiToken = '5586501093:AAF77HEZZjP8Qbx2kjTAlqHHBCO0ewO2N8o'
    chatID = '-1001683258640'
    apiURL = f'https://api.telegram.org/bot5586501093:AAF77HEZZjP8Qbx2kjTAlqHHBCO0ewO2N8o/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

previous = time()
delta = 0
seconds = 5
flag = 0

while True:
    current = time()
    delta += current - previous
    previous = current
    
    response = bot.getUpdates()
    # pprint(response)
    
    if delta > seconds:
        if response[-1]['update_id'] !=  flag:
            send_to_telegram("I have received [" + response[-1]['channel_post']['text'] + "] ~ !")
            flag = response[-1]['update_id']
        delta = 0