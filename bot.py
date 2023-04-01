import telebot
import sqlite3
from telebot.types import Message
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(chat_id=message.chat.id, text=f'Привет {message.from_user.username}, это бот для поиска карточек '
                                                   f'«Черепашки-ниндзя. Боевая четверка»\nЕсли ты такой же олд как и я,'
                                                   f' то напиши номер карточки о которой хочешь узнать)\n\n\n'
                                                   f'Вся информация и изображения взяты с сайта: '
                                                   f'https://www.laststicker.ru/')
    bot.register_next_step_handler(message, callback=search)


def search(message: Message):
    db = sqlite3.connect('cards.db')
    cur = db.cursor()
    try:
        number = int(message.text)
        if 1 <= number <= 260:
            data = cur.execute(f"SELECT * FROM Way_of_ninja WHERE number = {number}").fetchall()[0]
            text = f'Название: {data[1]}\n\nРедкость: {data[3]}\nКатегория: {data[2]}\n\nНомер: {data[0]}/670\n' \
                   f'Номер в серии: {data[0]}/260'
            photo = data[4]

        elif 261 <= number <= 520:
            data = cur.execute(f"SELECT * FROM Shadow_Warriors WHERE number = {number}").fetchall()[0]
            text = f'Название: {data[2]}\n\nРедкость: {data[3]}\n\nНомер: {data[1]}/670\nНомер в серии {data[0]}/260'
            photo = data[4]

        elif 521 <= number <= 670:
            data = cur.execute(f"SELECT * FROM Brothers_in_Arms WHERE number = {number}").fetchall()[0]
            text = f'Название: {data[2]}\n\nРедкость: {data[4]}\nКатегория: {data[3]}\n\nНомер: {data[1]}/670\n' \
                   f'Номер в серии {data[0]}/260'
            photo = data[5]

        else:
            raise Exception

        bot.send_photo(chat_id=message.chat.id, photo=photo, caption=text)
    except:
        text = 'Вы ввели некорректный номер'
        bot.send_message(chat_id=message.chat.id, text=text)
    bot.register_next_step_handler(message, callback=search)


if __name__ == '__main__':
    bot.delete_webhook(drop_pending_updates=True)
    bot.infinity_polling()
