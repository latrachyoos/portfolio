from time import sleep
import os
from time import sleep
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError
from colorama import Fore, init
import csv
import traceback
from telethon.tl.functions.channels import EditAdminRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
import asyncio
import time
from colorama import Fore
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputUser, InputChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import requests
import random
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
for po in range(449):
    try:
        print(po)
        file1 = open("C:\\RASPAYOO\\accdata\\acc" + str(po) + ".txt", "r")

        linea = file1.readline()

        file1.close()
        dati = linea.split(";")
        client = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + dati[0], int(dati[1]), dati[2])
        client.connect()
        client(LeaveChannelRequest("manuel_sanchezfx"))
        client.disconnect()
    except Exception as e:
        print(e)