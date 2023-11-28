import telebot

bot = telebot.TeleBot('6693004315:AAHSVg80aziZF4yeI5W-L6V2ZK1a_0z_9nM')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Что вы хотите сделать с этим ботом?', parse_mode='Markdown')


@bot.message_handler(commands=['talk'])
def talk(message):
    bot.send_message(message.chat.id, text='*Сегодня чудесная погода*', parse_mode='Markdown')


@bot.message_handler(commands=['wiki'])
def wiki(message):
    bot.send_message(message.chat.id, text='[Википедия](https://ru.wikipedia.org/wiki)', parse_mode='Markdown')


bot.infinity_polling()