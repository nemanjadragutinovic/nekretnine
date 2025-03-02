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
driver.get('https://www.kupujemprodajem.com/nekretnine-kupoprodaja/pretraga?categoryId=26&locationId=16&period=today&order=posted%20desc')
time.sleep(2)

flat_to_compare = []

while True:
    try:
        third_child = driver.find_element("xpath", "(//div[contains(@class, 'Grid_col-lg-10')])/*[3]")
        first_child = third_child.find_element("xpath", "./*")
        element = first_child.find_element(By.CSS_SELECTOR, "a.Link_link__2iGTE")
        href_value = element.get_attribute("href")
        if href_value in flat_to_compare:
            pass
        else:
            flat_to_compare.append(href_value)
            if len(flat_to_compare) > 20:
                del flat_to_compare[0]
            bot.send_message(chat_id=channel_id, text=href_value)
    except:
        pass
    driver.refresh()
    time.sleep(20)
