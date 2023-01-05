from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import os

def wait(path):
    try:
        sleep(1)
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        return myElem
    except:
        pass


def tabkey(clicks,text):
    actions = ActionChains(driver)
    for _ in range(clicks):
        actions = actions.send_keys(Keys.TAB)
        sleep(1)
    actions.send_keys(text)
    actions.perform()






from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# avoiding detection
options.add_argument('--disable-blink-features=AutomationControlled')

# Default User Profile
options.add_argument("--profile-directory=Default")
options.add_argument(r"--user-data-dir=C:/Users/latra/AppData/Local/Google/Chrome/User Data")

driver = webdriver.Chrome(options=options)
driver.get('https://www.tiktok.com/login')
#input("premere invio quando fatto il login: ")
driver.get("https://www.tiktok.com/upload?lang=it-IT")
tabkey(7,"hello")
path= r"C:\Users\latra\Desktop\file.mp4"
sleep(2)
for _ in range(200):
    try:
        driver.find_element(By.CSS_SELECTOR,'#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-410242825.uploader > div > div > button').click()
        sleep(1)


        print("cliked")

    except Exception as e:
        print(e)
        pass




















