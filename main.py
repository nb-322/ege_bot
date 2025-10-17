from tkinter.constants import W
from telebot import *
from random import randint
import json


# Загружаем токен из файла
try:
    with open('token.txt', 'r') as f:
        token = f.read().strip()
except FileNotFoundError:
    print("ОШИБКА: Файл token.txt не найден!")
    print("Создайте файл token.txt и поместите в него токен вашего бота")
    exit(1)
bot = TeleBot(token)

def arr_gen(key, right_arr, wrong_arr):
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
    kb2 = types.KeyboardButton("Начать жестко ботать 12 номер❗️❗️❗️(нажми меня)")
    markup = types.ReplyKeyboardMarkup()
    markup.add(kb1)
    markup.add(kb2)
    return markup

def ex_kb(q_arr):
    item1 = types.KeyboardButton(1)
    item2 = types.KeyboardButton(2)
    item3 = types.KeyboardButton(3)
    item4 = types.KeyboardButton(4)
    item5 = types.KeyboardButton("Молю хватит🙏🙏🙏")
    markup = types.ReplyKeyboardMarkup(row_width=4)
    markup.add(item1,item2,item3,item4)
    markup.add(item5)
    return markup
def ex_main(message, key,q_arr, streak, wrong_ans, ex,right_arr, wrong_arr):
    z='\n'
    if streak == 5:
        bot.send_message(message.chat.id, "Неплохой стри).....")
    elif streak == 10:
        bot.send_message(message.chat.id, "Хороший стрик)....")
    elif streak == 15:
        bot.send_message(message.chat.id, "ОГРОМНЫЙ СТРИК❗️❗️❗️")
    elif streak ==20:
        bot.send_message(message.chat.id, "ЭТОТ СТРИК ПРОСТО ГИГАНТСКИЙ")
    if message.text=="Молю хватит🙏🙏🙏":

        markup = main_kb()
        bot.send_message(message.chat.id, "Как прикажете 😈", reply_markup=markup)
        if len(wrong_ans)!=0:
            s = ', '.join(wrong_ans)
            z = f'Вам стоит повторить слова: {s}, но вы все равно молодец).....'
            bot.send_message(message.chat.id, z)
        else:
            bot.send_message(message.chat.id, "Вы ХОРОШО ПОСТАРАЛИСЬ)..... ошибок не было❗️❗️❗️❗️")
        return 0
    elif key == -1:
        key = randint(0,3)
        q_arr = arr_gen(key, right_arr,wrong_arr)
        markup = ex_kb(q_arr)
        if ex==4:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {', '.join(q_arr)}", reply_markup=markup)
        elif ex==12:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {z.join(q_arr)}", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex_main(message,key,q_arr, streak, wrong_ans,ex,right_arr, wrong_arr))
    elif not(message.text in ["1","2","3","4"]):
        markup = ex_kb(q_arr)
        msg = bot.send_message(message.chat.id, "Это ваще че отвечай давай😡😡😡", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex_main(message,key,q_arr, streak,wrong_ans,ex,right_arr, wrong_arr))
    elif int(message.text)-1==key:
        streak+=1
        s = f"Верно! R E S P E C T 💯 ВАШ СТРИК ОТВЕТОВ: {streak}"
        bot.send_message(message.chat.id, s)
        key = randint(0,3)
        q_arr = arr_gen(key, right_arr,wrong_arr)
        markup = ex_kb(q_arr)
        if ex==4:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {', '.join(q_arr)}", reply_markup=markup)
        elif ex==12:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {z.join(q_arr)}", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex_main(message,key,q_arr, streak,wrong_ans,ex,right_arr, wrong_arr))
    elif int(message.text-1 )!=key:
        streak = 0
        
        if ex==4:
            ind = wrong_arr.index(q_arr[int(message.text)-1]   )
            wrong_ans.append(right_arr[ind])
        wrong_ans.append(q_arr[key])
        s = f'ОШИБКА НОВИЧКА❗️ правильный ответ ❗️❗️❗️{q_arr[key]}❗️❗️❗️ есть над чем поработать).....'
        streak = 0
        print(q_arr)
        bot.send_message(message.chat.id, s)
        key = randint(0,3)
        q_arr = arr_gen(key, right_arr,wrong_arr)
        markup = ex_kb(q_arr)
        if ex==4:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {', '.join(q_arr)}", reply_markup=markup)
        elif ex==12:
            msg = bot.send_message(message.chat.id, f"Выберите верный вариант: {z.join(q_arr)}", reply_markup=markup)
        bot.register_next_step_handler(msg, lambda message: ex_main(message,key,q_arr, streak,wrong_ans,ex,right_arr, wrong_arr))
    
@bot.message_handler(commands=["start"])
def start(message):
  
    markup = main_kb()
    bot.send_message(message.chat.id, "ЕГЭ НАЧАЛОСЬ !!!", reply_markup=markup)
@bot.message_handler(content_types=["text"])
def ex4_start(message):
    if message.text=="322":
        for _ in range(13):
            bot.send_message(message.chat.id, "НАЙДУ❗️❗️❗️")
    elif message.text == "Начать жестко ботать 4 номер❗️❗️❗️(нажми меня)":
        right_arr=[]
        with open('right4.json', 'r') as file:
            right_arr = json.load(file)

        wrong_arr=[]
        with open('wrong4.json', 'r') as file:
            wrong_arr = json.load(file)
        ex_main(message, -1,[0,0,0,0], 0,[] ,4,right_arr,wrong_arr  )
    elif message.text == "Начать жестко ботать 12 номер❗️❗️❗️(нажми меня)":
        right_arr=[]
        with open('right12.json', 'r') as file:
            right_arr = json.load(file)

        wrong_arr=[]
        with open('wrong12.json', 'r') as file:
            wrong_arr = json.load(file)
        ex_main(message, -1,[0,0,0,0], 0,[],  12,right_arr,wrong_arr )
    else:
        markup = main_kb()
        bot.send_message(message.chat.id, "ЕГЭ НАЧАЛОСЬ !!!", reply_markup=markup)




bot.infinity_polling()
