# TeleBot lessons
Исходники с видео-роликов "Telegram Bot PYTHON". В этих исходниках переименованы некоторые переменные, например ~~client~~ -> *bot*\
Если в исходниках присутствуют ошибки, прошу сообщить об этом

__[YouTube канал автора](https://youtube.com/c/Фсоки)__
__[Группа Вконтакте](https://vk.com/fsoky)__

## Урок 1
[Настройка и небольшой чат-бот](https://www.youtube.com/watch?v=AlOBD8C9_yw)

В первом ролике, автор большую часть показывает, как подготовить рабочую директорию, но это не совсем важно. Остальную часть ролика, автор показывает основную структуру кода.

```py
import telebot

bot = telebot.TeleBot("YOUR_TOKEN") # Основная переменная, иницилизируем класс TeleBot


@bot.message_handler(content_types=["text"]) # Декоратор, позволит обрабатывать сообщения, команды и прочее..
def text_handler(message):
	if message.text.lower() == "hello":
		bot.send_message(message.chat.id, "Hello, unknown user of Internet!") # Отправляем ответ на сообщение "hello"
	elif message.text.lower() == "how are you?":
		bot.send_message(message.chat.id, "I'm fine, and you?")


bot.polling()
```

## Урок 2
[Команды и кнопки (Inline, Reply)](https://www.youtube.com/watch?v=LnherAK6NFA)

Здесь автор показывает, как работать с клавиатурой в данном модуле. Показывает, как создаются команды, обработчики.

```py
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
```

## Урок 3
[Пошаговый обработчик (register next step handler)](https://www.youtube.com/watch?v=yFdzGEAYiiE)

В данном видео ролике автор демонстрирует работу пошагового обработчика для бота.

```py
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
```