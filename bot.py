from selenium import webdriver
from time import sleep
from random import randint, choice
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By
import os
import json
import datetime
import requests
from time import sleep
from bs4 import BeautifulSoup as bs4
from telethon.sync import TelegramClient, events


with open('config.txt', 'r') as f:
    lines = f.readlines()
    maxsleep = int(lines[3].strip())
    minsleep = int(lines[4].strip())

def message(message):
    with open('config.txt', 'r') as f:
        lines = f.readlines()

        phone = lines[0].strip()
        api_id = lines[1].strip()
        api_hash = lines[2].strip()


    with TelegramClient(phone, api_id, api_hash) as client:
        client.send_message(
            'me', message)


while True:
    try:
        print('Launching Browser')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'pt')
        profile.set_preference('general.useragent.override',
                               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0')
        navegador = webdriver.Firefox(
            executable_path=r'/Program Files/Instagram2/geckodriver.exe', firefox_profile=profile)
        break
    except Exception as e:
        print(e)
        continue


def check(url):
    try:
        navegador.get(url)
        html = navegador.page_source
        soup = bs4(html, 'html.parser')
        outofstockdivs = soup.findAll('div', {'class': 'mt-oos'})

        if len(outofstockdivs) == 0:
            message(f'Product {url} in STOCK! Buy it now!')
        else:
            pass

    except Exception as e:
        message(
            f'This error ocurred during execution of the bot: {e}. Trying again.')


with open('urls.txt', 'r') as f:
    urls = f.readlines()

while True:
    for url in urls:
        url = url.strip()
        print('checking: ', url)
        if len(url) != 0:
            check(url)
            sleep(randint(minsleep, maxsleep))
