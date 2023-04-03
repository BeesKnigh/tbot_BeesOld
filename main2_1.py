import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import config
import time as tm

# создаем объект бота
bot = telebot.TeleBot(config.TOKEN)

# функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот BeesOld. Нажми на кнопку, чтобы узнать больше.')

    # создаем кнопки
    keyboard = InlineKeyboardMarkup()
    button_help = InlineKeyboardButton('Как пользоваться ботом?', callback_data='help')
    button_contacts = InlineKeyboardButton('Контакты', callback_data='contacts')
    keyboard.add(button_help, button_contacts)

    # добавляем кнопки в сообщение
    bot.send_message(message.chat.id, 'Выбери действие:', reply_markup=keyboard)

# функция для обработки нажатий на кнопки и команды /Balance
@bot.callback_query_handler(func=lambda call: True)
def button(call):
    if call.data == 'help':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Бот создан в коммерческих целях.(By BeesKnight)\nУже имеется одна полностью рабочая команда: /Balance ')
    elif call.data == 'contacts':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Мои контакты: email@example.com')
    elif call.data == 'bal':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Пополнить можно по этому счету: (реквизиты)')
    elif call.data == 'unkbal':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ваш баланс составляет: 10000000 рублей')
    elif call.data == 'anbal':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Снять деньги запрещено!!!!')
    elif call.data == 'balance':
        bot.send_message(chat_id=call.message.chat.id, text='Для возможности приглашать других людей, внесите предоплату 100 рублей.')

@bot.message_handler(commands=['Balance'])
def balance(message):
    keyboards = InlineKeyboardMarkup()
    button_balance = InlineKeyboardButton('Пополнить', callback_data='balance')
    button_unkbal = InlineKeyboardButton('Узнать', callback_data='unkbal')
    button_anbal = InlineKeyboardButton('Снять', callback_data='anbal')
    keyboards.add(button_balance, button_unkbal, button_anbal)

    bot.send_message(message.chat.id, 'Что вы хотите? Пополнить баланс, узнать баланс, снять деньги с баланса.', reply_markup=keyboards)

@bot.message_handler(commands=['time'])
def show_time(message):
    # получаем текущее время
    current_time = tm.strftime('%H:%M:%S', tm.localtime())
    # получаем время через 3 дня
    future_time = tm.strftime('%H:%M:%S', tm.localtime(tm.time() + 3*24*60*60))
    # получаем дату через 3 дня
    future_date = tm.strftime('%d.%m.%Y', tm.localtime(tm.time() + 3*24*60*60))
    # получаем текущую дату
    current_date = tm.strftime('%d.%m.%Y', tm.localtime())
    # отправляем сообщение с временем и датой
    bot.send_message(message.chat.id, f'Текущая дата: {current_date}\nТекущее время: {current_time}')
    bot.send_message(message.chat.id, f'Время и дата через 3 дня:\n{future_date}\n{future_time}')
# запускаем бота
bot.polling(non_stop=True)