import requests
import telebot
from telebot import types
from config import TOKEN
from kivano import callpic, callres, callpic2, callres2, callpic3, callres3
from enter import callpic4, callres4, callpic5, callres5, callpic6, callres6



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def first(message):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('KIVANO','ENTER')
    markup.row('О нас')

    bot.send_message(message.chat.id,'Добро пожаловать, <b>{}</b>'.format(message.from_user.full_name),parse_mode='html',reply_markup=markup)



@bot.message_handler(func=lambda message: message.text in ['KIVANO','ENTER','О нас'])
def intermenu(message):
        if message.text == 'KIVANO':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Компьютеры')
            markup.row('Красота и здоровье')
            markup.row('Электроника')
            markup.row('Главное меню')
            bot.send_message(message.chat.id,'Выбери категорию',reply_markup=markup)
        elif message.text == 'ENTER':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.row('Видеокарты')
            markup.row('Системы охлаждения')
            markup.row('Акустика и колонки')
            markup.row('Главное меню')
            bot.send_message(message.chat.id,'Выбери категорию',reply_markup=markup)
        else:
            bot.send_message(message.chat.id,'Наша компания начала свою деятельность на компьютерном рынке под торговой маркой Enter.kg в 2009 году.\nНаша специализация - это розничная мелкооптовая торговля комплектующими, компьютерами, оргтехникой, а также различной электроникой.\n\n\nМаркетплейс Kivano уже 12 лет на рынке и является ведущей платформой ecommerce Кыргызстана.\nЧто мы предлагаем? Интернет-магазин Kivano предлагает 50000 товаров в 500 товарных категорий от 300 продавцов.\nПродаём электронную и бытовую технику, товары для дома, одежду, строительство и ремонт, детские товары и многое другое с быстрой и бесплатной доставкой.')



user_categories = {}

@bot.message_handler(func=lambda message: message.text in ['Компьютеры','Красота и здоровье','Электроника','Видеокарты','Системы охлаждения','Акустика и колонки','Главное меню'])

def goods(message):
    user_categories[message.chat.id] = message.text
    if message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('KIVANO','ENTER')
        markup.row('О нас')

        bot.send_message(message.chat.id,'Вы в главном меню',reply_markup=markup)

    else:
        send_next_item(message.chat.id, message.text)



def send_next_item(chat_id, category):
    try:
        if category == 'Компьютеры':
            img_url = f"https://www.kivano.kg{next(callpic)}"
            bot.send_photo(chat_id, requests.get(img_url).content)

            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres), reply_markup=markup)

        elif category == 'Красота и здоровье':
            img_url = f"https://www.kivano.kg{next(callpic2)}"
            bot.send_photo(chat_id, requests.get(img_url).content)
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres2), reply_markup=markup)

        elif category == 'Электроника':
            img_url = f"https://www.kivano.kg{next(callpic3)}"
            bot.send_photo(chat_id, requests.get(img_url).content)
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres3), reply_markup=markup)


        elif category == 'Видеокарты':
            img_url = f"https://enter.kg{next(callpic4)}"
            bot.send_photo(chat_id, requests.get(img_url).content)
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres4), reply_markup=markup)
        elif category == 'Системы охлаждения':
            img_url = f"https://enter.kg{next(callpic5)}"
            bot.send_photo(chat_id, requests.get(img_url).content)
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres5), reply_markup=markup)
        elif category == 'Акустика и колонки':
            img_url = f"https://enter.kg{next(callpic6)}"
            bot.send_photo(chat_id, requests.get(img_url).content)
            markup = types.InlineKeyboardMarkup()
            markup.row(
                types.InlineKeyboardButton('buy', callback_data='buy'),
                types.InlineKeyboardButton('next', callback_data='next')
            )
            bot.send_message(chat_id, next(callres6), reply_markup=markup)


    except StopIteration:
        bot.send_message(chat_id, "Товар закончился.")



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'next':
        category = user_categories.get(call.message.chat.id)
        send_next_item(call.message.chat.id, category)
    elif call.data == 'buy':
        bot.send_message(call.message.chat.id, "Напишите ваш номер телефона по формуле +996ххххххххх\nФИО\nАртикул товара")

@bot.message_handler(func=lambda message: True)
def any_message(message):
    if message.text.startswith('+'):
        bot.send_message(message.chat.id, "Ваш заказ принят, ожидайте звонка")
        with open('zakaz.txt','a') as z:
            z.write(f'{message.text}\n')
    else:
        bot.send_message(message.chat.id, "Напишите ваш номер телефона по формуле +996ххххххххх\nФИО\nАртикул товара")
    
bot.polling(non_stop=True)