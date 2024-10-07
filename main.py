import sqlite3
import time
import urllib
from urllib import request
import json

import requests
import urllib3
from bs4 import BeautifulSoup

db = sqlite3.connect('base.sqlite')
connect = db.cursor()

connect.execute('''CREATE TABLE IF NOT EXISTS chats (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  username TEXT,
  pc TEXT,
  language_code TEXT,
  a INTEGER,
  image TEXT,
  p TEXT,
  UNIQUE (username)
)''')

url = 'https://combot.org/api/chart/all?limit=50&offset='

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/98.0.4758.109 Safari/537.36 OPR/84.0.4316.31 (Edition 360-1)', 'accept': '*/*'}
PARAMS = None


def parse():
    error = 0
    nice = 0
    page_count = 0
    page_drop = 32670        # парсим с 0 страницы прибавляя по 20
    for i in range(0, 150000):
        page_count += 1
        fr_url = url.replace(f"offset=", f"offset={page_drop}")
        page_drop += 29
        try:
            page = requests.get(fr_url)
        except:
            print("timeout connect 5 seconds.")
            time.sleep(5)
            continue
        soup = BeautifulSoup(page.text, 'html.parser')
        try:
            site_json = json.loads(soup.text)
        except json.decoder.JSONDecodeError:
            time.sleep(5)
            print("JSONDecodeError.")
            continue
        # print(fr_url)

        for i in site_json:
            title = i['t']
            username = i['u']
            pc = i['pc']
            language_code = i['l']
            a = i['a']
            image = i['i']
            p = i['p']

            inf_list = (title, username, pc, language_code, a, image, p)
            try:  # вносим данные парсера в бдшку
                connect.execute(f'''INSERT INTO chats 
                (title, username,  pc, language_code, a, image, p)
                VALUES(?, ?, ?, ?, ?, ?, ?)''', inf_list)
                db.commit()
                nice += 1
            except sqlite3.IntegrityError:
                error += 1
                pass
                # if pri.lower() == "on":
                # print("Uniq name error")

        print(f"Page num: {page_drop}       Parse page count: {page_count}        Nice: {nice}         Error: {error}")

        time.sleep(0.26)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse()
