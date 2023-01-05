# developed by @Karim Latrach and @tommaso villoto for personal use
# 18/03/2020
# follow me on ig @latrachyoo, @spaccianotty, @tommyvilo and @itagliano.degradato
from colorama import Fore
from selenium import webdriver
import time
from selenium import webdriver
import time
from art import *
import random
import string
import requests
from selenium.webdriver.chrome.options import Options
import requests
import time, colorama, urllib.request
from termcolor import *
from selenium.webdriver.chrome.options import Options
import requests

def emails(usr):
    nome = open("nome.txt", "r+").readlines()
    cognome = open("cognome.txt", "r+").readlines()
    mail = f"{nome[usr]}", f"{cognome[usr]}", f"{random.randint(2,177)}", "@gmail.com"


    print(mail)

    return mail

def usernames(usr):
    nome = open("nome.txt", "r+").readlines()
    cognome = open("cognome.txt", "r+").readlines()
    username = f"{nome[usr]}",f"{cognome[usr]}", f"{random.choice(string.ascii_letters)}", f"{random.choice(string.ascii_letters)}", f"{random.choice(string.ascii_letters)}"

    print(username)

    return username

def sendRequest(link, tempo):
    password = 'password'
    #ck = 0
    #fact = False
    #this = True
    send = 0
    usr = 0
    proxies = open("checked_proxies.txt","r+").readlines()
    if proxies == "":
        print("file is empty Please enter some proxies \nYou can find Proxies on http://www.proxyserverlist24.top/ \n Exiting","red")

    while True:
        try:
            email = emails(usr)
            username = usernames(usr)

            driver = webdriver.Chrome()
            driver.delete_all_cookies()
            driver.get(link)
            driver.delete_all_cookies()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="email_signup"]').send_keys(email)
            driver.find_element_by_xpath('//*[@id="holdon"]/div[1]/div/form/div[2]/input').send_keys(username)
            driver.find_element_by_xpath('//*[@id="password_signup"]').send_keys(password)
            driver.find_element_by_xpath('//*[@id="holdon"]/div[1]/div/form/div[4]/div/label/input').click()
            time.sleep(0.1)
            driver.find_element_by_xpath('//*[@id="btnRegister"]/b').click()
            time.sleep(5)

            usr += 1
            send += 1

            driver.quit()
            time.sleep(tempo)
            print("refresh", send)
        except:
            print("Proxy finite, o non funzionanti")


def checker(proxy):
    proxy_support = urllib.request.ProxyHandler({'https': proxy})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    print("\nSto provando con ==> " + proxy)
    try:
        urllib.request.urlopen("https://www.google.com/")
        cprint(proxy.replace("\n", "") + " Is working\n", 'green')
        with open("checked_proxies.txt", "a+") as appe:
            appe.write(proxy.replace("\n", "") + "\n")

    except:
        cprint(proxy.replace("\n", "") + " Is not working\n", 'red')
        pass


def text2art(text):
    pass


if __name__=="__main__":



    # FIRMA REVISION
    print(
        Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
    print('                        BENVENUTO NEL BOT AUMENTA CLICK BIDOO')
    print(Fore.LIGHTWHITE_EX + '                          DEVOLPED BY LATRACHYOO')
    print("--------------------------------------------------------------------------")
    text =str(('                   LINK'))

    str(Fore.LIGHTRED_EX + "" + str(tprint(text)))
    text = ('      SABOTAGE')

    stri = "latrachyoo devolpment sys"
    print(Fore.LIGHTRED_EX + "")
    str(tprint(text))
    print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
    print(Fore.WHITE + '                                VERSIONE ' , 1)
    print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
    link = 'https://www.bidoo.live/?utm_source=instagram&utm_medium=ig_page&utm_campaign=storia_danknazz&utm_term=28092020-danknazz'
    #link = str(input("LOOP LINK => "))
    tempo = int(input("DISTANZA TRA UN REFRESH IN SEC => "))
    checkask = input("Vuoi testare le proxy o parto con quelle già testate? (1 - 2)\n-: ")
    time.sleep(100)
    sendRequest(link, tempo)



