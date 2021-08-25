import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_TOKEN")


@bot.message_handler(commands=["application"])
def application(message):
	rmk = types.ReplyKeyboardMarkup()
	rmk.add(types.KeyboardButton("Yes"), types.KeyboardButton("No"))

	msg = bot.message_handler(message.chat.id, "Do you want give application to registration?")
	bot.register_next_step_handler(msg, user_answer) # Указываем сообщение и передаем название функции, на которую "прыгнем"


def user_answer(messsage):
	if message.text == "Yes":
		msg = bot.send_message(message.chat.id, "Enter your data")
		bot.register_next_step_handler(msg, user_reg)
	elif message.text == "No":
		bot.send_message(message.chat.id, "Ok.")


def user_reg(message):
	bot.send_message(message.chat.id, f"Your data: {mesage.text}")


bot.polling()