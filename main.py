import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# создаем объект бота
bot = telebot.TeleBot('6030065868:AAG-NZo8mgE_Wsj-NGFjeMFL9QuAHkbpf04')

# функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот с кнопками. Нажми на кнопку, чтобы узнать больше.')

    # создаем кнопки
    keyboard = InlineKeyboardMarkup()
    button_help = InlineKeyboardButton('Как пользоваться ботом?', callback_data='help')
    button_contacts = InlineKeyboardButton('Контакты', callback_data='contacts')
    keyboard.add(button_help, button_contacts)

    # добавляем кнопки в сообщение
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=keyboard)

# функция для обработки нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    if call.data == 'help':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пока никак :( т.к я еще пишу код ')
    elif call.data == 'contacts':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Мои контакты: email@example.com')

@bot.message_handler(commands=['Balance'])
def menu(message):
    bot.send_message(message.chat.id, 'Что вы хотите? Пополнить баланс, узнать баланс, снять деньги с баланса.')

    keyboards = InlineKeyboardMarkup()
    button_balance = InlineKeyboardButton('Пополнить', callback_data='bal')
    button_unkbal = InlineKeyboardButton('Узнать', callback_data='unkbal')
    button_anbal = InlineKeyboardButton('Снять', callback_data='anbal')
    keyboards.add(button_balance, button_unkbal, button_anbal)

    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=keyboards)

@bot.callback_query_handler(func=lambda call: True)
def buttons(call):
    if call.data == 'bal':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пополнить можно по этому счету: (реквизиты)')
    elif call.data == 'unkbal':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ваш баланс составляет: 10000000 рублей')
    elif call.data == 'anbal':
        bot.edit_message_text(chat_id=call.message.caht.id, message_id=call.message.message_id, text='Снять деньги запрещено!!!!')

# запускаем бота
bot.polling(non_stop=True)