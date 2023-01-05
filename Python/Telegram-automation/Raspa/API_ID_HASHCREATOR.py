import subprocess

import pyautogui as py
import pyperclip
import pyautogui
import telethon
from bs4 import BeautifulSoup
from lxml import etree
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import random,string,requests,shutil,os
from time import sleep
global cookie,hashrequests,r, api_id,hash
try:
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt","r")
    tgfather = str(file.readline())
    file.close()
except:
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt", "r")
    file.write(input("-name tggroupfather: "))
    file.close()
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt", "r")
    tgfather = str(file.readline())
    file.close()
groupdad = tgfather
contatore = 0
def txtmode():
    global cookie,hashrequests,r, api_id,hash, i
    try:
        file = open(r"C:\RASPAYOO\accdata\last.txt", "r")
        num = int(file.read())
        file.close()
    except:
        file = open(r"C:\RASPAYOO\accdata\last.txt", "w")
        file.write(str(1))
        file.close()
        file = open(r"C:\RASPAYOO\accdata\last.txt", "r")
        num = int(file.read())
        file.close()
    file = open(r"C:\RASPAYOO\accdata\last.txt", "w")
    file.write(str(num + 1))
    file.close()
    file = open(r"C:\RASPAYOO\accdata\acc" + str(num + 1) + ".txt", "w")
    file.write(i + ";" + api_id + ";" + hash)
    file.close()
    file = open(r"C:\RASPAYOO\accdata\acc" + str(num + 1) + ".txt", "w")
    file.write(i + ";" + api_id + ";" + hash)
    file.close()
    client(JoinChannelRequest(groupdad))
    client.send_message(groupdad, "Hello i'm " + i)
    os.remove("G:\\tgdatabase\\" + a + "\\notregistred.txt")
    file = open("G:\\tgdatabase\\"+a+"\\acc" + str(num + 1) + ".txt", "w")
    file.write(i + ";" + api_id + ";" + hash)
    file.close()
    FNULL = open(os.devnull, 'w')                                  
    subprocess.call("TASKKILL /F /IM telegram.exe", stdout=FNULL)
    print("[-] PROCCESSO COMPLETATO PER: " + i)
    sleep(75)
def logall():
    global cookie,hashrequests,r, api_id,hash,contatore,vecchia, i,a
    FNULL = open(os.devnull, 'w')
    subprocess.call("TASKKILL /F /IM telegram.exe", stdout=FNULL)
    sleep(2)
    for _ in range(20):
        try:
            shutil.rmtree(r"G:\\tgdatabase\randomaccess\tdata")
        except:
            subprocess.call("TASKKILL /F /IM telegram.exe", stdout=FNULL)
    try:
        shutil.copytree("G:\\tgdatabase\\" + a + "\\tdata",
                        "G:\\tgdatabase\\randomaccess\\tdata")
    except:
        print("tdata")
    os.system("cmd /c start G:\\tgdatabase\\randomaccess\\Telegram.exe")
    sleep(5)


    log = False
    verificalogin = False
    contatorelogin = 0
    while not log:
        if vecchia != ("["+str(contatore)+"/"+str(len(my_list))+"] "+ i):
            print("\n["+str(contatore)+"/"+str(len(my_list))+"] "+ i)
        vecchia = ("["+str(contatore)+"/"+str(len(my_list))+"] "+ i)
        head = {
            "Host": "my.telegram.org",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Length": "21",
            "Origin": "https://my.telegram.org",
            "Connection": "keep-alive",
            "Referer": "https://my.telegram.org/auth",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers",
        }
        data = {
            "phone": i,
        }
        link = "https://my.telegram.org/auth/send_password"
        r = requests.session()
        req = r.post(link, data=data, headers=head, proxies=proxies) #invio del codice
        print(req.text)

        try:

            texto = req.text.split(":")
            texto = texto[1].split('"')
            sleep(1)
            #random hash ottenuto
            req = r.post(link, data=data, headers=head, proxies=proxies)  # invio del codice
            print(req.text)
            print(req.text)
            texto = req.text.split(":")
            texto = texto[1].split('"')
            sleep(10)
            pyautogui.click(x=310, y=95)
            sleep(30)
            pyautogui.click(x=369, y=433)
            for _ in range(10):
                py.scroll(-70)
            sleep(5)
            pyautogui.click(x=263, y=264, button="right")
            sleep(2)
            pyautogui.click(x=377, y=347, button="left")








            texti = pyperclip.paste()
            codice = texti.split(" ")
            codice = codice[23].split("\n")
            code = codice[1]
            code = code.replace(" ","").replace("\n","")
            print(code)
            sleep(1)

            link = "https://my.telegram.org/auth/login"
            data = {
                "phone": i,
                "random_hash": texto[1],
                "password": code,
            }
            head = {
                "Host": "my.telegram.org",
                "Connection": "close",
                "Content-Length": "73",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://my.telegram.org",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://my.telegram.org/auth",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",

            }
            req = requests.post(link, data=data, headers=head, proxies=proxies) #incollare il codice
            print(req.text)
            if req.text != "Invalid confirmation code!": #verifico se il codice si agiusto
                link = "https://my.telegram.org/apps"
                head = {
                    "Host": "my.telegram.org",
                    "Connection": "close",
                    "sec-ch-ua-mobile": "?0",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-User": "?1",
                    "Sec-Fetch-Dest": "document",
                    "Referer": "https://my.telegram.org/",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                }
                re = r.post(link, headers=head, proxies=proxies) #ottengo i cookie
                try:
                    session_cookies = req.cookies
                    cookies_dictionary = session_cookies.get_dict()
                    cookie = str(cookies_dictionary).split("'")
                    cookie = cookie[3]
                    cookie = "stel_token=" + cookie
                    contatorelogin = 0
                    log = True
                    verificalogin = True
                except:
                    contatorelogin +=1
                    if contatorelogin == 5:
                        log = False
                        verificalogin = False
                    log = False
        except:
            try:
                head = {
                    "Host": "my.telegram.org",
                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Length": "21",
                    "Origin": "https://my.telegram.org",
                    "Connection": "keep-alive",
                    "Referer": "https://my.telegram.org/auth",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "same-origin",
                    "TE": "trailers",
                }

                data = {
                    "phone": "+1" + str(a),
                }
                link = "https://my.telegram.org/auth/send_password"
                r = requests.session()
                req = r.post(link, data=data, headers=head, proxies=proxies)  # invio del codice
                print(req.text)

                try:
                    texto = req.text.split(":")
                    texto = texto[1].split('"')
                    sleep(1)
                    # random hash ottenuto

                    req = r.post(link, data=data, headers=head, proxies=proxies)  # invio del codice
                    print(req.text)

                    texto = req.text.split(":")
                    texto = texto[1].split('"')
                    sleep(10)
                    pyautogui.click(x=310, y=95)

                    sleep(30)
                    pyautogui.click(x=369, y=433)
                    for _ in range(10):
                        py.scroll(-70)
                    sleep(5)
                    pyautogui.click(x=263, y=264, button="right")
                    sleep(2)
                    pyautogui.click(x=377, y=347, button="left")
                    pyautogui.click(x=10, y=10, button="right")
                    pyautogui.click(x=10, y=10, button="right")




                    texti = pyperclip.paste()
                    codice = texti.split(" ")
                    codice = codice[23].split("\n")
                    code = codice[1]
                    code = code.replace(" ", "").replace("\n", "")
                    print(code)
                    sleep(1)

                    link = "https://my.telegram.org/auth/login"
                    data = {
                        "phone": i,
                        "random_hash": texto[1],
                        "password": code,
                    }
                    head = {
                        "Host": "my.telegram.org",
                        "Connection": "close",
                        "Content-Length": "73",
                        "Accept": "application/json, text/javascript, */*; q=0.01",
                        "X-Requested-With": "XMLHttpRequest",
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Origin": "https://my.telegram.org",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Dest": "empty",
                        "Referer": "https://my.telegram.org/auth",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",

                    }
                    req = requests.post(link, data=data, headers=head, proxies=proxies)  # incollare il codice
                    print(req.text)

                    if req.text != "Invalid confirmation code!":  # verifico se il codice si agiusto
                        link = "https://my.telegram.org/apps"
                        head = {
                            "Host": "my.telegram.org",
                            "Connection": "close",
                            "sec-ch-ua-mobile": "?0",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                            "Sec-Fetch-Site": "same-origin",
                            "Sec-Fetch-Mode": "navigate",
                            "Sec-Fetch-User": "?1",
                            "Sec-Fetch-Dest": "document",
                            "Referer": "https://my.telegram.org/",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                        }
                        re = r.post(link, headers=head, proxies=proxies)  # ottengo i cookie
                        print(re.text)
                        try:
                            session_cookies = req.cookies
                            cookies_dictionary = session_cookies.get_dict()
                            cookie = str(cookies_dictionary).split("'")
                            cookie = cookie[3]
                            cookie = "stel_token=" + cookie
                            contatorelogin = 0
                            log = True
                            verificalogin = True
                        except:
                            contatorelogin += 1
                            if contatorelogin == 5:
                                log = False
                                verificalogin = False
                            log = False
                except:
                    print(req.text)
                    print("[-] Contatto in spam!")
                    verificalogin = False
                    log = True


            except:
                print(req.text)
                print("[-] Contatto in spam!")
                verificalogin = False
                log = True


    return verificalogin
#proxi = "4k81j:rci9l8e5@169.197.83.74:6052"
"""proxies = {
            'http': 'http://' + proxi,
            'https': 'http://' + proxi
        }"""
proxies = {
  'http': 'http://xhyc3:qnzy5p30@169.197.83.74:6024',
  'https': 'http://xhyc3:qnzy5p30@169.197.83.74:6024'
}

my_list = os.listdir(r"G:\tgdatabase")
vecchia = ""

for a in my_list:


    global cookie,hashrequests,r, api_id,hash,code, i

    i = a
    p = 0
    try:
        contatore+=1
        if os.path.exists("G:\\tgdatabase\\"+a+"\\notregistred.txt") and not os.path.exists("G:\\tgdatabase\\" + a + "\\pwreq.txt"): #or os.path.exists("G:\\tgdatabase"+i+"\\hashnonottenuto.txt"):
            try:
                if logall(): #cookie ottenuti
                    continues = False
                    link = "https://my.telegram.org/apps"
                    head = {
                        "Host": "my.telegram.org",
                        "Connection": "close",
                        "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
                        "sec-ch-ua-mobile": "?0",
                        "Upgrade-Insecure-Requests": "1",
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "Sec-Fetch-Site": "same-origin",
                        "Sec-Fetch-Mode": "navigate",
                        "Sec-Fetch-User": "?1",
                        "Sec-Fetch-Dest": "document",
                        "Referer": "https://my.telegram.org/",
                        "Accept-Encoding": "gzip, deflate",
                        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                        "Cookie": cookie
                    }
                    req = r.post(link, headers=head, proxies=proxies)
                    print(req.text)
                    soup = BeautifulSoup(req.text, 'html.parser')
                    dom = etree.HTML(str(soup))
                    hashrequests = str(dom.xpath('/html/body/div[2]/div[2]/div/div/form/input')[0].attrib['value'])
                    try:
                        soup = BeautifulSoup(req.text, 'html.parser')
                        dom = etree.HTML(str(soup))
                        api_id = str(dom.xpath('/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/span/strong')[0].text)
                        hash = str(dom.xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[1]/span')[0].text)
                        #print("[-] api_id e hash ottenuti")
                        continues =True
                    except:
                        l = 0
                        while True:

                            all = string.ascii_letters
                            name = "".join(random.sample(all, int(random.randint(15, 20))))
                            shortname = "".join(random.sample(all, 12))
                            link = "https://my.telegram.org/apps/create"
                            head = {
                                "Host": "my.telegram.org",
                                "Connection": "close",
                                "Accept": "*/*",
                                "X-Requested-With": "XMLHttpRequest",
                                "sec-ch-ua-mobile": "?0",
                                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                                "Origin": "https://my.telegram.org",
                                "Sec-Fetch-Site": "same-origin",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Dest": "empty",
                                "Referer": "https://my.telegram.org/apps",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                                "Cookie": cookie,
                            }
                            data = {
                                "hash": hashrequests,
                                "app_title": str(name),
                                "app_shortname": str(shortname),
                                "app_url": "https://" + hashrequests + name +".com",
                                "app_platform": "desktop",
                                "app_desc": "hello world " + hashrequests,

                            }
                            #print(hashrequests)
                            reqspecial = r.post(link, data=data, headers=head, proxies=proxies)
                            sleep(5)
                            print(reqspecial)
                            try:
                                link = "https://my.telegram.org/apps"
                                head = {
                                    "Host": "my.telegram.org",
                                    "Connection": "close",
                                    "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
                                    "sec-ch-ua-mobile": "?0",
                                    "Upgrade-Insecure-Requests": "1",
                                    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                    "Sec-Fetch-Site": "same-origin",
                                    "Sec-Fetch-Mode": "navigate",
                                    "Sec-Fetch-User": "?1",
                                    "Sec-Fetch-Dest": "document",
                                    "Referer": "https://my.telegram.org/",
                                    "Accept-Encoding": "gzip, deflate",
                                    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                                    "Cookie": cookie
                                }
                                req = r.post(link, headers=head, proxies=proxies)
                                print(req.text)
                                soup = BeautifulSoup(req.text, 'html.parser')
                                dom = etree.HTML(str(soup))
                                api_id = str(
                                    dom.xpath('/html/body/div[2]/div[2]/div/div/form/div[1]/div[1]/span/strong')[
                                        0].text)
                                hash = str(
                                    dom.xpath('/html/body/div[2]/div[2]/div/div/form/div[2]/div[1]/span')[0].text)
                                #print("[-] api_id e hash ottenuti")
                                l = 0
                                continues = True
                                print(req.text)
                                break
                            except:
                                #print("[-] api_id e hash non ottenuti, tentativo: " + str(l) + " | 6")
                                l +=1
                                if l < 7:
                                    if logall() == False:
                                        l = 7

                                    link = "https://my.telegram.org/apps"
                                    head = {
                                                "Host": "my.telegram.org",
                                                "Connection": "close",
                                                "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
                                                "sec-ch-ua-mobile": "?0",
                                                "Upgrade-Insecure-Requests": "1",
                                                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
                                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                                "Sec-Fetch-Site": "same-origin",
                                                "Sec-Fetch-Mode": "navigate",
                                                "Sec-Fetch-User": "?1",
                                                "Sec-Fetch-Dest": "document",
                                                "Referer": "https://my.telegram.org/",
                                                "Accept-Encoding": "gzip, deflate",
                                                "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                                                "Cookie": cookie
                                            }
                                    req = r.post(link, headers=head, proxies=proxies)
                                    print(req.text)
                                    soup = BeautifulSoup(req.text, 'html.parser')
                                    dom = etree.HTML(str(soup))
                                    hashrequests = str(dom.xpath('/html/body/div[2]/div[2]/div/div/form/input')[0].attrib['value'])
                                    print(hashrequests)
                                    #print(hashrequests)
                                else:
                                    continues = False
                                    file = open("G:\\tgdatabase\\"+a+"\\hashnonottenuto.txt", "w")
                                    #print("[-] hash non ottenuto")
                                    file.close()
                                    l = 0
                                    break

                    if continues:
                        r.close()
                        client = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + i, api_id, hash)
                        client.connect()
                        if not client.is_user_authorized():
                            try:
                                client.send_code_request(i)
                                sleep(10)
                                pyautogui.click(x=369, y=433)
                                for _ in range(10):
                                    py.scroll(-70)
                                sleep(1)
                                pyautogui.click(x=278, y=292,button="right")
                                sleep(2)
                                pyautogui.click(x=355, y=384, button="left")


                                texti = pyperclip.paste()
                                texti = texti.split(" ")
                                code = texti[3].replace(".", "")
                                print(code)
                                client.sign_in(i, code)
                                txtmode()
                            except telethon.errors.SessionPasswordNeededError:
                                file = open("G:\\tgdatabase\\" + a + "\\pwreq.txt", "w")
                                file.close()
                                print("[-] PASSWORD REQUERED")
                            except telethon.errors.rpcerrorlist.PhoneCodeInvalidError:
                                print("[-] CODICE ERRATO")

                        else:
                            txtmode()
            except Exception as e:
                print("[-] HAS OCCURED A ERROR")
                try:
                    file = open("G:\\tgdatabase\\" + a + "\\recheck.txt", "w")
                    file.write(str(e))
                except:pass
                print(e)
                file.close()
    except Exception as e:
        print(e)



