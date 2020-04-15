import telebot
from telebot import types
import COVID19Py

covid19 = COVID19Py.COVID19()
bot = telebot.TeleBot('1154277651:AAHmEAGh_4gOvnsvf7ANPGvSu6g1eMxuPdk')

# Функция, что сработает при отправке команды Старт
# Здесь мы создаем быстрые кнопки, а также сообщение с привествием
@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	btn1 = types.KeyboardButton("Butun dunyo bo'yicha")
	btn2 = types.KeyboardButton('Qozogiston')
	btn3 = types.KeyboardButton('Rossiya')
	btn4 = types.KeyboardButton("O'zbekiston")
	markup.add(btn1, btn2, btn3, btn4)

	send_message = f"<b>Salom {message.from_user.first_name}!</b>\nKoronavirus bo'yicha malumotlarni bilish uchun yozing" \
		f"Davlat nomi, masalan: Aqsh, O'zbekiston, Rossiya\n"
	bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)

# Функция, что сработает при отправке какого-либо текста боту
# Здесь мы создаем отслеживания данных и вывод статистики по определенной стране
@bot.message_handler(content_types=['text'])
def mess(message):
	final_message = ""
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "aqsh":
		location = covid19.getLocationByCountryCode("US")
	elif get_message_bot == "ukraina":
		location = covid19.getLocationByCountryCode("UA")
	elif get_message_bot == "rossiya":
		location = covid19.getLocationByCountryCode("RU")
	elif get_message_bot == "o'zbekiston":
		location = covid19.getLocationByCountryCode("UZ")
	elif get_message_bot == "qozogiston":
		location = covid19.getLocationByCountryCode("KZ")
	elif get_message_bot == "italiya":
		location = covid19.getLocationByCountryCode("IT")
	elif get_message_bot == "fransiya":
		location = covid19.getLocationByCountryCode("FR")
	elif get_message_bot == "germaniya":
		location = covid19.getLocationByCountryCode("DE")
	elif get_message_bot == "yaponiya":
		location = covid19.getLocationByCountryCode("JP")
	else:
		location = covid19.getLatest()
		final_message = f"<u>Butun dunyo bo'yicha malumotlar:</u>\n<b>Kasallanganlar: </b>{location['confirmed']:,}\n<b>Vafot etganlar: </b>{location['deaths']:,}"

	if final_message == "":
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Mamlakat bo'yicha malumotlar:</u>\nRasmiy kanalimiz: @instagram_tv_video\n" \
				f"Oxirgi yangilanish: {date[0]} {time[0]}\nOxirgi malumotlar:\n<b>" \
				f"Kasallanganlar: </b>{location[0]['latest']['confirmed']:,}\n<b>Vafot etganlar: </b>" \
				f"{location[0]['latest']['deaths']:,}"

	bot.send_message(message.chat.id, final_message, parse_mode='html')

# Это нужно чтобы бот работал всё время
bot.polling(none_stop=True)
