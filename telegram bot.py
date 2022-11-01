from time import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

bot = telepot.Bot('5586501093:AAF77HEZZjP8Qbx2kjTAlqHHBCO0ewO2N8o')
# bot.getMe()

previous = time()
delta = 0
seconds = 2

while True:
    current = time()
    delta += current - previous
    previous = current
    
    response = bot.getUpdates()
    # pprint(response)
    
    if delta > seconds:
        
        if response[-1]['channel_post']['text'] == 'Clock':
            print('Clock!!!')
        elif response[-1]['channel_post']['text'] == 'Music':
            print('Music!!!')
        elif response[-1]['channel_post']['text'] == 'Video':
            print('Video!!!')
        delta = 0