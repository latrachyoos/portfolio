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


my_list = os.listdir(r"G:\filedata")
d = 1
for file in my_list:
    try:
      


        Archive("G:\\filedata\\"+file).extractall(r"G:\tgdatabase")
        print(file + " UNZIPPED")
    except:
        pass
