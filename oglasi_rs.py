import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import telebot

bot = telebot.TeleBot("8116867522:AAFOUlW5xLjPjtdAociSSFLNW66oaxOqxSQ")
channel_id = "5357149995"

sys.path.append(os.curdir + '\\..')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://www.oglasi.rs/nekretnine/prodaja-stanova/novi-sad?s=d&rt=vlasnik&p=1')
time.sleep(2)

flat_to_compare = []

while True:
    try:
        flat_list_div = driver.find_element(By.CSS_SELECTOR, 'div[itemtype="http://schema.org/ItemList"]')
        flat_list = flat_list_div.find_elements(By.CSS_SELECTOR, 'article[itemtype="http://schema.org/Product"]')
        flat_holder = flat_list[0].find_element(By.CSS_SELECTOR, ".fpogl-holder")
        flat = flat_holder.find_element(By.CSS_SELECTOR, ".fpogl-list-title")
        flat_link = flat.get_attribute("href")
        if flat_link in flat_to_compare:
            pass
        else:
            flat_to_compare.append(flat_link)
            if len(flat_to_compare) > 20:
                del flat_to_compare[0]
            bot.send_message(chat_id=channel_id, text=flat_link)
    except:
        pass
    driver.refresh()
    time.sleep(20)
