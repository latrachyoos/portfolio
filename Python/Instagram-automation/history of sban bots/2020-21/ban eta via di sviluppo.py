#developed by @Karim Latrach and @tommaso villoto for personal use
#18/03/2020
#follow me on ig @latrachyoo, @spaccianotty, @tommyvilo and @itagliano.degradato
from selenium import webdriver
import time
import random
import string
import os
from selenium.webdriver.chrome.options import Options
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

def sendRequest(name,username):

        sent=0
        num=0
        #num1=countProxy()
        print ("MODULO INVIATO NUMERO: ",sent)
        driver = webdriver.Chrome()
        #name='karim latrach'
        #username='spaccianotty'
        #text= 'Hi, I was working with an influencer marketing agency. I closed the contract and strangely my account was deactivated. I am afraid it is a kind of revenge of the agency. Please help me recover the account.I am desperate and I do not know how. I hope your fantastic support team can help me.I wish you a good job.'
        url = 'https://help.instagram.com/contact/723586364339719'
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
                driver.find_element_by_id('735407019826414').send_keys(name)
                driver.find_element_by_id('258021274378282').send_keys(username)
                s1 = driver.find_element_by_xpath('//a[@class="periodMenu yearMenu"]').click()
                s1.select_by_value("208")
                
                s2 = Select(browser.find_element_by_id("506888789421014"))
                s2.select_by_value("4")
                s3 = Select(browser.find_element_by_id("294540267362199"))
                s3.select_by_val("Non-Family")
                

                driver.find_element_by_id('u_0_8').click()
                
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
     


    
if __name__ == '__main__':
    print( " BOT PER SBAN ATTRAVERSO LINK MOD1 AVVIATO CORRETAMENTE " )

    name= str(input( " Inserisci nome e cognome spaziati es: Karim Latrach => "))
    username= input ("Inserire username account es: spaccianotty => ")

    sendRequest(name,username)

