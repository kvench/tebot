import telebot

token = "475058781:AAESECL2BMUDfOF38v-vl6qjfrirZw31BSQ"

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Я ржумэн уровня про. Напиши /anek для случайного анекдота или /pic для получения случайного мема.")


# content_types=['text'] - сработает, если нам прислали текстовое сообщение
    # message - входящее сообщение
@bot.message_handler(commands=['pic'])
def pic(message):
    user = message.chat.id
    #отправляем мем
    bot.send_photo(user, "https://pp.userapi.com/c830209/v830209594/7e4a/QJodaxex-Lw.jpg" )

@bot.message_handler(commands=['anek'])
def anek(message):
     #отправляем анек
    user = message.chat.id
    bot.send_message(user, 'Ленин на броневике. Ельцин на танке. Саакашвили на крыше. Чем мельче политик, тем выше забирается.'  )

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)