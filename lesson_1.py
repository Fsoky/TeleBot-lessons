import telebot

bot = telebot.TeleBot("YOUR_TOKEN") # Основная переменная, иницилизируем класс TeleBot


@bot.message_handler(content_types=["text"]) # Декоратор, позволит обрабатывать сообщения, команды и прочее..
def text_handler(message):
	if message.text.lower() == "hello":
		bot.send_message(message.chat.id, "Hello, unknown user of Internet!") # Отправляем ответ на сообщение "hello"
	elif message.text.lower() == "how are you?":
		bot.send_message(message.chat.id, "I'm fine, and you?")


bot.polling()