import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_TOKEN")


@bot.message_handler(commands=["get_info", "info"])
def get_user_info(message):
	markup_inline = types.InlineKeyboardMarkup() # Создаем Inline клавиатуру для сообщения
	item_yes = types.InlineKeyboardButton(text="YES!", callback_data="yes") # Создаем кнопку
	item_no = types.InlineKeyboardButton(text="NO!", callback_data="no")

	markup_inline.add(item_yes, item_no) # Добавляем кнопки в нашу клавиатуру
	bot.send_message(message.chat.id, "Do you want to know info about you?", reply_markup=markup_inline) # Прикрепляем кнопки к сообщению


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data == "yes":
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True) # Создаем клавиатуру и делаем кнопки маленькими
		item_id = types.KeyboardButton("My ID")
		item_nickname = types.KeyboardButton("My nickname")

		markup.add(item_id, item_nickname) # Добавляем кнопки в нашу клавиатуру
		bot.send_message(call.message.chat.id, "Press one button", reply_markup=markup_reply)
	elif call.data == "no":
		pass


@bot.message_handler(content_types=["text"])
def text_handler(message):
	if message.text.lower() == "My ID":
		bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}")
	elif message.text.lower() == "My nickname":
		bot.send_message(message.chat.id, f"Your nickname: {message.from_user.first_name} {message.from_user.last_name}")


bot.polling()