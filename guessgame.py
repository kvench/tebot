import telebot
import random
token = "475058781:AAESECL2BMUDfOF38v-vl6qjfrirZw31BSQ"

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Привет! Я умею играть в игру загадай число. Напиши /game для начала игры.")


numbers = {}
@bot.message_handler(commands=['game'])
def game(message):
    user_id = message.chat.id
    numbers[user_id] = random.randint(1,10)
    bot.send_message(user_id, "Число загадано, угадайте число от 0 до 10")

@bot.message_handler(content_types=['text'])
def guessing (message):
    user_id = message.chat.id

    try:
        if int(message.text) == numbers[user_id]:
            bot.send_message(user_id, "Ты угадал число, молодец! Если хочешь играть ещё напиши /game")
        else:
            bot.send_message(user_id, "Ты не угадал, попробуй ещё. Если ты не знаешь, что делать, напиши /help")
    except:   bot.send_message(user_id, "Ты отправил текстовое сообщение, Напиши число цифрами или, если ты не знаешь что делать напиши /help")

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)
