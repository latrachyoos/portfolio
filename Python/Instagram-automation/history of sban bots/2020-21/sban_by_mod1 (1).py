#developed by @Karim Latrach and @tommaso villoto for personal use
#18/03/2020
#follow me on ig @latrachyoo, @spaccianotty, @tommyvilo and @itagliano.degradato
from selenium import webdriver
import time
import random
import string
import os
from selenium.webdriver.chrome.options import Options
from time import sleep
#boolean ran= True;



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

def sendRequest(name,username,text,mail,phone,tempo):

        sent=0
        num=0
        #num1=countProxy()
        print ("REQUESTS SENT: ",sent)
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
            if pausa==250:
                print("IN PAUSA PER 20 MINUTI \n")
                time.sleep(1200)
                print("PAUSA TERMINATA \n")
                pausa=0
            pausa+=1
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
                print ("MODULO NUMERO: ",sent,"IN PAUSA PER",tempo,"SECONDI")
                time.sleep(str(tempo))
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
     


    

if __name__=='__main__':
    print( " BOT PER SBAN ATTRAVERSO LINK MOD1 AVVIATO CORRETAMENTE " )
    nome= input( " Inserisci nome e cognome spaziati es: Karim Latrach => ")
    username= input ("Inserire username account es: spaccianotty => ")
    mail= input("inserisci mail :")
    phone= input("inserisci numero di telefono ")
    text= input("Inserisci motivazione sban: ")
    tempo=str(input("distanza tra un modulo e un altro in secondi :"))
    print("Verranno utilizzate mail e numeri di telefoni diversi per ogni modulo inviato! \n")
    sendRequest(nome,username,text,mail,phone,tempo)
