# TMNTcards
## Предыстория
Давным-давно, в далёком-далёком 2010 появились в киосках карточки по прекрасному мультику "Черепашки ниндзя (2003)".

Я был готов продать за них душу, и вот в 2023 я нахожу у себя сундучок полный этих карточек.

Я решил провести "инвентаризацию", а потом подумал яжпрограммист и решил написать скрипт который парсит информацию с сайта https://www.laststicker.ru и создаёт базу данных по всем карточкам, а потом записывает те которые у меня и те которых нет. Затем решил написать телеграмм бота который выдаёт изображение и информацию о карточке по её номеру. Ну и собственно вот...

## Установка и запуск бота

Установить зависимости
> pip install -r requirements.txt

Создать конфиг файл `config.py`

В файл `config.py` записать `TOKEN = 'Токен вашего бота'`

### Если нужно заново создать базу данных

Перед запуском в файл `parser.py` в `headers` записать свои данные User-Agent, 

а в `i_have_WoN` `i_have_SW` `i_have_BiA` записать свои карточки)
> python db.py

### Запустить бота 
> python bot.py