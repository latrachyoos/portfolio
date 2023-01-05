if __name__=="__main__":
  print(" BENVENUTO NEL BOT DI KARIM LATRACH, QUA PUOI ACCETTARE LE RICHIESTE OPZIONE 1, INVIARE MODULI PER SBANNARE PAGINE OPZIONE 2 E BANNARE PAGINE (NON DISPONIBILE)")

  choice= input("SCEGLI: \n - SE VUOI   ACCETTARE LE RICHIESTE SCHIACCIA(1)\n - SE VUOI MANDARE MODULI PER SBAN SCHIACCIA (2): ")
  
  if choice=="1":
      import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver= webdriver.Chrome(".\chromedriver.exe")

def username():
    username= str(input("Inserisci username--> "))

    u=open("username.txt", "w")
    u.write(username)
    u.close()

def password():
    password= str(input("Inserisci Password--> "))

    p=open("password.txt", "w")
    p.write(password)
    p.close()

def start(user, passw):

    driver.delete_all_cookies()
    driver.get("https://www.instagram.com")

    myElem = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.NAME , 'username')))

    u= driver.find_element_by_name("username")
    u.clear()
    u.click()
    u.send_keys(user)

    p= driver.find_element_by_name("password")
    p.clear()
    p.click()
    p.send_keys(passw)
    p.send_keys(Keys.ENTER)
#_0ZPOP kIKUG

if __name__=="__main__":

    a= str(input("Vuoi usare credenziali gia' usate in precedenza?(y/n) "))
    if a=="n" or a=="N":
        username()
        password()

    password=open("password.txt", "r")
    password=str(password.read())

    username=open("username.txt", "r")
    username=str(username.read())

    start(username, password)
    sleep(5)
    #myElem = WebDriverWait(driver, 999).until(EC.presence_of_element_located((By.CLASS_NAME , 'aOOlW.HoLwm')))

    try:
        pi=driver.find_element_by_class_name("aOOlW.HoLwm")
        pi.click()
    except selenium.common.exceptions.NoSuchElementException:
        print("")

    #driver.get("https://www.instagram.com/accounts/activity")
     #sleep(3)
    driver.get("https://www.instagram.com/accounts/activity")
    while True:
        try:
            #myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME , 'PUHRj.eKc9b.H_sJK')))
            sleep(3)
            a=driver.find_element_by_class_name("PUHRj.eKc9b.H_sJK")
            a.click()

            #myElem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME , 'sqdOP.L3NKy.y3zKF')))
            try:
                sleep(2)
                driver.execute_script("""var i; for(i=0; i<20; i++){var a=document.querySelector(".sqdOP.L3NKy.y3zKF"); if(a.textContent=="Conferma"){a.click(); a.remove();}else{a.remove();}}""")
                sleep(4)
                #bb=driver.find_element_by_xpath("//*[text()='Conferma']")
                #bb.click()
                driver.get("https://www.instagram.com/accounts/activity")
            except:
                a=1
                driver.refresh()
                #continue

            #driver.refresh()
            #driver.delete_all_cookies()
        except selenium.common.exceptions.NoSuchElementException:
            a=1
            #print("")
if choice=="2": 
#developed by @Karim Latrach for personal use
#18/03/2020
#follow me on ig @latrachyoo and @spaccianotty
 from selenium import webdriver
 import time
 import random
 import string
 import os
 from selenium.webdriver.chrome.options import Options
#boolean ran= True;

choice=2

def mails():

    mail=""
    value=random.randint(5,15)
    dizio= {1: 'a', 3: 'c', 2: 'b', 5: 'e', 4: 'd', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j', 13: 'm', 12: 'l', 15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't', 23: 'w', 22: 'v', 25: 'y', 24: 'x', 26: 'z'}
    for i in range(0,value):
        x=dizio[random.randint(1,26)]
        mail+=x
    mail+="@gmail.com"
    return mail 

def phones():

    number="+393"
    for i in range(0,9):
        number+=str(random.randint(0,9))
    return number

def countProxy():
    ck=0
    f= open("proxyList.txt","r+")
    for line in f:
        for letter in line:
            if letter==";":
                ck=ck+1
    f.close() 
    return ck

def getProxy(num):
    f= open("proxyList.txt","r+")
    ck=0;
    for line in f:
        if ck==num:
            proxy=line
            break
        else:
            ck+=1
    proxy=proxy[:-1]
    f.close()
    print(proxy)
    return proxy

def delete(num):
    f= open("proxyList1.txt","r+")
    f1=open("proxyList.txt","w+")
    ck=0;
    for line in f:
        if ck==num:
            ck+=1
        else:
            f1.write(line)
            ck+=1
    f.close()
    f1.close()

def sendRequest(name,username,text,mail,phone):

        sent=0
        num=0
        #num1=countProxy()
        print ("MODULO INVIATO NUMERO: ",sent)
        driver = webdriver.Chrome()
        #name='karim latrach'
        #username='spaccianotty'
        #text= 'Hi, I was working with an influencer marketing agency. I closed the contract and strangely my account was deactivated. I am afraid it is a kind of revenge of the agency. Please help me recover the account.I am desperate and I do not know how. I hope your fantastic support team can help me.I wish you a good job.'
        url = 'https://help.instagram.com/contact/606967319425038'
        ck=0
        pausa=0
        #print(countProxy())
        fact=False
        this=True
        while True:
            driver.refresh()
            driver.delete_all_cookies()
            if pausa==1:
                print("MODULO INVIATO CORETTAMENTE, TEMPO ATTESA PER IL PROSSIMO MODULO: 2.30 MIN \n")
                time.sleep(144)
                print("PREPARAZIONE DELL'INVIO DEL MODULO \n")
                pausa=0
            pausa+=1
            if choice=="1":
                mail=mails()
                phone=phones()
            if ck==1 and fact==True and this==True:
                driver.quit()
                fact=False
                hostname = "13.69.155.75"
                port = "8080"
                chrome_options = Options()
                chrome_options.add_argument('--proxy-server={}'.format(getProxy(num)))
                driver = webdriver.Chrome(options=chrome_options)
                ck=(random.randint(1,3))
                num+=1
                
            else:
                ck=0
                
            driver.get(url)
            try:
                t=time.perf_counter()
                driver.find_element_by_id('649649255120112').send_keys(name)
                driver.find_element_by_id('1464214030500550').send_keys(username)
                driver.find_element_by_id('328991337275965').send_keys(mail)
                driver.find_element_by_id('602863763172693').send_keys(phone)
                driver.find_element_by_id('709786765737601').send_keys(text)
                driver.find_element_by_xpath('//button[@class="_42ft _4jy0 _4jy4 _4jy1 selected _51sy"]').click()
                
                n= False
                while n==False:
                    try:
                     driver.find_element_by_xpath('//a[@class="_42ft _42fu layerConfirm uiOverlayButton selected _42g- _42gy"]').click()
                     n=True
                    except:
                     n=False
                t1=time.perf_counter()
                sent+=1
                print ("REQUESTS SENT: ",sent)
                time.sleep(15-(t1-t))
            except:
                #print("da rimuovere")
                num-=1
                #delete(num)
                fact=True

def provalo():

    num=0
    while True:
        num+=1
        try:
               
                driver = webdriver.Chrome()
                driver.quit()
                fatc=False
                chrome_options = Options()
                chrome_options.add_argument('--proxy-server={}'.format(getProxy(num)))
                driver = webdriver.Chrome(options=chrome_options)
                driver.get('https://www.google.com/')
                
        except:
                print('da togliere')
                num-=1
                delete(num)
     


    
if __name__=="__main__":

    nome= input("Inserisci nome e cognome spaziati es: Karim Latrach => ")
    username= input ("Inserire username account es: spaccianotty => ")
    choice= input("SCEGLI: \n - SE VUOI USARE EMAIL E NUMERO CASUALI SCHIACCIA(1)\n - SE VUOI USARE NUMERO E MAIL PERSONALI SCHIACCIA(2): ")
    mail=""
    phone=""
    if choice=="2": 
        mail= input("inserisci mail :")
        phone= input("inserisci numero di telefono ")
    text= input("Inserisci motivazione sban: ")
    print("Verranno utilizzate mail e numeri di telefoni diversi per ogni modulo inviato! \n")
    sendRequest(nome,username,text,mail,phone)



  
