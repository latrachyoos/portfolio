import requests
from time import sleep

from art import tprint
from colorama import Fore

"""def click(path):
    f = 0
    while True:
        try:
            driver.find_element(By.XPATH, path).click()
            break
        except:
            f+=1
            if f == 30:
                break
def tabtxt(path, txt):
    f = 0
    while True:
        try:
            driver.find_element(By.XPATH, path).send_keys(txt)
            break
        except:
            f += 1
            if f == 30:
                break"""
# FIRMA REVISION
print(
    Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
print('                        BENVENUTO NEL BOT SBANYOO')
print(Fore.LIGHTWHITE_EX + '                          DEVOLPED BY LATRACHYOO')
print("--------------------------------------------------------------------------")
text = str(('          SBANYOO'))

str(Fore.LIGHTRED_EX + "" + str(tprint(text)))
text = ('               MOD FB')

stri = "latrachyoo devolpment sys"
print(Fore.LIGHTYELLOW_EX + "")
str(tprint(text))
print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
print(Fore.WHITE + '                                VERSIONE ', 5)
print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
name = input(" - name: ")
mail = input("- mail: ")
user = input("- user: ")
num = input("- number: ")
mot = input("- motivation: ")
while True:
    try:
        time = int(input("- sleep time in seconds: "))
        break
    except:
        print("- please write a number, thank you")
"""pathname = "/html/body/div[1]/div/div[3]/article/form/div[1]/div/div[2]/div[2]/div/div/input"
pathmail = "/html/body/div[1]/div/div[3]/article/form/div[1]/div/div[2]/div[3]/div/div/input"
pathuser = "/html/body/div[1]/div/div[3]/article/form/div[1]/div/div[2]/div[4]/div/div/input"
pathnum = "/html/body/div[1]/div/div[3]/article/form/div[1]/div/div[2]/div[5]/div/div/input"
pathmot = "/html/body/div[1]/div/div[3]/article/form/div[1]/div/div[2]/div[6]/div/div/textarea"
pathsend = "/html/body/div[1]/div/div[3]/article/form/div[2]/button"
pathcookie = "/html/body/div[1]/div/div[7]/div[1]/div/div[2]/div[3]/button"""



url = "https://m.facebook.com/help/contact/606967319425038"
"""driver = webdriver.Chrome()
driver.minimize_window()"""
k = 1


LINK = "https://m.facebook.com/a/help/contact_us/"
head = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Content-Length": "1311",
        "Content-Type": "multipart/form-data; boundary=---------------------------405972001617733653783408447109",
        "Host": "m.facebook.com",
        "Origin": "https://m.facebook.com",
        "Referer": "https://m.facebook.com/help/contact/606967319425038",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "TE": "trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
        # "X-FB-LSD": "AVo0u-U1VUo",
    }

data = {
        "lsd": "AVo0u-U1tOc",
        "jazoest": "2900",
        "name": name,
        "email": mail,
        "instagram_username": user,
        "mobile_number": num,
        "appeal_reason": mot,
        "form_id": 606967319425038,
        "support_form_hidden_fields": "{}",
        "support_form_fact_false_fields": "[]",
    }

r = requests.session()



while True:
    req = r.post(LINK, data=data, headers=head, timeout=10)
    if req.status_code == 200:
        print(k, "modules sended to: " + user)
        k +=1

    else:
        print("module for: " + user + " didn't sended")
    sleep(time)

