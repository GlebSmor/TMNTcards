from env import text_WoN, i_have_WoN, text_SW, i_have_SW, text_BiA, i_have_BiA
import re
import sqlite3


db = sqlite3.connect('cards.db')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Way_of_ninja (
                number INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                rarity TEXT NOT NULL,
                image TEXT NOT NULL,
                availability TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Shadow_Warriors (
                id INTEGER PRIMARY KEY,
                number INTEGER NOT NULL,
                name TEXT NOT NULL,
                rarity TEXT NOT NULL,
                image TEXT NOT NULL,
                availability TEXT)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Brothers_in_Arms (
                id INTEGER PRIMARY KEY,
                number INTEGER NOT NULL,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                rarity TEXT NOT NULL,
                image TEXT NOT NULL,
                availability TEXT)''')


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------Way of Ninja-------------------------------------------------------


result = re.findall(r">[CPYа-яА-ЯЁё\W]+<", text_WoN)
cards_list = [[result[i], result[i + 1], result[i + 2]] for i in range(0, len(result) - 2, 3)]

link = 'https://www.laststicker.ru/i/cards/123/'
count = 1
for card in cards_list:
    if count <= 260:
        img = link + str(count) + '.jpg'
        cur.execute(f"INSERT INTO Way_of_ninja (name, category, rarity, image) VALUES ('{card[0][1:-1]}', "
                    f"'{card[1][1:-1]}', '{card[2][1:-1]}', '{img}')")
    else:
        img = link + 'c' + str(count - 260) + '.jpg'
        cur.execute(
            f"INSERT INTO Way_of_ninja (name, category, rarity, image) VALUES ('{card[0][1:-1]}', "
            f"'{card[1][1:-1]}', '{card[2][1:-1]}', '{img}')")
    count += 1

data = cur.execute(f"SELECT number, availability FROM Way_of_ninja WHERE availability IS NULL").fetchall()
for elem in data:
    if elem[0] in i_have_WoN:
        cur.execute(f"UPDATE Way_of_ninja SET availability = 'Есть' WHERE number = {elem[0]}")
    else:
        cur.execute(f"UPDATE Way_of_ninja SET availability = 'Нет' WHERE number = {elem[0]}")
    cur.execute(f"UPDATE Way_of_ninja SET rarity = 'O' WHERE rarity = '-'")


# --------------------------------------------------Shadow Warriors-----------------------------------------------------


result = re.findall(r">[CPYа-яА-ЯЁё\W]+<", text_SW)
cards_list = [[result[i], result[i + 1], result[i + 2]] for i in range(0, len(result) - 2, 3)]

link = 'https://www.laststicker.ru/i/cards/274/'
count = 261
for card in cards_list:
    img = link + str(count) + '.jpg'
    cur.execute(f"INSERT INTO Shadow_Warriors (number, name, rarity, image) VALUES ('{count}', '{card[0][1:-1]}',"
                f"'{card[1][1:-1]}', '{img}')")
    count += 1

data = cur.execute(f"SELECT number, availability FROM Shadow_Warriors WHERE availability IS NULL").fetchall()
for elem in data:
    if elem[0] in i_have_SW:
        cur.execute(f"UPDATE Shadow_Warriors SET availability = 'Есть' WHERE number = {elem[0]}")
    else:
        cur.execute(f"UPDATE Shadow_Warriors SET availability = 'Нет' WHERE number = {elem[0]}")


# -------------------------------------------------Brothers in Arms-----------------------------------------------------


result = re.findall(r">[CPYа-яА-ЯЁё\W]+<", text_BiA)
cards_list = [[result[i], result[i + 1], result[i + 2]] for i in range(0, len(result) - 2, 3)]

link = 'https://www.laststicker.ru/i/cards/838/'
count = 521
print(cards_list)
for card in cards_list:
    img = link + str(count) + '.jpg'
    cur.execute(f"INSERT INTO Brothers_in_Arms (number, name, category, rarity, image) VALUES ('{count}', "
                f"'{card[0][1:-1]}', '{card[1][1:-1]}', '{card[2][1:-1]}', '{img}')")
    count += 1

data = cur.execute(f"SELECT number, availability FROM Brothers_in_Arms WHERE availability IS NULL").fetchall()
for elem in data:
    if elem[0] in i_have_BiA:
        cur.execute(f"UPDATE Brothers_in_Arms SET availability = 'Есть' WHERE number = {elem[0]}")
    else:
        cur.execute(f"UPDATE Brothers_in_Arms SET availability = 'Нет' WHERE number = {elem[0]}")


db.commit()
