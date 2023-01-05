import os

import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def click(xpath):
    c = 0
    z = 0
    while True:
        try:
            driver.find_element(By.XPATH,xpath).click()
            break
        except:
            if z == 20:
                break
            z+=1
        if z==20:
            driver.find_element(By.XPATH, xpath).click()
"""file = open("data.txt","r")
line = file.readline()#.split(";")"""

a = False
if a:
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"download.default_directory": r"C:\Users\latra\Desktop\filedata"}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=chromeOptions)
    c = 1

    with open('data.txt') as file:
        for line in file:
            if c > 944:

                if "mega" in line:
                    driver.get(line)
                    try:
                        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[2]/div[1]/div/button'))
                        WebDriverWait(driver, 2).until(element_present)
                        click('/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[2]/div[1]/div/button')
                        click('/html/body/div[6]/div[2]/div[2]/section/div[1]/div/div[4]/div[3]/div[2]/div[1]/div/div/div/a[2]')
                        print(c, " download MEGA ")
                        c += 1
                    except:
                        print("pass")



                elif "drive" in line:
                    riga = line.split("/")
                    st3 = "https://drive.google.com/uc?id=" + riga[5] + "&export=download"
                    driver.get(st3)
                    sleep(2)
                    print(c, " download DRIVE")
                    c +=1
                    #click('/html/body/div[3]/div[4]/div/div[3]/div[2]/div[2]/div[3]/div')
                elif "yandex" in line:
                    driver.get(line)
                    element_present = EC.presence_of_element_located(
                        (By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/button[2]'))
                    WebDriverWait(driver, 10).until(element_present)
                    click("/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div[2]/button[2]")
                    sleep(4)
            else:

                c+=1

numstart = int(input("NUM START: "))
my_list = os.listdir(r"G:\filedata")

for i in my_list:
    os.rename("G:\\filedata\\"+ i,"G:\\filedata\\"+ str(numstart) + i[len(i)-4:len(i)])
    #"G:\filedata"
    numstart+=1