# -*- coding: utf-8 -*-
import random
from random import randint
import datetime

def onQQMessage(bot, contact, member, content):
    if isSayGoodbuy(content):
        if 0 == randint(0, 1):
            return
        msg = [
	    'See you tomorrow!',
            'Good night!',
            'Have a nice dream!',
            'Have a sweet dream!'
	]
        bot.SendTo(contact, random.choice(msg))
    elif isMornigGreeting(content):
        if 0 == randint(0, 1):
            return
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

def isSayGoodbuy(content):
    keys = ['睡觉', '睡了']
    for key in keys:
        if content.find(key) != -1:
            return True
    return False

def isMornigGreeting(content):
    if isMorningTime() == False:
        return
    keysMatch = ['早', '早啊']
    keysContain = ['早上好']
    for key in keysMatch:
        if content == key:
            return True
    for key in keysContain:
        if content.find(key) != -1:
            return True        
    return False

def isMorningTime():
    now = datetime.datetime.now()
    today5am = now.replace(hour=18, minute=0, second=0, microsecond=0)
    today10am = now.replace(hour=23, minute=0, second=0, microsecond=0)
    if now < today10am and now > today5am:
        return True
    return False
