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

FNULL = open(os.devnull, 'w')
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
proxies = {
  'http': 'http://xhyc3:qnzy5p30@169.197.83.74:6024',
  'https': 'http://xhyc3:qnzy5p30@169.197.83.74:6024'
}

my_list = os.listdir(r"G:\tgdatabase")


def logall():
    pass


for number in my_list:
    if os.path.exists("G:\\tgdatabase\\"+number+"\\notregistred.txt"):
        for _ in range(10):
            try:
                shutil.rmtree(r"G:\\tgdatabase\randomaccess\tdata")
                break
            except:
                subprocess.call("TASKKILL /F /IM telegram.exe", stdout=FNULL)
        try:
            shutil.copytree("G:\\tgdatabase\\" + number + "\\tdata",
                            "G:\\tgdatabase\\randomaccess\\tdata")
        except:
            print("tdata")
        os.system("cmd /c start G:\\tgdatabase\\randomaccess\\Telegram.exe")
        sleep(2)

        for _ in range(5):
            try:
                link = "https://my.telegram.org/auth/send_password"
                head ={
                    "Host": "my.telegram.org",
                    "Connection": "close",
                    "Content-Length": "20",
                    "sec-ch-ua": '";Not A Brand";v="99", "Chromium";v="88"',
                    "Accept": "application/json, text/javascript, */*; q=0.01",
                    "X-Requested-With": "XMLHttpRequest",
                    "sec-ch-ua-mobile": "?0",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://my.telegram.org",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://my.telegram.org/auth",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
                }
                data={
                    "phone":number
                }

                r = requests.session()
                req = r.post(link,headers=head,data=data,proxies=proxies)

                try:
                    texto = req.text.split(":")
                    texto = texto[1].split('"')
                    sleep(5)
                    py.click(x=272, y=105)
                    req = r.post(link, headers=head, data=data, proxies=proxies)
                    texto = req.text.split(":")
                    texto = texto[1].split('"')
                    print(req.text)

                    pyautogui.click(x=310, y=95)
                    sleep(10)
                    pyautogui.click(x=369, y=433)
                    sleep(5)
                    pyautogui.click(x=263, y=264, button="right")
                    sleep(2)
                    pyautogui.click(x=377, y=347, button="left")
                    texti = pyperclip.paste()
                    codice = texti.split(" ")
                    codice = codice[23].split("\n")
                    code = codice[1]
                    code = code.replace(" ", "").replace("\n", "")
                    print(code)






                except:
                    pass

            except:
                pass



