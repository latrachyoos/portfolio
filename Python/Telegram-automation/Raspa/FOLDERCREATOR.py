import pyscreenshot as ImageGrab
import pytesseract
import pyautogui
from time import sleep
import telethon
from pyunpack import Archive

from telethon.sync import TelegramClient
from pathlib import Path

from telethon.tl.functions.channels import JoinChannelRequest
import random,string,requests,shutil,os,zipfile



my_list = os.listdir(r"G:\tgdatabase")
for foldername in my_list:
    if not "not" in foldername and not foldername=="randomaccess":

        try:
            os.system("TASKKILL /F /IM telegram.exe")
        except Exception as e:
            pass
        try:
            shutil.rmtree("G:\\tgdatabase\\randomaccess\\tdata")
        except:
            pass
        try:
            shutil.copytree("G:\\tgdatabase\\"+foldername+"\\tdata","G:\\tgdatabase\\randomaccess\\tdata")
        except:
            try:
                shutil.rmtree("G:\\tgdatabase\\randomaccess\\tdata")
            except:
                pass
        for k in range(10):
            try:
                shutil.rmtree("G:\\tgdatabase\\randomaccess\\tdata")
            except:
                pass
        try:
            shutil.copytree("G:\\tgdatabase\\" + foldername + "\\tdata",
                            "G:\\tgdatabase\\randomaccess\\tdata")
            os.system("cmd /c start /max G:\\tgdatabase\\randomaccess\\Telegram.exe")
            sleep(5)
            pyautogui.click(x=1107, y=1048)
            pyautogui.click(x=1107, y=1048)
            pyautogui.click(x=1107, y=1048)
            pyautogui.click(x=1107, y=1048)
            sleep(2)
            pyautogui.click(x=400, y=500)
            sleep(3)
            pyautogui.click(20, 47)
            sleep(2)
            im = ImageGrab.grab(bbox=(20, 100, 200, 150))
            im.save(r"C:\Users\latra\Desktop\prova1.png")
            sleep(2)
            pyautogui.click(x=1107, y=1048)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
            string = (pytesseract.image_to_string(r"C:\Users\latra\Desktop\prova1.png"))
            ver = False
            c = 0
            newnum = ""
            cont = 0

            for k in string:
                # print(k)
                if k == "+" or k == "#" or k == "4" or k == "7":
                    ver = True
                if ver and cont < 2:
                    if k != " ":
                        cont = 0
                        newnum = newnum + k
                    else:
                        cont += 1

            if str(newnum)[0:1] == "4" or str(newnum)[0:1] == "7":
                newnum = "+" + str(newnum)[1:len(newnum)]
            newnum = newnum.replace("#", "+").strip()
            newnum = newnum.replace(" ", "").strip()
            newnum = newnum.replace(".", "").strip()
            newnum = newnum.replace(":", "").strip()
            numero = newnum
            if len(numero) < 5:
                numero = "notlogged" + foldername
            nummom = numero.replace("+", "")
            nummom='+'+nummom
            os.system("TASKKILL /F /IM telegram.exe")
            sleep(3)
            print(nummom)
            os.rename("G:\\tgdatabase\\"+foldername,"G:\\tgdatabase\\"+nummom)
            file = open("G:\\tgdatabase\\" + nummom + "\\notregistred.txt", "w")
            file.close()
        except Exception as e:
            print(foldername)
            print(e)
            numero = "notloggeddir" + foldername
            os.rename("G:\\tgdatabase\\" + foldername, "G:\\tgdatabase\\" + numero)





