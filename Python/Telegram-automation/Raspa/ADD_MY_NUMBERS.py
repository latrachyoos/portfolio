import subprocess

import pyautogui as py
import pyperclip
import pyautogui
import telethon
from bs4 import BeautifulSoup
from lxml import etree
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import random, string, requests, shutil, os
from time import sleep




my_list = os.listdir(r"C:\RASPAYOO\accdata")

for k in my_list:
    if "acc" in k:
        file = open("C:\\RASPAYOO\\accdata\\"+k)
        dati = file.readline().split(";")
        try:
            client = TelegramClient("accdatasess/" + dati[0], dati[1], dati[2])
            client.connect()
            client(JoinChannelRequest("@officialminidogetoken"))
            sleep(1)
            client(JoinChannelRequest("@teddytokengroup"))
            sleep(3)

        except Exception as e:
            print(k + " error")
            print(e)
