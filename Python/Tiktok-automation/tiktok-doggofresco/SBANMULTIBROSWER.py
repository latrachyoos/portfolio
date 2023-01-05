#DATA CREAZIONE SBANYOO: 18/03/2020
#AGGIORNAMENTO DEFINITIVO - PASSAGGIO DA SELENIUM A REQUESTS 4/02/2022, ACCANTONATO E ELIMINATO TUTTO DI SBANYOO SELENIUM :(
#reintegro selenium mod4 21/07 - migraggio richesto a windows

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from colorama import init, Fore, Style
from telethon.sync import TelegramClient
import requests, random, os, pandas as pd
#169.197.83.75:11748@4k81j:rci9l8e5

def chrome():
    from selenium.webdriver.chrome.options import Options
    os.system("TASKKILL /F /IM chrome.exe")
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--profile-directory=Default")
    options.add_argument("--user-data-dir=C:/Users/latra/AppData/Local/Google/Chrome/User Data")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    return driver
def plusservice(LINK, data, head):
    global k, txt, send,modplus, tentativi
    send = True
    txt = ""
    varnum = 0

    if verprox:
        proxies = {
            'http': 'http://' + proxi,
            'https': 'http://' + proxi
        }
        r = requests.session()

        req = r.post(LINK, data=data, headers=head, timeout=10, proxies=proxies)
    else:
        r = requests.session()

        req = r.post(LINK, data=data, headers=head, timeout=10)
    #print(req.text)


    print(Fore.LIGHTYELLOW_EX + "[STARUS CODE]" + Style.RESET_ALL, req.status_code)
    if "COVID" in req.text:
        txt += ", BLOCK X COVID"
        message("@" + user[k] + ' BLOCK X COVID ')
        send = False
    if "We need you to provide a valid email address, so our support team can contact you." in req.text:
        txt += ", INVALID EMAIL"
        message("@" + user[k] + ' INVALID EMAIL ')
        send = False
    if "We cannot find record of User ID that you entered." in req.text or "The Given Instagram User ID is Invalid" in req.text:
        txt += ", INVALID ID"
        message("@" + user[k] + ' ID NON ESISTENTE ')
        send = False
    if "Go to Instagram and confirm it&#039;s you before requesting a review." in req.text:
        txt += ", MOD 1 BLOCKED"
        message("@" + user[k] + ' MOD1 BLOCCATO')
        send = False
    if "There was a problem with this request. We're working on getting it fixed as soon as we can." in req.text:
        txt += ", MOD 5 XX PROBLEMA DI RICHIESTA"
        send = False
    if "The username or short-link you provided does not belong to an inactive Instagram Account." in req.text:
        message("https://instagram.com/" + user[k] + ' RESTORED')
        txt += ", ACCOUNT !!!! ATTIVO UNBANED !!!!"
        send = False
    if "We limit how often you can post, comment or do other things in a given amount of time in order to help protect the community from spam." in req.text:
        txt += ", BLOCCATO PER SPAM"
        message("@" + user[k] + ' ANDATO IN SPAM')
        send = False
    if "A confirmation is required before you can proceed." in req.text:
        txt += ", CONFRIM UNKNOW ERROR"
        message("@" + user[k] + ' CONFRIM UNKNOW ERROR')
        send = False
    if "We could not process your request. Please try again later." in req.text:
        txt += ", ELIMINAZIONE IN CORSO"
        message("@" + user[k] + ' ELIMINAZIONE IN CORSO')
        send = False
    if "You may want to slow down or stop to avoid a restriction on your account. We limit how often you can post, " \
       "comment or do other things in a given amount of time to help protect the community from spam." in req.text:

        if modplus == 2:
            dga = {
                "jazoest": 2877,
                "lsd": "AVo2TMelPC0",
                "AccountType": "Personal",
                "name": str(nomis[k]),
                "Field1489970557888767": str(user[k]),
                "email": str(maill[k]),
                "Field236858559849125_iso2_country_code": "US",
                "Field236858559849125": "Stati Uniti",
                "support_form_id": 1652567838289083,
                "support_form_hidden_fields": "%7B%22904224879693114%22%3Afalse%2C%22495070633933955%22%3Afalse%2C%221489970557888767%22%3Afalse%2C%22488955464552044%22%3Afalse%2C%22236858559849125%22%3Afalse%2C%221638971086372158%22%3Atrue%2C%221615324488732156%22%3Atrue%2C%22236548136468765%22%3Atrue%7D",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
                "__csr": "",
                "__req": "7",
                "__hs": "18955.BP:DEFAULT.2.0.0.0.",
                "dpr": 1,
                "__ccg": "EXCELLENT",
                "__rev": 1004770477,
                "__s": "f3vso6:mkvxmk:d2jut0",
                "__hsi": "7034234083541491106-0",
                "__comet_req": 0,
                "__spin_r": 1004770477,
                "__spin_b": "trunk",
                "__spin_t": 1639767966,
                "confirmed": "1"
            }
            LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
            head = {
                "Host": "help.instagram.com",
                "Connection": "close",
                "Content-Length": "930",
                "X-FB-LSD": "AVo2TMelPC0",
                # "sec-ch-ua-mobile": "?0",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                # "sec-ch-ua": ';Not A Brand";v="99", "Chromium";v="88"',
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "Origin": "https://help.instagram.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://help.instagram.com/contact/1652567838289083",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.5",

            }
        else:
            dga = {
                "jazoest": 2890,
                "lsd": "AVp_e1Vy20M",
                "name": nomis[k],
                "email": maill[k],
                "instagram_username": user[k],
                "mobile_number": phonis[k],
                "appeal_reason": text[k],
                "support_form_id": 606967319425038,
                "support_form_hidden_fields": "{}",
                "support_form_fact_false_fields": "[]",
                "__user": 0,
                "__a": 1,
                "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
                "__csr": "",
                "__req": "8",
                "__hs": "18980.BP%3ADEFAULT.2.0.0.0.",
                "dpr": 1,
                "__ccg": "EXCELLENT",
                "__rev": 1004889841,
                "__s": "074in0%3Atrxneu%3A88f4ol",
                "__hsi": "7043332365423471873-0",
                "__comet_req": 0,
                "__spin_r": 1004889841,
                "__spin_b": "trunk",
                "__spin_t": 1639903608,
                "confirmed": "1",
            }
            LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
            head = {
                "Host": "help.instagram.com",
                "Connection": "close",
                "Content-Length": "627",
                "X-FB-LSD": "AVp_e1Vy20M",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "*/*",
                "Origin": "https://help.instagram.com",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://help.instagram.com/contact/606967319425038",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.5",
            }
        if tentativi == 0:
            tentativi+=1

            plusservice(LINK, dga, head)
        else:
            tentativi = 0
        if modplus == 1:
            mode = "mod 1"
        else:
            mode = "mod 2"
        txt += ", RISCHIO BAN PER SPAM (confirm "+mode+")"
        message("@" + user[k] + " RISCHIO BAN PER SPAM (confirm "+mode+")")
        send = False
    if req.status_code == 429:
        txt += ", TROPPE RICHIESTE, RIAVVIARE LA CONNESSIONE"
        message("@" + user[k] + ' TROPPE RICHIESTE, CONSIGLIO DI RIAVVIARE LA CONNESSIONE')
        varnum += 1
        send = False
    if req.status_code == 500:
        txt += ", MODULO NON MANDATO"
        message("@" + user[k] + ' NON MANDATO')
        send = False
    return send
def message(testo):
    global nomepc
    if logins.lower() == "si":
        try:
            client.send_message(msg, message=nomepc + ": " + testo)
        except:
            pass
def slept():
    try:
        if tempo > 30:
            tempomom = random.randint(tempo - 10, tempo + 10)
        else:
            tempomom = random.randint(tempo, tempo + 10)
        print(Fore.LIGHTYELLOW_EX + "[TIME]" + Style.RESET_ALL + " PAUSA DI: ", tempomom, "SECONDI")
        sleep(tempomom)
    except:
        pass
def login():
    global client, dati, nomepc
    try:
        phone = dati[0]
        api_id = int(dati[1])
        api_hash = dati[2]

        client = TelegramClient(nomepc, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))
        message('IS ONLINE')
    except:
        print('LOGIN FAIL')
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
def mod1plus():
    global k


    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    data = {
        "jazoest": 2914,  # 2890,
        "lsd": "AVqGkw8tK28",  # "AVr_Dx9PS9A",
        "name": nomis[k],
        "instagram_username": user[k],
        "email": maill[k],
        "mobile_number": phonis[k],
        "appeal_reason": text[k],
        "support_form_id": 606967319425038,
        "support_form_hidden_fields": "{}",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W09yyE158",
        # "7xe6Fo4OQ1PyWwHBWo5O12wAxu13wqovzEy58ogbUuw9-3K4o1j8hwem0nCq1ewcG0KEswaq1xwEw7BKdwnU1e42C220qu1TwoU2swdq0Ho2ew",
        "__csr": "",
        "__req": "4",  # h
        "__hs": "18947.BP:DEFAULT.2.0.0.0.",  # new
        # "__beoa": 0,
        # "__pc": "PHASED:DEFAULT",
        # "__bhv": 2,
        "dpr": 1,  # 3
        "__ccg": "EXCELLENT",
        "__rev": 1004737389,  # 1003521343,
        "__s": "6z732o:0uk3s3:k9j7j6",  # "8x0mgw:dal0sr:s5g412",
        "__hsi": "7031219665036584047-0",  # "6943937313156005653-0",
        "__comet_req": 0,
        "__spin_r": 1004737389,  # 1003521343,
        "__spin_b": "trunk",
        "__spin_t": 1637083399,  # 1616761394
    }
    head = {
        # ----------------------------
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",  # "en-us",
        "Connection": "keep-alive",
        "Content-Length": "581",  # new
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "help.instagram.com",

        "Origin": "https://help.instagram.com",
        "Referer": "https://help.instagram.com/contact/606967319425038",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "X-FB-LSD": "AVqGkw8tK28",  # "AVr_Dx9PS9A",
        # "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content"
    }
    return plusservice(LINK, data, head)
def mod2aplus():
    global k

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {
        # ----------------------------

        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",  # "en-us",
        "Connection": "keep-alive",
        "Content-Length": "911",  # new
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "help.instagram.com",
        # cookie no
        "Origin": "https://help.instagram.com",
        "Referer": "https://help.instagram.com/contact/1652567838289083",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "X-FB-LSD": "AVrwqcag4mI",  # "AVr_Dx9PS9A",
        # "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content"
    }
    data1 = {
        "jazoest": 2877,
        "lsd": "AVo2TMelPC0",
        "AccountType": "Personal",
        "name": str(nomis[k]),
        "Field1489970557888767": str(user[k]),
        "email": str(maill[k]),
        "Field236858559849125_iso2_country_code": "US",
        "Field236858559849125": "Stati Uniti",
        "support_form_id": 1652567838289083,
        "support_form_hidden_fields": "%7B%22904224879693114%22%3Afalse%2C%22495070633933955%22%3Afalse%2C%221489970557888767%22%3Afalse%2C%22488955464552044%22%3Afalse%2C%22236858559849125%22%3Afalse%2C%221638971086372158%22%3Atrue%2C%221615324488732156%22%3Atrue%2C%22236548136468765%22%3Atrue%7D",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
        "__csr": "",
        "__req": "7",
        "__hs": "18955.BP:DEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1004770477,
        "__s": "f3vso6:mkvxmk:d2jut0",
        "__hsi": "7034234083541491106-0",
        "__comet_req": 0,
        "__spin_r": 1004770477,
        "__spin_b": "trunk",
        "__spin_t": 1639767966,
        "confirmed": "1"



    }
    data = {
        "jazoest": 21030,
        "lsd": "AVrwqcag4mI",
        "AccountType": "Personal",
        "name": str(nomis[k]),
        "Field1489970557888767": str(user[k]),
        "email": str(maill[k]),
        "Field236858559849125_iso2_country_code": "",
        "Field236858559849125": "United States",
        "support_form_id": 1652567838289083,
        "support_form_hidden_fields": "{\"904224879693114\":false,\"495070633933955\":false,\"1489970557888767\":false,\"488955464552044\":false,\"236858559849125\":false,\"1638971086372158\":true,\"1615324488732156\":true,\"236548136468765\":true}",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
        "__csr": "",
        "__req": "7",
        "__hs": "18955.BP:DEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1004770477,
        "__s": "f3vso6:mkvxmk:d2jut0",
        "__hsi": "7034234083541491106-0",
        "__comet_req": 0,
        "__spin_r": 1004770477,
        "__spin_b": "trunk",
        "__spin_t": 1637785249,
    }

    return plusservice(LINK, data, head)
def mod2bplus():
    global k

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {
        # ----------------------------

        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",  # "en-us",
        "Connection": "keep-alive",
        "Content-Length": "911",  # new
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "help.instagram.com",
        # cookie no
        "Origin": "https://help.instagram.com",
        "Referer": "https://help.instagram.com/contact/1652567838289083",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "X-FB-LSD": "AVrwqcag4mI",  # "AVr_Dx9PS9A",
        # "Referer": "https://help.instagram.com/contact/606967319425038?helpref=page_content"
    }

    data = {
        "jazoest":2938,
        "lsd":"AVpcOUA_W6o",
        "AccountType":"Business",
        "name":nomis[k],
        "Field1489970557888767":user[k],
        "email":maill[k],
        "Field236858559849125_iso2_country_code":"US",
        "Field236858559849125":"Stati%20Uniti",
        "Field236548136468765[0]":"confirmation",
        "support_form_id":1652567838289083,
        "support_form_hidden_fields":"%7B%22904224879693114%22%3Afalse%2C%22495070633933955%22%3Afalse%2C%221489970557888767%22%3Afalse%2C%22488955464552044%22%3Afalse%2C%22236858559849125%22%3Afalse%2C%221638971086372158%22%3Afalse%2C%221615324488732156%22%3Afalse%2C%22236548136468765%22%3Afalse%7D",
        "support_form_fact_false_fields":"[]",
        "__user":0,
        "__a":1,
        "__dyn":"7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo",
        "__csr":"",
        "__req":"8",
        "__hs":"19066.BP%3ADEFAULT.2.0.0.0.",
        "dpr":1,
        "__ccg":"EXCELLENT",
        "__rev":1005197378,
        "__s":"k4qedz%3Adubj8r%3A6i6uhe",
        "__hsi":"7075370115674727854-0",
        "__comet_req":0,
        "__spin_r":1005197378,
        "__spin_b":"trunk",
        "__spin_t":"1647362978"
    }

    return plusservice(LINK, data, head)
def mod3aplus():

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {

        "Host": "help.instagram.com",
        "Connection": "close",
        "Content-Length": "562",
        "X-FB-LSD": "AVpLpLZbfN8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://help.instagram.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://help.instagram.com/contact/1610459702591585",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",

    }
    data = {
        "jazoest":2951,
        "lsd":"AVpLpLZbfN8",
        "instagram_user_name":user[k],
        "additional_details":text[k],
        "support_form_id":1610459702591585,
        "support_form_hidden_fields":"{}",
        "support_form_fact_false_fields":"[]",
        "__user":0,
        "__a":1,
        #"__dyn":"7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
        "__csr":"",
        "__req":5,
        "__hs":"19092.BP:DEFAULT.2.0.0.0.",
        "dpr":1,
        "__ccg":"EXCELLENT",
        "__rev":1004940863,
        "__s":"y18vnw:8dlt33:s4y6j9",
        "__hsi":"7053140572569764402-0",
        "__comet_req":0,
        "__spin_r":1004940863,
        "__spin_b":"trunk",
        "__spin_t":1642187259,

    }
    return plusservice(LINK, data, head)
def mod3plus():

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {

        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Length": "643",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "help.instagram.com",
        "Origin": "https://help.instagram.com",
        "Referer": "https://help.instagram.com/contact/1784471218363829?helpref=page_content",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "X-FB-LSD": "AVr7gU0n7TY",
    }
    data = {
        "jazoest": 2894,
        "lsd": "AVr7gU0n7TY",
        "name": nomis[k],
        "username": user[k],
        "email": maill[k],
        "Field236858559849125_iso2_country_code": "US",
        "Field236858559849125": "United State",
        "user_comment": text[k],
        "support_form_id": 1784471218363829,
        "support_form_hidden_fields": "{}",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi",
        "__csr": "",
        "__req": "6",
        "__hs": "18952.BP:DEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1004765091,
        "__s": "swgf8j:uclfkr:ae3gvc",
        "__hsi": "7032938682445430338-0",
        "__comet_req": "0",
        "__spin_r": 1004765091,
        "__spin_b": "trunk",
        "__spin_t": 1637483640
    }
    return plusservice(LINK, data, head)
def mod4plus():
    driver = chrome()
    driver.get("https://www.google.com/search?q=data+instagram+download")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div/div/div[1]/div/a"))).click()
    sleep(2)
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH,
             "/html/body/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div[1]/div/div"))).click()
    except:
        pass


    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/span/div[13]/span/a"))).click()  # cookie

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]"))).click()  # cookie
    except:
        pass
    sleep(2)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/div[2]/label[1]"))).click()  # accesso dati
    sleep(2)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/div[5]/label[1]"))).click()  # op 4
    sleep(1)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[17]/input"))).send_keys(nomis[k])
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[18]/input"))).send_keys(user[k])
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[20]/input"))).send_keys(maill[k])
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[19]/select"))).send_keys(paese)
    for _ in range(1):
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/div[22]/div[2]/label[1]"))).click()
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/form/button"))).click()
    sleep(10)
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
                  EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/nav/div/div[1]/div/div[1]/div/div/div/div/div/div/span/span/div/div/div[1]/div[2]/div[1]/div/div")))
            break
        except:
            pass
    driver.delete_all_cookies()
    driver.quit()

def mod5xxplus():

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {

        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Length": "616",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "help.instagram.com",
        "Origin": "https://help.instagram.com",
        "Referer": "https://help.instagram.com/contact/402592967178996",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "X-FB-LSD": "AVqvX1spGOI",
    }
    data = {
        "jazoest":2969,
        "lsd":"AVqvX1spGOI",
        "name":nomis[k],
        "igid":user[k],
        "email":maill[k],
        "Field236858559849125_iso2_country_code":"",
        "Field236858559849125":"United States",
        "user_comment":text[k],
        "support_form_id":402592967178996,
        "support_form_hidden_fields":"%7B%7D",
        "support_form_fact_false_fields":"[]",
        "__user":0,
        "__a":1,
        "__dyn":"7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo",
        "__csr":"",
        "__req":5,
        "__hs":"19025.BP%3ADEFAULT.2.0.0.0.",
        "dpr":1,
        "__ccg":"EXCELLENT",
        "__rev":1005013657,
        "__s":"ry449m%3Aqx9t52%3Ambov8",
        "__hsi":"7060238005726563469-0",
        "__comet_req":0,
        "__spin_r":1005013657,
        "__spin_b":"trunk",
        "__spin_t":1643839758,
    }
    return plusservice(LINK, data, head)
def mod5xxxplus():

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {

        "Host": "help.instagram.com",
        "Connection": "close",
        "Content-Length": "628",
        "X-FB-LSD": "AVpcOUA_xtU",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": '"https://help.instagram.com"',
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": 'https://help.instagram.com/contact/402592967178996',
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",



    }
    data = {"jazoest": 21007,
            "lsd": "AVpcOUA_xtU",
            "name": nomis[k],
            "igid": user[k],
            "email": maill[k],
            "Field236858559849125_iso2_country_code": "US",
            "Field236858559849125": "Stati%20Uniti",
            "user_comment": text[k],
            "support_form_id": 402592967178996,
            "support_form_hidden_fields": "%7B%7D",
            "support_form_fact_false_fields": "[]",
            "__user": 0,
            "__a": 1,
            "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo",
            "__csr": "",
            "__req": 6,
            "__hs": "19066.BP%3ADEFAULT.2.0.0.0.",
            "dpr": 1,
            "__ccg": "EXCELLENT",
            "__rev": 1005197686,
            "__s": "ksojyp%3Adubj8r%3Aftrsqo",
            "__hsi": "7075387930689867746-0",
            "__comet_req": 0,
            "__spin_r": 1005197686,
            "__spin_b": "trunk",
            "__spin_t": 1647367126

            }
    return plusservice(LINK, data, head)
def modcopyplus():

    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    data ={
        "jazoest": 2985,
        "lsd": "AVpcOUA_dXo",
        "acknowledge": "I%20understand%20and%20wish%20to%20continue.",
        "your_name": nomis[k],
        "email": maill[k],
        "instagram_username": user[k],
        "Field2004892743057041": text[k],
        "Field389435238140162[0]": "--",
        "electronic_signature": str(nomis[k]).replace(" ",""),
        "support_form_id": 437908793443074,
        "support_form_hidden_fields": "%7B%222217965951821062%22%3Afalse%2C%22389435238140162%22%3Afalse%2C%221577725542288809%22%3Afalse%2C%22240094270012923%22%3Afalse%2C%22347202659379010%22%3Afalse%2C%22524532294666477%22%3Afalse%2C%221968124449913407%22%3Afalse%2C%222004892743057041%22%3Afalse%2C%221522459831126825%22%3Afalse%2C%22255680768287361%22%3Afalse%2C%222811762515517276%22%3Afalse%2C%22543115736141733%22%3Afalse%7D",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo",
        "__csr": "",
        "__req": 7,
        "__hs": "19066.BP%3ADEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": "1005197686",
        "__s": "nlfafi%3Adubj8r%3Asf3ao6",
        "__hsi": "7075399151103101537-0",
        "__comet_req": 0,
        "__spin_r": 1005197686,
        "__spin_b": "trunk",
        "__spin_t": 1647369738



    }
    head = {
        "Host": "help.instagram.com",
        "Connection": "close",
        "Content-Length": "1079",
        "X-FB-LSD": "AVpcOUA_dXo",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://help.instagram.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://help.instagram.com/contact/437908793443074",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",

    }
    return plusservice(LINK, data, head)
def mod6xxplus():
    LINK = "https://help.instagram.com/ajax/help/contact/submit/page"
    head = {
        "Host": "help.instagram.com",
        "Connection": "close",
        "Content-Length": "600",
        "X-FB-LSD": "AVr518P5-CU",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://help.instagram.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://help.instagram.com/contact/513098328818064",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",

    }
    data = {
        "jazoest": 2753,
        "lsd": "AVr518P5-CU",
        "Field274974709205675": nomis[k],
        "inputReportedUsername": user[k],
        "emailaddress": maill[k],
        "Field219374698146202": text[k],
        "support_form_id": 513098328818064,
        "support_form_hidden_fields": "%7B%7D",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa81Vrzo5-0jx0Fwww6DwtU6e0D83mwaS0zE5W0PU1AEG0hi0Lo6-",
        "__csr": "",
        "__req": 5,
        "__hs": "19086.BP%3ADEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1005290945,
        "__s": "sjx43j%3Avcb6nn%3Auvx8d9",
        "__hsi": "7082785685456143450-0",
        "__comet_req": 0,
        "__spin_r": 1005290945,
        "__spin_b": "trunk",
        "__spin_t": 1649089550,
    }
    return plusservice(LINK, data, head)
def mod8plus():

    LINK = "https://www.facebook.com/ajax/help/contact/submit/page"
    head = {


        "Host": "www.facebook.com",
        "Connection": "close",
        "Content-Length": "577",
        "X-FB-LSD": "AVpHs6c27Ks",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "*/*",
        "Origin": "https://www.facebook.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.facebook.com/help/instagram/contact/606967319425038",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",

    }
    data = {
        "jazoest": "2888",
        "lsd": "AVo0u-U1VUo",
        "name": nomis[k],
        "email": maill[k],
        "instagram_username": user[k],
        "mobile_number": phonis[k],
        "appeal_reason": text[k],
        "support_form_id": 606967319425038,
        "support_form_hidden_fields": "{}",
        "support_form_fact_false_fields": "[]",
        "__user": 0,
        "__a": 1,
        "__dyn": "7xe6Fo4OQ1PyUbFuC1swgE98nwgU6C7UW8xi642-7E2vwXx60kO4o3Bw5VCwjE3awbG782Cwooa87i0n2US1vw4Ugao884y0lW1TwoU2swdq0Ho2ewnE3fw5rwSyE158",
        "__csr": "",
        "__req": "7",
        "__hs": "18966.BP:DEFAULT.2.0.0.0.",
        "dpr": 1,
        "__ccg": "EXCELLENT",
        "__rev": 1004812321,
        "__s": "tdriw4:s0bcv8:zoodcc",
        "__hsi": "7038207081874181769-0",
        "__comet_req": 0,
        "__spin_r": 1004812321,
        "__spin_b": "trunk",
        "__spin_t": 1638710285


    }
    return plusservice(LINK, data, head)
def modfbplus():

    global k, txt, send, modplus
    send = True
    txt = ""
    url = "https://m.facebook.com/a/help/contact_us/"
    data = {
        "lsd": "AVoAWXZbRaI",
        "jazoest": 2942,
        "name": nomis[k],
        "email": maill[k],
        "instagram_username": user[k],
        "mobile_number": phonis[k],
        "appeal_reason": text[k],
        "form_id": "606967319425038",
        "support_form_hidden_fields": "{}",
        "support_form_fact_false_fields": "[]"
    }
    r = requests.session()
    req = r.get("https://m.facebook.com/help/contact/606967319425038")
    session_cookies = req.cookies
    cookies_dictionary = session_cookies.get_dict()
    cookie = str(cookies_dictionary).split("'")
    head = {

        "Host": "m.facebook.com",
        "Connection": "close",
        "Content-Length": "1098",
        # "Cache-Control": "max-age=0",
        "sec-ch-ua-mobile": "?0",
        # "Upgrade-Insecure-Requests": "1",
        "Origin": "https://m.facebook.com",
        # "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary1HD2UvOfWh5mxwy2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://m.facebook.com/help/contact/606967319425038",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.5",
        "Cookie": "datr=" + cookie[3]
    }
    if verprox:
        proxies = {
            'http': 'http://' + proxi,
            'https': 'http://' + proxi
        }

        req = r.post(url, data=data, headers=head, timeout=10, proxies=proxies)
    else:
        r = requests.session()
        req = r.post(url, data=data, headers=head, timeout=10)
    #print(req.text)
    print(Fore.LIGHTYELLOW_EX + "[STARUS CODE]" + Style.RESET_ALL, req.status_code)
    if "We need you to provide a valid email address, so our support team can contact you." in req.text:
        txt += ", INVALID EMAIL"
        send = False
    if "We cannot find record of User ID that you entered." in req.text:
        txt += ", INVALID ID"
        message("@" + user[k] + ' ID NON ESISTENTE ')
        send = False
    if "Go to Instagram and confirm it&#039;s you before requesting a review." in req.text:
        txt += ", MOD 1 BLOCKED"
        message("@" + user[k] + ' MOD1 BLOCCATO')
        send = False
    if "There was a problem with this request. We're working on getting it fixed as soon as we can." in req.text:
        txt += ", MOD 5 XX PROBLEMA DI RICHIESTA"
        send = False
    if "The username or short-link you provided does not belong to an inactive Instagram Account." in req.text:
        message("https://instagram.com/" + user[k] + ' RESTORED')
        txt += ", ACCOUNT !!!! ATTIVO UNBANED !!!!"
        send = False
    if "We limit how often you can post, comment or do other things in a given amount of time in order to help protect the community from spam." in req.text:
        txt += ", BLOCCATO PER SPAM"
        message("@" + user[k] + ' BLOCCATO PER SPAM')
        send = False
    if "A confirmation is required before you can proceed." in req.text:
        txt += ", CONFRIM UNKNOW ERROR"
        message("@" + user[k] + ' CONFRIM UNKNOW ERROR')
        send = False
    if "We could not process your request. Please try again later." in req.text:
        txt += ", ELIMINAZIONE IN CORSO"
        message("@" + user[k] + ' ELIMINAZIONE IN CORSO')
        send = False
    return send
def mod(user, tempo):
    try:
        global txt, k, send,modplus,righe,nomefile, motind, indmotper, contindmot, mailind, indmailper, contindmail
        while True:
            b = 1
            k = 1
            while k < righe:



                send = True
                if str(modd1[k]).lower() == "nan" and str(modd2[k]).lower() == "nan" and str(
                        modd3[k]).lower() == "nan" and str(modd4[k]).lower() == "nan" and str(
                    modd5[k]).lower() == "nan" and str(modd6[k]).lower() == "nan" and str(modd7[k]).lower() == "nan":
                    pass
                else:
                    try:
                        text[k] = motind[k][indmotper[k]]
                        maill[k] = mailind[k][indmailper[k]]
                        if not indmotper[k] >= contindmot[k]:
                            indmotper[k] += 1
                        else:
                            indmotper[k] = 0

                        if not indmailper[k] >= contindmail[k]:
                            indmailper[k] += 1
                        else:
                            indmailper[k] = 0
                    except:
                        pass




                    try:
                        print("\n" + Fore.LIGHTCYAN_EX + "[SUMMARY]" + Style.RESET_ALL + " USER: @" + user[
                            k].upper() + Fore.LIGHTBLUE_EX + "\n[COUNT]" + Style.RESET_ALL, count[k])
                    except:
                        print("\n" + Fore.LIGHTCYAN_EX + "[SUMMARY]" + Style.RESET_ALL + " USER: @" + user[
                            k].upper())
                # mod1
                if str(modd1[k]).lower() == "x" or modd1[k] == 'X' or str(modd1[k]).lower() == str("xx").lower() or str(
                        modd1[k]).lower() == str("xxx").lower():
                    try:
                        modplus = 1 #mi serve per requests per fare differenza tra mod1 e 2
                        if str(modd1[k]).lower() == str("xx").lower():
                            send = modfbplus()
                        elif str(modd1[k]).lower() == str("xxx").lower():
                            send = mod8plus()
                        else:
                            send = mod1plus()
                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: @" + user[k].upper() + " MOD1 COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR :" + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: @" + user[k].upper() + " MOD1 MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except Exception as e:
                        print(e)
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + " CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD1 PER @" + user[k].upper() + " CHE SBANYOO NON RIESCE A GESTIRE")
                # mod2
                if str(modd2[k]).lower() == 'x' or str(modd2[k]).lower() == 'xx':
                    modplus = 2 #mi serve per requests per fare differenza tra mod1 e 2
                    try:
                        if str(modd2[k]).lower() == 'x':
                            send = mod2aplus()
                        else:
                            send = mod2bplus()


                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: @" + user[
                                    k].upper() + " MOD2 COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: @" + user[k].upper() + " MOD2 MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except Exception as e:
                            print(e)
                            print(
                                Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + " CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD2 PER @" + user[k].upper() + " CHE SBANYOO NON RIESCE A GESTIRE")
                # mod3
                if str(modd3[k]).lower() == 'x' or str(modd3[k]).lower() == 'xx':
                    try:

                        if str(modd3[k]).lower() == 'x':
                            send = mod3plus()
                        else:
                            send = mod3aplus()
                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: @" + user[k].upper() + " MOD3 COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: @" + user[
                                k].upper() + " MOD3 MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()

                        count[k] += 1
                    except Exception as e:
                        print(e)
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + " CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD3 PER @" +
                            user[k].upper() + " CHE SBANYOO NON RIESCE A GESTIRE")
                # mod4
                if str(modd4[k]).lower() == 'x' or modd4[k] == 'X':
                    try:

                        send = mod4plus()
                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: @" + user[
                                k].upper() + " MOD4 COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: @" + user[k].upper() + " MOD4 MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except Exception as e:
                        print(e)
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + " CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD4 PER @" +
                            user[k].upper() + " CHE SBANYOO NON RIESCE A GESTIRE")
                # mod5
                if str(modd5[k]).lower() == 'x' or str(modd5[k]).lower() == 'xx' or str(modd5[k]).lower() == 'xxx' :
                    try:
                        if str(modd5[k]).lower() == 'xx':
                            send = mod5xxplus()
                        elif str(modd5[k]).lower() == 'xxx':
                            send = mod5xxxplus()

                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: " + user[
                                k] + "MOD5 COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: " + user[k] + "MOD5 MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except Exception as e:
                        print(e)
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + ' CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD5 PER ' +
                            user[k] + ' CHE SBANYOO NON RIESCE A GESTIRE')
                # mod6
                if str(modd6[k]).lower() == "x" or str(modd6[k]).lower() == "xx":
                    """if str(path[k]) != "nan":
                        pass
                    else:
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + ' CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL AGE PER ' +
                            user[
                                k] + ' PER MANCANZA DI DATI CORETTI')"""
                    try:
                        'ANCORA IN LAVORAZIONE'
                        if str(modd6[k]).lower() == "x":
                            send = modcopyplus()
                        else:
                            send = mod6xxplus()
                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: " + user[
                                k] + "COPYRIGHT COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: " + user[
                                k] + "COPYRIGHT MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except:
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + ' CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL COPYRIGHT PER ' +
                            user[
                                k] + ' CHE SBANYOO NON RIESCE A GESTIRE')

                # mod7
                if str(modd7[k]) != "nan":
                    if str(path[k]) != "nan" and str(modd7[k]).lower() != "x":
                        try:
                            'ancora in lavorazione'
                            send = False
                            if send == False:
                                print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + " USER: " + user[
                                    k] + "AGE COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR : " + Fore.RED + txt[
                                                                                                                                 2:len(
                                                                                                                                     txt)])
                            else:
                                print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: " + user[
                                    k] + "AGE MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                            slept()
                            count[k] += 1
                        except :
                            print(
                                Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + ' CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL AGE PER ' +
                                user[
                                    k] + ' CHE SBANYOO NON RIESCE A GESTIRE')
                    else:
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + ' CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL AGE PER ' +
                            user[
                                k] + ' PER MANCANZA DI DATI CORETTI')
                b += 1
                k+=1
            message("CICLI DI MODULI SU TUTTE LE PAGE FATTO! ")
            sleep(tempoc)
            aggiornamentofile(nomefile)
    except Exception as e:
        print(e)
        print("bot error")
        try:
            if logins == "si":
                insta = login()
        except:
            pass
        message(" ERRORE BOT, BOT FERMO")
        quit()
def lettura(df):
    try:
        global username, password, msg, paese, tempo, tempoc, scelta, logins, cmb, proxi, nomepc,verprox,dati,prox, righe, motind, indmotper, contindmot, mailind, indmailper, contindmail
        cont = 1
        righe = df.shape[0]
        nomepc = df.iloc[0][1]
        msg = df.iloc[0][2]
        textmom = df.iloc[0][11]
        paese = df.iloc[0][12]
        tempo = int(df.iloc[0][13])
        tempoc = int(df.iloc[0][14])
        logins = (str(df.iloc[0][15])).lower()
        cmb = (str(df.iloc[0][16])).lower()
        try:
            prox = (str(df.iloc[0][17])).lower().split("@")
        except:
            pass
        if prox[0] != "nan":
            proxi = prox[1] + "@" + prox[0]
            verprox = True
        else:
            verprox = False
        if logins.lower() == "si":
            if logins.lower() == "si":
                nomefile1 = df.iloc[0][0]
                try:
                    file = open("/Users/PYTHONBOT/TELEGRAMDATA/" + nomefile1 + ".txt", "r")
                    linea = file.readline()
                    dati = linea.split(";")

                except:
                    print(Fore.LIGHTRED_EX + ' PROFILO INESISTENTE, NON SARA EFFETTUATO IL LOGIN' + Fore.LIGHTWHITE_EX)
                    logins = "no"
        for cont in range(1,righe):
            user[cont], nomis[cont], maill[cont], phonis[cont], modd1[cont], modd2[cont], modd3[cont], modd4[cont], \
            modd5[
                cont], modd6[cont], modd7[cont], path[cont], text[cont] = df.iloc[cont][0], df.iloc[cont][1], df.iloc[cont][
                2], phones(), df.iloc[cont][3], df.iloc[cont][4], df.iloc[cont][5], df.iloc[cont][6], df.iloc[cont][7], \
                                                              df.iloc[cont][8], df.iloc[cont][9], df.iloc[cont][10],df.iloc[cont][11]

            if str(text[cont]).lower() == "nan":
                text[cont] = textmom
            motind[cont] = text[cont].split(";")
            contindmot[cont] = len(motind[cont])
            indmotper[cont] = 0
            mailind[cont] = maill[cont].split(";")
            contindmail[cont] = len(mailind[cont])
            indmailper[cont] = 0


        scelta = righe

        print(Fore.LIGHTGREEN_EX + "\n\n[SUCCESS]" + Style.RESET_ALL + "RILETTURA ESEGUITA CORRETTAMENTE SENZA NESSUN ERRORE ")
    except:
        print(Fore.LIGHTGREEN_EX + "\n\n[FAILURE]" + Style.RESET_ALL + "RILETTURA NON ESEGUITA CORRETTAMENTE")
def aggiornamentofile(nomefile):
    global df
    try:
        df = pd.read_excel(nomefile)
        lettura(df)
    except:
        print('rilettura file fallita')
if __name__ == "__main__":
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '                    SBANYOO TK ' + Style.RESET_ALL)
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    global insta, client, nomefile, tentativi
    tentativi = 0
    modplus = 1
    init(convert=False)
    send = False
    df = None
    verprox = True
    txt = ""
    prox = ["nan", "nan"]
    count, nomis, user, maill, phonis, modd1, modd2, modd3, modd4, modd5, modd6, modd7, path, sban, dati, text, motind, indmotper, contindmot, mailind, indmailper, contindmail = {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}
    while True:
        try:
            try:
                nomefile = input( Fore.LIGHTGREEN_EX + "[INPUT FILE]" + Style.RESET_ALL + ' INSERISCI IL PERCORSO DEL FILE EXCEL: ').replace('"',"")
                if nomefile == "t" or nomefile=="":
                    nomefile = r"C:\PYTHONBOT\ACCOUNTABBANDONATI.xlsx"
                nomefile = nomefile.strip()
                df = pd.read_excel(nomefile.strip())
                break
            except Exception as e:
                print(e)
                print(Fore.LIGHTRED_EX + "[ERRORE]" + Style.RESET_ALL + ' FILE NON TROVATO')

        except Exception as e:
            print(Fore.LIGHTRED_EX + "[ERRORE]" + Style.RESET_ALL + '  - FILE NON TROVATO - ')
    # lettura
    cont = 1
    righe = df.shape[0]
    nomepc = df.iloc[0][1]
    msg = df.iloc[0][2]
    textmom = df.iloc[0][11]
    paese = df.iloc[0][12]
    tempo = int(df.iloc[0][13])
    tempoc = int(df.iloc[0][14])
    logins = (str(df.iloc[0][15])).lower()
    cmb = (str(df.iloc[0][16])).lower()
    try:
        prox = (str(df.iloc[0][17])).lower().split("@")

    except:
        pass
    if prox[0] != "nan":
        proxi = prox[1] + "@" + prox[0]
        verprox = True
    else:
        verprox = False
    if logins.lower() == "si":
        if logins.lower() == "si":
            nomefile1 = df.iloc[0][0]
            try:
                file = open("/Users/PYTHONBOT/TELEGRAMDATA/" + nomefile1 + ".txt", "r")
                linea = file.readline()
                dati = linea.split(";")

            except:
                print(Fore.LIGHTRED_EX + ' PROFILO INESISTENTE, NON SARA EFFETTUATO IL LOGIN' + Fore.LIGHTWHITE_EX)
                logins = "no"
    for cont in range(1,righe):
        user[cont], nomis[cont], maill[cont], phonis[cont], modd1[cont], modd2[cont], modd3[cont], modd4[cont], modd5[
            cont], modd6[cont], modd7[cont], path[cont], text[cont] = df.iloc[cont][0], df.iloc[cont][1], df.iloc[cont][
            2], phones(), df.iloc[cont][3], df.iloc[cont][4], df.iloc[cont][5], df.iloc[cont][6], df.iloc[cont][7],df.iloc[cont][8], df.iloc[cont][9], df.iloc[cont][10],df.iloc[cont][11]
        if str(text[cont]).lower() == "nan":
            text[cont] = textmom
        motind[cont] = text[cont].split(";")
        contindmot[cont] = len(motind[cont])
        indmotper[cont] = 0
        mailind[cont] = maill[cont].split(";")
        contindmail[cont] = len(mailind[cont])
        indmailper[cont] = 0




    scelta = righe

    for indice in range(1,righe-1):



        count[indice] = 1
        sban[indice] = 0

    # finelettura
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '                     RIEPILOGO' + Style.RESET_ALL)
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Nome pc: ' + Fore.RED + nomepc.upper())
    if logins.lower() == "si":
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Numero che manda lo status bot: ' + Fore.RED + str(dati[0]).upper())
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Il messaggio arriva a: ' + Fore.RED + msg.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Paese: ' + Fore.RED + paese.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Login Status: ' + Fore.RED + logins.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " SBAN METHOD: " + Fore.RED + "SBAN +")
    if prox[0] != "nan":
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " PROXY STATUS: " + Fore.RED + "ON")
    else:
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " PROXY STATUS: " + Fore.RED + "OFF")
    print(Fore.BLUE + "------------------------------------------------------\n" + Style.RESET_ALL)
    if logins == "si":
        insta = login()
    mod(user, tempo)