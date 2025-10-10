from tkinter.constants import W
from telebot import *
from random import randint
import json
right_arr=[]
with open('right.json', 'r') as file:
    right_arr = json.load(file)

wrong_arr=[]
with open('wrong.json', 'r') as file:
    wrong_arr = json.load(file)

token = ''
bot = TeleBot(token)

def arr_gen(key):
    q_arr = [0]*4
    for i in range(len(q_arr)):
        if i==key:
            q_arr[i] = right_arr[randint(0, len(right_arr)-1)]
        else:
            variant = wrong_arr[randint(0,len(wrong_arr)-1)]
            while variant in q_arr:
                variant = wrong_arr[randint(0,len(wrong_arr)-1)]
            q_arr[i] = variant
    return q_arr

def main_kb():
    kb1 = types.KeyboardButton("Начать жестко ботать 4 номер❗️❗️❗️(нажми меня)")
    markup = types.ReplyKeyboardMarkup()
    markup.add(kb1)
    return markup

def ex4_kb(q_arr):
    item1 = types.KeyboardButton(q_arr[0])
    item2 = types.KeyboardButton(q_arr[1])
    item3 = types.KeyboardButton(q_arr[2])
    item4 = types.KeyboardButton(q_arr[3])
    item5 = types.KeyboardButton("Молю хватит🙏🙏🙏")
    markup = types.ReplyKeyboardMarkup(row_width=4)
    markup.add(item1,item2,item3,item4)
    markup.add(item5)
    return markup
def ex4_main(message, key,q_arr, streak, wrong_ans):
   
    if message.text=="Молю хватит🙏🙏🙏":

        markup = main_kb()
        bot.send_message(message.chat.id, "Как прикажете 😈", reply_markup=markup)
        if len(wrong_ans)!=0:
            s = ', '.join(wrong_ans)
            z = f'Вам стоит повторить слова: {s}'
            bot.send_message(message.chat.id, z)
        else:
            bot.send_message(message.chat.id, "Вы ХОРОШО ПОСТАРАЛИСЬ)..... ошибок не было❗️❗️❗️❗️")
        return 0
    elif key == -1:
        key = randint(0,3)
        q_arr = arr_gen(key)
        markup = ex4_kb(q_arr)
        msg = bot.send_message(message.chat.id, "Выберите вариант, где ударение поставлено верно", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex4_main(message,key,q_arr, streak, wrong_ans))
    elif not(message.text in q_arr):
        markup = ex4_kb(q_arr)
        msg = bot.send_message(message.chat.id, "Это ваще че отвечай давай😡😡😡", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex4_main(message,key,q_arr, streak,wrong_ans))
    elif message.text==q_arr[key]:
        streak+=1
        s = f"Верно! R E S P E C T 💯 ВАШ СТРИК ОТВЕТОВ: {streak}"
        bot.send_message(message.chat.id, s)
        key = randint(0,3)
        q_arr = arr_gen(key)
        markup = ex4_kb(q_arr)
        msg = bot.send_message(message.chat.id, "Выберите вариант, где ударение поставлено верно", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex4_main(message,key,q_arr, streak,wrong_ans))
    elif message.text!=q_arr[key]:
        streak = 0
        ind = wrong_arr.index(message.text)
        wrong_ans.append(right_arr[ind])
        wrong_ans.append(q_arr[key])
        s = f'ОШИБКА НОВИЧКА❗️ правильный ответ ❗️❗️❗️{q_arr[key]}❗️❗️❗️ ВАШЕМУ СТРИКУ КОНЕЦ)'
        streak = 0
        print(q_arr)
        bot.send_message(message.chat.id, s)
        key = randint(0,3)
        q_arr = arr_gen(key)
        markup = ex4_kb(q_arr)
        msg = bot.send_message(message.chat.id, "Выберите вариант, где ударение поставлено верно", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex4_main(message,key,q_arr, streak,wrong_ans))
    
@bot.message_handler(commands=["start"])
def start(message):
  
    markup = main_kb()
    bot.send_message(message.chat.id, "ЕГЭ НАЧАЛОСЬ !!!", reply_markup=markup)
@bot.message_handler(content_types=["text"])
def ex4_start(message):
    if message.text == "Начать жестко ботать 4 номер❗️❗️❗️":
        ex4_main(message, -1,[0,0,0,0], 0,[]   )
    else:
        markup = main_kb()
        bot.send_message(message.chat.id, "ЕГЭ НАЧАЛОСЬ !!!", reply_markup=markup)




bot.infinity_polling()
