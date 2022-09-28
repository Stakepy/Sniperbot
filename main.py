import telebot
from telebot import types

bot = telebot.TeleBot('5776260408:AAGy2cbKqrtJuqR3zW_g8d_k1vi7DWZMQ0Y')

@bot.message_handler(commands=['help', 'start', 'restart'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item2 = types.KeyboardButton('Розклад уроків 📝')
    item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
    item6 = types.KeyboardButton('/start')
    markup.add(item2, item3, item6 )
    bot.send_message(message.chat.id,
                     'Привіт, {0.first_name}!'.format(message.from_user), reply_markup = markup)

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.chat.type == 'private':
            if message.text == 'Розклад дзвінків 🛎️':
                bot.send_message(message.chat.id, '\n1) 8:00 - 9:20   \n2) 9:35 - 10:55   \n3) 11:20 - 12:45  \n4) 13:00 - 14:20')
            elif message.text == 'Розклад уроків 📝':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item3 = types.KeyboardButton('Понеділок')
                item4 = types.KeyboardButton('Вівторок')
                item5 = types.KeyboardButton('Середа')
                item6 = types.KeyboardButton('Четвер')
                item7 = types.KeyboardButton('Пятниця')
                back = types.KeyboardButton('⬅️Назад')
                start2 = types.KeyboardButton('/restart')
                markup.add(item3, item4, item5, item6, item7, back, start2)
                bot.send_message(message.chat.id, 'Розклад уроків 📝', reply_markup = markup )
            elif message.text == 'Понеділок':
                bot.send_message(message.chat.id,
                                 '\n1.Історія України/Хімія'
                                 '\n2.Хімія/Геометрія'
                                 '\n3.Фізична культура'
                                    )
            elif message.text == 'Вівторок':
                bot.send_message(message.chat.id,
                                 '\n1.Біологія'
                                 '\n2.Захист України'
                                 '\n3.Інформатика'
                                 )

            elif message.text == 'Середа':
                bot.send_message(message.chat.id,
                                 '\n1.Хімія/Фізична культура'
                                 '\n2.Інформатика'
                                 '\n3.Зарубіжна література'
                                 '\n4.Фізика'
                                 )
            elif message.text == 'Четвер':
                bot.send_message(message.chat.id,
                                 '\n1.Всесвітня історія'
                                 '\n2.Українська мова'
                                 '\n3.Українська література'
                                 '\n4.Година спілкування'
                                 )
            elif message.text == 'Пятниця':
                bot.send_message(message.chat.id,
                                 '\n1.Історія України'
                                 '\n2.Алгебра'
                                 '\n3.Іноземна мова'
                                 )
            elif message.text == '⬅️Назад':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item2 = types.KeyboardButton('Розклад уроків 📝')
                item3 = types.KeyboardButton('Розклад дзвінків 🛎️')
                item6 = types.KeyboardButton('/start')
                markup.add(item2, item3, item6 )
                bot.send_message(message.chat.id, '⬅️Назад' , reply_markup = markup)

bot.polling(none_stop = True)