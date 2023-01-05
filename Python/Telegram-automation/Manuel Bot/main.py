#5743046086:AAGlFUJm5I4aJeQWW66nasyp7PBFOT6ugm8
import os
from time import sleep

import pyodbc
import telegram
from selenium import webdriver
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
from telethon import TelegramClient

global autorizzato





updater = Updater("5742708830:AAFUSXHSlo-T0p3ryhI8kU2dTHKkpPI43Rk",
                  use_context=True)


autorizzato = False
def chrome():
    from selenium.webdriver.chrome.options import Options
    os.system("TASKKILL /F /IM chrome.exe")
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--profile-directory=Profile 1")
    options.add_argument("--user-data-dir=C:/Users/Manuel Di Geronimo/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    return driver
def send_query(query, case):
    global conn
    conn = pyodbc.connect(

        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\tiktok-doggofresco\history_of_posts.accdb;')
    #
    cursor = conn.cursor()
    cursor.execute(query)
    if case != 3:
        conn.commit()
    return cursor
def message(testo):
    global nomepc

    if logins.lower() == "si":
        try:
            client.send_message(msg, message=nomepc + ": " + testo)
        except:
            pass

def login():
    global client, dati, nomepc
    if logins.lower()=="si":
        try:
            phone_pc ="+393517153396"
            api_id =16240473
            api_hash ="6d30aa1da295b46adcebc02186d9ede5"

            client = TelegramClient(nomepc, api_id, api_hash)
            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(phone_pc)
                client.sign_in(phone_pc, input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))
            message('IS ONLINE remote server')
        except:
            print('LOGIN FAIL')


#itshairbyivy;itshairbyivy;Daniellaemilien@gmail.com;393515049286;unbaneme;msg;nomepc;no
def send_bot(update, context):
    try:
        global autorizzato, msg, nomepc, logins, user
        txt = str(update.message.text).split(";")
        user = txt[0]
        name = txt[1]
        mail = txt[2]
        phone = txt[3]
        mot = txt[4]
        msg = txt[5]
        nomepc = txt[6]
        logins = txt[7]
        if logins.lower() =="si":
            login()
        # user;name;mail;phone;mot;msg;nomepc;logins
        driver = chrome()
        # mod1


        driver.get("https://www.google.com/search?q=instagram+contact+606967319425038&rlz=1C1ONGR_itIT1022IT1022&oq=instagram+contact+606967319425038&aqs=chrome.0.69i59j0i546l4j69i60l3.335j0j9&sourceid=chrome&ie=UTF-8")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a"))).click()
        sleep(2)
        try:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]"))).click()
        except:
            pass
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/input"))).send_keys(name)
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/div[3]/input"))).send_keys(mail)
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/div[4]/input"))).send_keys(user)
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/div[5]/input"))).send_keys(phone)
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/div[6]/textarea"))).send_keys(mot)
        sleep(2)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div/div/div[3]/div/div[2]/div/form/button"))).click()
        sleep(2)

        sleep(10)
        try:
            try:
                #/html/body/div[2]/div[2]/div/div/div/div[3]/div/a
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                    (By.XPATH,
                     "/html/body/div[2]/div[2]/div/div/div/div[3]/div/a"))).click()
                message("mod1 mandato corettamente senza captcha")
            except:


                for _ in range(2):
                    driver.switch_to.frame(driver.find_element(By.ID, 'captcha-recaptcha'))
                    WebDriverWait(driver, 50).until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]"))).click()
                    for _ in range(1000):
                        text = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]").text
                        if text == "Captcha solved!":

                            sleep(5)
                            driver.switch_to.default_content()
                            WebDriverWait(driver, 50).until(
                                EC.element_to_be_clickable(
                                    (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div[3]/div/button"))).click()
                            break
                        else:
                            sleep(0.5)
                    try:
                        WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH,
                                                        "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/nav/div/div[1]/div/div[1]/div/div/div/div/div/div/span/span/div/div/div[1]/div[2]/div[1]/div/div")))
                        break
                    except:
                        pass
        except:
            print("error")


        driver.delete_all_cookies()
        driver.quit()
    except Exception as e:
        print(e)
        try:
            message("errore gnerico mod1 per user: @" + user)
        except:
            message("errore gnerico mod1")








def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "comando: ")







updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, send_bot))
updater.start_polling()
updater.idle()