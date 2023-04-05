from bs4 import BeautifulSoup as Soup
import requests
import re

link1 = 'https://www.laststicker.ru/cards/turtleninja_cards/'
link2 = 'https://www.laststicker.ru/cards/turtleninja_cards-2/'
link3 = 'https://www.laststicker.ru/cards/turtleninja_cards-3/'


def parser(link):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0'}
    response = requests.get(link, headers=headers).content

    soup = Soup(response, 'html.parser')
    if link == 'https://www.laststicker.ru/cards/turtleninja_cards/':
        string = str(soup.find_all('tbody')[1])
    else:
        string = str(soup.find_all('tbody'))
    string = string[8:]

    result = re.findall(r">[CcPYа-яА-ЯёЁ\W0-9]+<", string)

    list1 = []
    for i in result:
        try:
            int(i[1:-1])
        except ValueError:
            try:
                float(i[1:-1])
            except ValueError:
                if i[1:-1] not in ['C'+str(x) for x in range(1, 8)]:
                    list1.append(i[1:-1])
    list3 = [[list1[i], list1[i+1], list1[i+2]] for i in range(0, len(list1), 3)]

    return list3


cards_list_WoN = parser(link1)
cards_list_SW = parser(link2)
cards_list_BiA = parser(link3)

i_have_WoN = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 19, 21, 23, 25, 26, 27, 29, 35, 37, 39, 41, 42, 43, 44, 46,
              50, 51, 53, 58, 59, 61, 64, 65, 67, 69, 70, 72, 74, 78, 81, 82, 84, 89, 93, 94, 97, 98, 100, 101, 103,
              104, 108, 112, 114, 115, 116, 118, 122, 124, 125, 126, 128, 135, 136, 138, 139, 140, 141, 142, 143, 146,
              147, 148, 149, 151, 152, 156, 157, 161, 168, 172, 173, 177, 182, 184, 186, 187, 190, 191, 197, 198, 199,
              201, 204, 206, 208, 209, 210, 211, 212, 215, 216, 220, 221, 223, 224, 226, 228, 231, 232, 236, 237, 238,
              239, 240, 241, 242, 246, 247, 252, 253, 255, 257, 260, 262, 263, 264, 265, 266, 267]

i_have_SW = [263, 264, 266, 270, 274, 277, 307, 313, 325, 328, 332, 335, 350, 351, 358, 367, 370, 372, 395, 410, 411,
             415, 416, 425, 427, 440, 443, 455, 456, 459, 460, 462, 467, 474, 477, 488, 490, 495, 496, 504]

i_have_BiA = [530, 555, 579, 583, 599, 602, 606, 626]
