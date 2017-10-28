# -*- coding: utf-8 -*-
import random

def onQQMessage(bot, contact, member, content):
    if content.find('睡觉') != -1:
        bot.SendTo(contact, 'Have a nice dream!')
    elif content == '早':
        msg = [
	    'Morning!',
            'What a wonderful day!',
            'Ow ya going',
            'Wish you a lovely morning!',
            'Good morning!'
	]
        bot.SendTo(contact, random.choice(msg))
    elif content == 'faq':
       bot.SendTo(contact, 'FAQs: https://goo.gl/gE5ABF')
