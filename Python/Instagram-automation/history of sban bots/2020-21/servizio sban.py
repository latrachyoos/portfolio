# developed by @Tommaso Vilotto for personal use
# 12/28/2019
# follow me on ig @tommyvilo and @itagliano.degradato
from selenium import webdriver
import time
import requests
import random
import string
import os
from selenium.webdriver.chrome.options import Options

# boolean ran= True;

choice = 2


def mails():
    mail = ""
    value = random.randint(5, 15)
    dizio = {1: 'a', 3: 'c', 2: 'b', 5: 'e', 4: 'd', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j', 13: 'm', 12: 'l',
             15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't', 23: 'w', 22: 'v', 25: 'y', 24: 'x',
             26: 'z'}
    for i in range(0, value):
        x = dizio[random.randint(1, 26)]
        mail += x
    mail += "@gmail.com"
    return mail


def phones():
    number = "+393"
    for i in range(0, 9):
        number += str(random.randint(0, 9))
    return number


def countProxy():
    ck = 0
    f = open("proxyList.txt", "r+")
    for line in f:
        for letter in line:
            if letter == ";":
                ck = ck + 1
    f.close()
    return ck


def getProxy(num):
    f = open("proxyList.txt", "r+")
    ck = 0
    for line in f:
        if ck == num:
            proxy = line
            break
        else:
            ck += 1
    proxy = proxy[:-1]
    f.close()
    print(proxy)
    return proxy


def delete(num):
    f = open("proxyList1.txt", "r+")
    f1 = open("proxyList.txt", "w+")
    ck = 0
    for line in f:
        if ck == num:
            ck += 1
        else:
            f1.write(line)
            ck += 1
    f.close()
    f1.close()


def sendRequest(nome, username, text, mail, phone, paese, tempo):
    sent = 0
    num = 0
    # num1=countProxy()
    print("REQUESTS SENT: ", sent)
    driver = webdriver.Chrome()
    # name='Tommaso Vilotto'
    # username='itagliano.degradato'
    # text= 'Hi, I was working with an influencer marketing agency. I closed the contract and strangely my account was deactivated. I am afraid it is a kind of revenge of the agency. Please help me recover the account.I am desperate and I do not know how. I hope your fantastic support team can help me.I wish you a good job.'

    ck = 0
    pausa = 0
    # print(countProxy())
    fact = False
    this = True
    while True:
        a = 1
        while 1 < 10:  # mod1
            driver.get("https://help.instagram.com/contact/606967319425038")

            if pausa == 20:
                print("IN PAUSA PER 20minuti \n")
                time.sleep(1200)
                print("PAUSA TERMINATA \n")
                pausa = 0
            pausa += 1
            if choice == "1":
                mail = mails()
                phone = phones()
            if ck == 1 and fact == True and this == True:
                driver.quit()
                fact = False
                hostname = "13.69.155.75"
                port = "8080"
                chrome_options = Options()
                chrome_options.add_argument('--proxy-server={}'.format(getProxy(num)))
                driver = webdriver.Chrome(options=chrome_options)
                ck = (random.randint(1, 3))
                num += 1

            else:
                ck = 0


            try:
                t = time.perf_counter()
                driver.find_element_by_id('649649255120112').send_keys(name)
                driver.find_element_by_id('1464214030500550').send_keys(username)
                driver.find_element_by_id('328991337275965').send_keys(mail)
                driver.find_element_by_id('602863763172693').send_keys(phone)
                driver.find_element_by_id('709786765737601').send_keys(text)
                driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
                n = False
                while n == False:
                    try:
                        driver.find_element_by_xpath(
                            '//a[@class="_42ft _42fu layerConfirm uiOverlayButton selected _42g- _42gy"]').click()
                        n = True
                        i += 1
                    except:
                        n = False
                t1 = time.perf_counter()
                sent += 1
                print("REQUESTS SENT: ", sent)
                time.sleep(tempo)
            except:
                # print("da rimuovere")
                num -= 1
                # delete(num)
                fact = True

        b = 1
        while b < 2: #mod2
            driver.get("https://help.instagram.com/contact/1652567838289083")

            if pausa == 20:
                print("IN PAUSA PER 20 di minuti \n")
                time.sleep(1200)
                print("PAUSA TERMINATA \n")
                pausa = 0
            pausa += 1



            try:
                t = time.perf_counter()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="SupportFormRow.904224879693114"]/div[3]/label[1]').click()
                time.sleep(4)
                driver.find_element_by_id('904224879693114.1').send_keys(name)
                driver.find_element_by_id('495070633933955').send_keys(name)
                driver.find_element_by_id('1489970557888767').send_keys(username)
                driver.find_element_by_id('488955464552044').send_keys(mail)
                try:
                    driver.find_element_by_id('u_0_e').send_keys(paese)
                    driver.find_element_by_id('u_0_e').send_keys(Keys.RETURN)
                except:
                    driver.find_element_by_id('u_0_c').send_keys(paese)
                    driver.find_element_by_id('u_0_c').send_keys(Keys.RETURN)

                driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()

                try:
                    driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
                    b += 1
                except:
                    ck = 0

                driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
                # driver.find_element_by_xpath('//button[@class="text').click()
                t1 = time.perf_counter()
                sent += 1
                print("REQUESTS SENT: ", sent)

                time.sleep(tempo)

            except:

                fact = True




def provalo():
    num = 0
    while True:
        num += 1
        try:

            driver = webdriver.Chrome()
            driver.quit()
            fatc = False
            chrome_options = Options()
            chrome_options.add_argument('--proxy-server={}'.format(getProxy(num)))
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://www.google.com/')

        except:
            print('da togliere')
            num -= 1
            delete(num)


if __name__ == "__main__":
    # FIRMA REVISION
    print('------------------------------------------------------------ ')

    response = requests.get("https://artii.herokuapp.com/make?text=SERVIZIO_SBAN&font=slant")
    print(response.text)
    import time
    time.sleep(5)

    print('------------------------------------------------------------\n ')
    # FINE FIRMA
    print("")
    print("")
    print("                BOT PER SBAN ATTRAVERSO LINK MOD1 AVVIATO CORRETAMENTE                ")
    print("")
    print("")
    nome = input("Inserisci nome e cognome spaziati es: KARIM LATRACH ")
    username = input("Inserire username account es: Spaccianotty ")
    choice = input("SCEGLI: \n - NUMERO E MAIL RANDOM(1)\n - NUMERO e MAIL PERSONALI(2): ")
    mail = ""
    phone = ""
    if choice == "2":
        mail = input("inserisci mail :")
        phone = input("inserisci numero di telefono ")
    text = input("Inserisci motivazione sban: ")
    paese = input("Inserisci paese es: Italia ")
    tempo = int(input("Inserisci tempo in secondi tra un modulo e l'altro "))
    print("Verranno utilizzate mail e numeri di telefoni diversi per ogni modulo inviato! \n")
    sendRequest(nome, username, text, mail, phone, paese, tempo)

