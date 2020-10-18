# -*- coding: utf8 -*-
shablon = '''Имя: %s
TELEGRAM: @%s
Город: %s
Район: %s
ID TELEGRAM: %s
Номер перевода: %s
Номер заказа: %s
Товар: %s
Кол-во: %s'''

the_end = '''Вы Бронируете 🌫 %s
У вас есть 60 минут что бы оплатить заказ или он будет отменён.
Ваш номер заказа %s
➖➖➖➖➖➖
📞 Тех. Поддержка: @hawaii_security
➖➖➖➖➖➖
Оплата Easypay ➡️: 26526369
➖➖➖➖➖➖
BitCoin ➡️ 33yPjjSMGHPp8zj1ZXySNJzSUfVSbpXEuL
➖➖➖➖➖➖
GLOBALMONEY ➡️ OFF
➖➖➖➖➖➖
После оплаты ID квитанции написать сюда. После оплаты клад будет выдан сразу!
Где находиться ID - http://prntscr.com/kspcml'''

region_text = '''❗️В случае ненахода - обязательно нужно иметь видеофиксацию до прихода на место, как вы начинаете путь. В противном случае - перезаклад рассматриваться не будет. Если есть проблемы с заказом, пожалуйста обратитесь к оператору @hawaii_oper2 или саппорту @hawaii_security:
🌴 HAWAII WEED 🌴

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Канал:
🌃Чат: @hawaii_shop
🤖Бот: @HawaiiWeedbot

Удачных покупок в HAWAII WEED 🌴
➖➖➖➖➖➖➖➖➖➖
Выберите Район:
➖➖➖➖➖➖➖➖➖'''

tovar_text = '''Внимание! Все клады исключительно свежие и только на магните.
Помощь:
🌴 HAWAII WEED 🌴

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Канал: 
🌃Чат: @hawaii_shop
🤖Бот: @HawaiiWeedbot

Удачных покупок в HAWAII WEED 🌴

➖➖➖➖➖➖➖➖➖➖
%s, выберите товар:'''

mix = '''🍵Коктейль «Amnesia» .
:
0.5 - 125 грн
1 г - 240 грн
2 г - ? грн
5 г - ? грн
10 г - ? грн
20 г - ? грн
30 г - ? грн
50 г - ? грн'''
met = '''🍵Коктейль «Amnesia» - 125 грн за 0.5 грамм.:

0,3 г = 400 грн
0.5 г. = 700 грн
1 г. = 1200 грн'''

hello_text = '''
🌴 HAWAII WEED 🌴

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Канал: 
🌃Чат: @hawaii_shop
🤖Бот: @HawaiiWeedbot

Удачных покупок

⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Если бот не отвечает наберите комманду
/start
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Ежедневная техподдержка и опт:
В случае удаления бота писать оператору.
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Выбери свой Город:'''

city_text = '''Трип-репорты, описание и фото товара!:
🌴 HAWAII WEED 🌴

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Канал: 
🌃Чат: @hawaii_shop
🤖Бот: @HawaiiWeedbot

Удачных покупок в HAWAII WEED 🌴
➖➖➖➖➖➖➖➖➖➖
Выберите Район:
➖➖➖➖➖➖➖➖➖'''

pay_text = '''Вы Бронируете %s
У вас есть 60 минут что бы оплатить заказ или он будет отменён.
Ваш номер заказа %s
➖➖➖➖➖➖
📞 Тех. Поддержка: @hawaii_security
➖➖➖➖➖➖
Оплата Easypay ➡️: 26526369
➖➖➖➖➖➖
BitCoin ➡️ 33yPjjSMGHPp8zj1ZXySNJzSUfVSbpXEuL
➖➖➖➖➖➖
GLOBALMONEY ➡️ OFF
➖➖➖➖➖➖
После оплаты ID квитанции написать сюда. После оплаты клад будет выдан сразу!
Где находиться ID - http://prntscr.com/kspcml'''

thanks_text = '''Ваша оплата принята, клад будет скинут как только бот проверит оплату, эта процедура проходит каждые 60 секунд.
Помощь - 

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Удачных покупок в HAWAII WEED 🌴'''

user_text = '''id: %s
User name: @%s
Имя: %s
Номер последнего заказа: %s'''

import telebot
import constants
import random
import time





bot = telebot.TeleBot(constants.token)

@bot.message_handler(commands=["start"])  # Действия вначале
def start(message):
    if message.text == "/start":
        user_markup = telebot.types.ReplyKeyboardMarkup(True) #создаем кнопки
        user_markup.row("Комсомольск", "Кременчуг")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        sent = bot.send_message(message.chat.id,'''

🌴 HAWAII WEED 🌴

Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security

Канал: 
🌃Чат: @hawaii_shop
🤖Бот: @HawaiiWeedbot

Удачных покупок

⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Если бот не отвечает наберите комманду
/start
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Ежедневная техподдержка и опт:
В случае удаления бота писать оператору.
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Выбери свой Город:''', reply_markup=user_markup)
        bot.register_next_step_handler(sent, region)

def region(message):
    if message.text == "Комсомольск":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Церковь ", "Больница")  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Dnepr)
    elif message.text == "Кременчуг":
        constants.town = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("РАНДОМ",)  # Чтобы добавить кнопку напишите user_markup.row("Ваша кнопка")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, region_text, reply_markup=user_markup)
        bot.register_next_step_handler(sent, tovar_Kiev)

    elif message.text == "Назад":
        message.text = "/start"
        start(message)
    else:
        sent = bot.send_message(message.chat.id, "Данный город не обслуживается. Проверьте, пожалуйста, правильность названия. Или выберете из списка")
        message.text = "/start"
        bot.register_next_step_handler(sent, start)




def tovar_Dnepr(message):
    if message.text == "Церковь": #🎊Микс, ⚜️Шишки (G13), 💤Alfa Белая Синяя, амф
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍵Коктейль «Amnesia»")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)

    elif message.text == "Больница":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍵Коктейль «Amnesia»")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)

def tovar_Kiev(message):
    if message.text == "РАНДОМ":
        constants.region = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🍵Коктейль «Amnesia»")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, tovar_text %(message.from_user.first_name), reply_markup=user_markup)
        bot.register_next_step_handler(sent, end)
   
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def end(message):
    if message.text == "🍵Коктейль «Amnesia»":
        constants.tovar = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("🎉0.5 г - 125 грн")
        user_markup.row("🎉1 г - 240 грн")
        user_markup.row("🎉2 г - 470 грн")
        user_markup.row("Назад")
        sent = bot.send_message(message.chat.id, "🍵Коктейль «Amnesia»",  reply_markup=user_markup)
        bot.register_next_step_handler(sent, pay_Mix)

def pay_Mix(message):
    constants.number = random.randint(1, 100000)
    if message.text == "🎉0.5 г - 125 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end %(message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    if message.text == "🎉1 г - 240 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end %(message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    if message.text == "🎉2 г - 470 грн":
        constants.volume = message.text
        user_markup = telebot.types.ReplyKeyboardMarkup(True)  # создаем кнопки
        user_markup.row("Отмена")
        sent = bot.send_message(message.chat.id, the_end %(message.text, constants.number), reply_markup=user_markup)
        bot.register_next_step_handler(sent, id_pay)
    elif message.text == "Назад":
        message.text = "/start"
        start(message)

def id_pay(message):
    if message.text != "Отмена":
        sent = bot.send_message(message.chat.id, '''⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Ваша оплата принята, клад будет скинут как только бот проверит оплату, эта процедура проходит каждые 60 секунд.
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Наши контакты:
👨🏻‍🎤Оператор: @hawaii_oper2
👨🏻‍🎤Саппорт: @hawaii_security
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆
Если бот не отвечает наберите комманду
/start
⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆⋆''')
        bot.send_message(constants.admin_id, shablon %(message.from_user.first_name, message.from_user.username, constants.town, constants.region, message.from_user.id, message.text,constants.number ,constants.tovar, constants.volume))
        bot.send_message(constants.a, shablon %(message.from_user.first_name, message.from_user.username, constants.town, constants.region, message.from_user.id, message.text,constants.number ,constants.tovar, constants.volume))
        message.text = "/start"
        start(message)
        bot.register_next_step_handler(sent, start)
    else:
        sent = bot.send_message(message.chat.id, '''Ваш заказ отменен''')
        message.text = "/start"
        bot.register_next_step_handler(sent, start)
        start(message)

bot.polling(none_stop=True, timeout=30)