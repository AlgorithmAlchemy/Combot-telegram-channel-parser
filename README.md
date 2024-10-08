##############################################
# Telegram Chats Parser
##############################################
![2024-10-09_00-02](https://github.com/user-attachments/assets/c0ccff53-35a4-424c-b36a-4edf9dacd3ce)

Это проект на Python, который парсит информацию о чатах с сайта [Combot](https://combot.org/) и сохраняет результаты в базу данных SQLite.

![dd_DeWatermark](https://github.com/user-attachments/assets/d9becce2-a13c-49fb-9eef-9ef0b2cda357)


## Особенности
- Сбор информации о чатах (название, юзернейм, количество участников, язык, изображение и т.д.).
- Сохранение данных в базу данных SQLite.
- Парсинг данных с сайта через API с использованием BeautifulSoup и requests.

##############################################
## Требования
##############################################
- Python 3.10+
- Requests
- BeautifulSoup4
- SQLite3 (предустановлен в Python)

##############################################
## Установка
##############################################

1. Клонируйте репозиторий:

```bash
git clone https://github.com/yourusername/telegram-chats-parser.git
cd telegram-chats-parser
```

2. Установите необходимые Python-пакеты:
```bash
pip install requests beautifulsoup4
```
