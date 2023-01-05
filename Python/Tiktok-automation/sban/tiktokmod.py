import pyodbc, enlighten, os, random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from ctypes import windll, byref, wintypes
from time import sleep
from art import text2art
from colorama import Fore, init
from colorama import Fore
import requests
from bs4 import BeautifulSoup




def start():
    global driver
    os.system("TASKKILL /F /IM chrome.exe")
    options = Options()
    options.add_argument("start-maximized")
    # Chrome is controlled by automated test software
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # avoiding detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--log-level=3")
    # Default User Profile
    file = open(r"C:\tiktok-doggofresco\chromesettings.txt","r")
    sett_chrome=file.read().split(";")

    options.add_argument("--profile-directory=" + sett_chrome[0])
    options.add_argument("--window-size=1936,1048")
    options.add_argument("--user-data-dir="+sett_chrome[1]) #user config

                                          #
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)



    return driver
def click_path(path):
    global driver
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, path))
    ).click()

def text_path(path, text):
    global driver
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, path))
    ).send_keys(text)

def send_modtk(driver):
    while True:
        driver.get("https://www.tiktok.com/legal/report/feedback?lang=en")
        try:
            pass#driver.delete_all_cookies()
        except:
            pass

        try:
            click_path("/html/body/tiktok-cookie-banner//div/div[2]/button[2]")
        except:
            pass
        text_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[1]/div/input",email)
        text_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[2]/div/input",username)
        click_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[3]/div/select/option[3]")
        click_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[4]/div/select/option[4]")
        text_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[5]/textarea",motivation)
        if len(allegato) != 0:
            text_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[6]/input",allegato)
        click_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[7]/div[1]/label")
        click_path("/html/body/div/div/div[2]/div[2]/main/article/div/form/div[7]/div[2]/label")
        click_path("/html/body/div/div/div[2]/div[2]/main/article/div/button")
        pbar = enlighten.Counter(total=pausa, desc='PAUSA', unit='ticks', color="red")
        for _ in range(pausa):
            pbar.update()
            sleep(1)






    pass
if __name__=="__main__":
    email = input("-- Inserisci un email: ")
    username = input("-- inserisci uno username: ")
    while True:
        motivation = input("-- inserisci una motivazione: ")
        if len(motivation) > 10:
            break
        else:
            print("motivazione troppo corta")
    allegato = input("inserisci un allegato (opzionale): ")
    while True:
        try:
            pausa = int(input("-- inserisci una pausa maggiore di 10 sec: "))
            if pausa > 10:
                break
            else:
                print("pausa troppo corta")
        except:
            print("pausa non valida")

    send_modtk(start())




