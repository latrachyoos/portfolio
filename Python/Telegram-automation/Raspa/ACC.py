import os
import shutil
import subprocess
from time import sleep
import keyboard
from tkinter import *
from tkinter import messagebox

import pyautogui
import pyautogui as py
my_list = os.listdir(r"C:\Users\latra\Desktop\tgdatabase")
vecchia = ""
a = input("nome del gruppo: ")
b = True
c = True
for i in my_list:
    global cookie,hashrequests,r, api_id,hash,code, XYb, XYa
    p = 0
    if "+" in i:
        subprocess.call("TASKKILL /F /IM telegram.exe")
        sleep(2)
        try:
            shutil.rmtree(r"C:\Users\latra\Desktop\tgdatabase\randomaccess\tdata")
        except:
            pass
        shutil.copytree("C:\\raspayoo\\tgdatabase\\" + i + "\\tdata",
                        "C:\\raspayoo\\tgdatabase\\randomaccess\\tdata")
        os.system("cmd /c start /max C:\\raspayoo\\tgdatabase\\randomaccess\\Telegram.exe")
        if b:
            messagebox.showinfo("COSA DEVI FARE", "PUNTA IL MOUSE SOPRA L'ICONA DI TELEGRAM NELLA BARRA DELLE APPLICAZIONI, POI SCHIACCIA IL TASTO CONTROL -- SCHIACCIA OK E PROCEDI -- ")
            while True:
                if keyboard.read_key() == "ctrl":
                    XYa = py.position()
                    b = False
                    break
        sleep(5)
        pyautogui.click(XYa)
        pyautogui.click(XYa)
        pyautogui.click(XYa)
        pyautogui.click(XYa)
        pyautogui.click(XYa)
        pyautogui.click(XYa)
        sleep(3)
        pyautogui.click(x=143, y=50)
        keyboard.write(a)
        sleep(5)
        pyautogui.click(x=190, y=142)
        sleep(2)
        sleep(3)
        pyautogui.click(x=558, y=570)
        sleep(2)
        pyautogui.click(x=558, y=570)
        sleep(1)
        pyautogui.click(x=759, y=516)
        if c:
            messagebox.showinfo("COSA DEVI FARE",
                                "PUNTA IL MOUSE SOPRA IL MESSAGGIO DA CLICCARE PER VERIFICARE CHE SEI UN UMANO, POI SCHIACCIA IL TASTO CONTROL -- SCHIACCIA OK E PROCEDI -- ")
            while True:
                if keyboard.read_key() == "ctrl":
                    XYb = py.position()
                    c = False
                    break
        pyautogui.click(XYb)
        sleep(5)


