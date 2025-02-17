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
driver.get('https://www.4zida.rs/prodaja-stanova/gradske-lokacije-novi-sad/vlasnik?sortiranje=najnoviji')
time.sleep(2)

flat_to_compare = ""

while True:
    element = driver.find_element(By.CSS_SELECTOR, "div.flex.flex-col.gap-2")
    element = element.find_element(By.CSS_SELECTOR, "a.flex.justify-between.gap-1")
    href = element.get_attribute("href")
    if flat_to_compare != href:
        bot.send_message(chat_id=channel_id, text=href)
        flat_to_compare = href

    driver.refresh()
    time.sleep(20)
