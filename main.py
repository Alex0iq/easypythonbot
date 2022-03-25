#Создателем данного бота является Пастухов Александр
#Оригинал кода можно найти на https://github.com/Alex0iq/easypythonbot/


import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):


    # Создание клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Информатика")
    item2 = types.KeyboardButton("Профильная математика")
    item3 = types.KeyboardButton("Русский язык")
    item5 = types.KeyboardButton("ХимБио")
    #Вместо Информатика, ХимБио и т д ваше название кнопок клавиатуры
    #Например item1 = types.KeyboardButton("Ваше название кнопки")
    markup.add(item1, item2, item3, item5)
    #добавление этих кнопок на клавиатуру
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - Бот {1.first_name}, и я помогу тебе сдать экзамены на высший балл!".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
    #Стартовое сообщение которое пришлет бот(может быть изменено на что угодно)
    #{0.first_name} - пользователь который запустил бота
    #{1.first_name} - название вашего бота
@bot.message_handler(content_types=['text'])
#Далее создается функция которая отвечает что пришлет бот в зависимости от команды пользователя
#Очень важно в строчке if message.text == 'Информатика': Информатику заменить на название вашей кнопки, чуть ниже сообщение
#которое пришлет бот
def razgovor(message):
    if message.chat.type == 'private':
        if message.text == 'Информатика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Полезный канал с теорией: https://t.me/+Mo1DhM5F6g5jYjMy', reply_markup=markup)
        elif message.text == 'Профильная математика':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Краткая информация о предстоящем экзамене в 2022 году: https://telegra.ph/Profilnyj-EGEH-po-matematike-2022-02-11', reply_markup=markup)
            bot.send_message(message.chat.id, 'Полезный канал с кучей материалов: https://t.me/+NkCzk6ejOuxiODgy', reply_markup=markup)
        elif message.text == 'Русский язык':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Полезный канал с теорией: https://t.me/+0vEux3BOjfxjZDEy', reply_markup=markup)
        elif message.text == 'ХимБио':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Очень полезный канал от моей подруги: https://t.me/+GKcWftPZgv9hNTMy', reply_markup=markup)

bot.polling(none_stop=True)
#чтобы бот не прекращал работу