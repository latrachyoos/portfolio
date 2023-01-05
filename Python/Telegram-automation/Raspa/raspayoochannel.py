import os
from time import sleep
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError
from colorama import Fore, init
import csv
import traceback
from telethon.tl.functions.channels import EditAdminRequest, LeaveChannelRequest
from telethon.tl.functions.channels import EditAdminRequest
import asyncio
from telethon import TelegramClient, sync, events
import time
from colorama import Fore
from telethon.tl.functions.contacts import ResolveUsernameRequest
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
from telethon.tl.functions.messages import ImportChatInviteRequest
chat_id = {list:100000}
def errors(frase):
    print(Fore.LIGHTRED_EX + "[ERROR] " + Fore.LIGHTWHITE_EX + frase.upper())
__author__ = "latrachyoo S.P.A"
__copyright__ = "Copyright (C) 2921 " + __author__
__license__ = "Private Domain"
__version__ = "6.0"
init(convert=True)
os.system("mode con: cols=74 lines=40")
print(Fore.LIGHTWHITE_EX+"--------------------------------------------------------------------------")
print('                        BENVENUTO NEL TUO BOT RASPA')
print(Fore.LIGHTWHITE_EX+'                          DEVOLPED BY LATRACHYOO')
print("--------------------------------------------------------------------------")
text = ('                   MEDIA')
rI = requests.get('http://artii.herokuapp.com/make?text='+text)
print(Fore.LIGHTRED_EX+""+rI.text)
text = ('           PANELYOO')
r = requests.get('http://artii.herokuapp.com/make?text='+text)
stri ="latrachyoo devolpment sys"
print(Fore.LIGHTRED_EX+r.text)
print(Fore.LIGHTWHITE_EX+"--------------------------------------------------------------------------")
print(Fore.WHITE+'                                VERSIONE ' + __version__)
print(Fore.LIGHTWHITE_EX+"--------------------------------------------------------------------------")
while True:
    try:
        cnlorgrp = int(input("[+] VUOI AGGIUNGERE I MEMBERI IN UN: \n [-] GRUPPO PUBBLICO:\n [-] CANALE PUBBLICO:\n --->"))
        if cnlorgrp == 1 or cnlorgrp == 2:
            print("ATTENZIONE, DOVRAI NOMINARE AMMINISTRATORI, SUCCESSIVAMENTE QUANDO TE LO CHIEDE IL BOT, TUTTI I VOIP!")
            print("ATTENZIONE, IL BOT ACCETTA SOLO GRUPPI PER PRENDERE I MEMBRI!")
            break

        else:
            errors(" SELEZIONA UN PARAMENTRO VALIDO; 1-2!")
    except:
        errors(" SELEZIONA UN PARAMENTRO NUMERICO VALIDO; 1-2!")
"""a = int(input("[RANGE] RANGE-start --> "))
b = int(input("[RANGE] RANGE-end -->  "))
gruppoa = str(input("[-] @ Del gruppo dove prende i membri --> "))
gruppob = str(input("\n[+] @ Del gruppo\CANALE PUBBLICO dove inserire i membri --> "))"""
#400
a = 43
b =50
gruppoa="thewolfoftuscanyofficial"
gruppob="manuel_sanchezfx"
#gruppob= "latrachyootest1"
        #"manuel_sanchezfx"

end = 1500
while True:
    try:
        print(Fore.LIGHTCYAN_EX + "\n[SELECT MODE SLEEP]" + Fore.LIGHTWHITE_EX + " CHE MODALITA' DI PAUSA VUOI USARE? \n- [1] PAUSA TRA UN CICLO E L'ALTRO:\n- [2] PAUSA TRA UN VOIP E L'ALTRO:")
        mode = int(input("---> "))
        if mode == 2 or mode == 1:
            while True:
                try:
                    if mode ==1:
                        print(
                            Fore.LIGHTCYAN_EX + "\n[SELECT OPTION]" + Fore.LIGHTWHITE_EX + " VUOI UNA PICCOLA PAUSA DI 5 SEC TRA UN VOIP E L'ALTRO? \n [1] SI:\n [2] NO:")
                        active = int(input("---> "))
                        if active == 2 or active == 1:
                            break
                        else:
                            errors("SCRIVI UN OPZIONE VALIDA 1 o 2 ")
                    else:
                        break


                except:
                    errors("USARE CARATTERI NUMERICI, GRAZIE ")

            break
        else:
            errors("SCRIVI UN OPZIONE VALIDA 1 o 2 ")
    except:
        errors("USARE CARATTERI NUMERICI, GRAZIE ")



while True:
    try:
        print(Fore.LIGHTCYAN_EX + "\n[SELECT TIME]" + Fore.LIGHTWHITE_EX + " SCRIVI UNA PAUSA IN SECONDI (CONSIGLIATO 20 SEC): ")
        delay = int(input("---> "))
        break
    except:
        errors("USARE CARATTERI NUMERICI, GRAZIE ")
target_group_entity = {list:10000000}
client = {list:10000000}

try:
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt","r")
    tgfather = str(file.readline())
    file.close()
except:
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt", "r")
    file.write(input("-name tggroupfather: "))
    file.close()
    file = open(r"C:\RASPAYOO\accdata\TGFATHER.txt", "r")
    tgfather = str(file.readline())
    file.close()
progress = tgfather
contacc = a
while contacc<b:
    try:
        file = open("C:\\RASPAYOO\\accdata\\acc" + str(contacc) + ".txt")
        dati = file.readline().split(";")
        file.close()
        client[0] = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + dati[0], int(dati[1]), dati[2])
        try:
            client[0].connect()

            if client[0].is_user_authorized():
                    #userinfo = (client[0].get_entity("me"))
                    #client[0](UpdateProfileRequest(first_name= userinfo.first_name, last_name =  userinfo.last_name + " VOIP RASPA"))
                try:
                    try:
                        client[0](JoinChannelRequest(gruppoa))
                    except Exception as e:
                        print(e)

                    try:
                        client[0](JoinChannelRequest(gruppob))
                    except:
                        pass
                    sleep(1)
                    try:
                        client[0](JoinChannelRequest(progress))
                    except:
                        pass
                    sleep(2)
                    while True:
                        chats = []
                        last_date = None
                        chunk_size = 200
                        groups = []
                        result = client[0](GetDialogsRequest(
                            offset_date=last_date,
                            offset_id=0,
                            offset_peer=InputPeerEmpty(),
                            limit=chunk_size,
                            hash=0
                        ))
                        chats.extend(result.chats)
                        for chat in chats:
                            #print(chat)
                            try:
                                if chat.megagroup == True:
                                    groups.append(chat)
                            except:
                                continue
                        o = 0
                        g_index = -1

                        for g in groups:

                            try:
                                if gruppoa.upper() in g.username.upper():
                                    print(g.username)
                                    g_index = o
                            except:
                                try:
                                    if gruppoa.lower() in g.username.lower():
                                        g_index = o
                                except:
                                    pass

                            o += 1
                        if g_index == -1:
                            gruppoa = str(input("[-] @ del gruppo VALIDO dove prende i membri --> "))
                            client[0](JoinChannelRequest(gruppoa))
                            sleep(1)
                        else:

                            break

                    target_group = groups[int(g_index)]
                    users = []

                    csf = 0
                    try:
                        for u in client[0].iter_participants(target_group, aggressive=False, limit=200):

                            if u.username:
                                username = u.username
                            else:
                                username = ""
                            if u.first_name:
                                first_name = u.first_name
                            else:
                                first_name = ""
                            if u.last_name:
                                last_name = u.last_name
                            else:
                                last_name = ""
                            name = (first_name + ' ' + last_name).strip()
                            try:
                                    if username != "":
                                        if name.upper() == "AMAR":
                                            csf += 1
                                            usert = {}
                                            usert['username'] = username
                                            usert['name'] = name
                                            usert['id'] = u.id
                                            usert['access_hash'] = u.access_hash
                                            users.append(usert)
                            except:
                                pass
                    except:
                        csf -= 1
                    print("HO RACCOLTO:",csf , " MEMBRI" )

                    while True:
                        chats = []
                        last_date = None
                        chunk_size = 200
                        groups = []
                        result = client[0](GetDialogsRequest(
                            offset_date=last_date,
                            offset_id=0,
                            offset_peer=InputPeerEmpty(),
                            limit=chunk_size,
                            hash=0
                        ))
                        chats.extend(result.chats)
                        for chat in chats:
                            try:
                                if chat.megagroup == True or chat.gigagroup==False:
                                    groups.append(chat)
                            except:
                                continue
                        o = 0
                        g_index = -1
                        for g in groups:
                            try:
                                if gruppob.upper() in g.username.upper():
                                    print(g)
                                    g_index = o
                            except:
                                try:
                                    if gruppob.lower() in g.username.lower():
                                        g_index = o
                                except:
                                    pass

                            o += 1
                        if g_index == -1:
                            gruppob = input("[+] @ del gruppo VALIDO dove inserisce i membri --> ")
                            try:
                                client[0](JoinChannelRequest(gruppob))
                            except:
                                pass
                            sleep(1)
                        else:

                            break

                    break
                except Exception as e:


                    contacc +=1

            else:

                contacc += 1

        except:

            contacc += 1
    except:
        contacc += 1


#print("inizio sezione massa")

"""random.shuffle(users)
usr = users
lens = len(usr)
us = 0
print("start2")"""

sleep(5)
d = b - a
po = a

data = {list: 10000}
k = 0
zk = 0
ranges = b-a
color = "white"

import enlighten
pbar = enlighten.Counter(total=ranges, desc='Basic', unit='ticks', color = color)
while zk<=d:
    pbar.update()
    try:

        try:
            file1 = open("C:\\RASPAYOO\\accdata\\acc" + str(po) + ".txt", "r")
            po += 1
            linea = file1.readline()
            data[k] = linea
            file1.close()
            dati = linea.split(";")
            client[k] = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + dati[0], int(dati[1]), dati[2])
            sleep(3)
            for p in range(3):
                try:
                     client[k].disconnect()
                     sleep(0.1)
                except:
                    pass

            client[k].connect()
            client[k](LeaveChannelRequest(gruppob))
            client[k](JoinChannelRequest(gruppob))
            client[k](JoinChannelRequest(progress))
            try:
                userinfo = (client[k].get_entity("me"))
                client[k](UpdateProfileRequest(first_name=userinfo.first_name, last_name=userinfo.last_name + " VOIP RASPA " + str(zk)))
            except Exception as e:
                client[k](UpdateProfileRequest(first_name= "maneul", last_name=" latrachyoo VOIP RASPA " + str(zk)))

            chats = []
            last_date = None
            chunk_size = 200
            groups = []
            result = client[k](GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash=0
            ))
            chats.extend(result.chats)
            for chat in chats:
                try:
                    if chat.megagroup == True or chat.gigagroup==False:
                        groups.append(chat)
                except:
                    continue
            o = 0
            g_index = -1
            for g in groups:
                try:
                    if gruppob.upper() in g.username.upper():
                        g_index = o
                except:
                    try:
                        if gruppob.lower() in g.username.lower():
                            g_index = o
                    except:
                        pass
                o += 1
            target_group = groups[int(g_index)]
            print(target_group)
            target_group_entity[k] = InputChannel(channel_id=target_group.id, access_hash=target_group.access_hash)
            response = client[k](ResolveUsernameRequest(gruppob))

            target_group_entity[k] = InputPeerChannel(response.chats[0].id, response.chats[0].access_hash)

            chat_id[k] = target_group.id

            client[k].disconnect()
            k+=1
        except Exception as e:
            print(e)
            po +=1
    except Exception as e:
        print(e)
    zk +=1
print(k)
#for k in range(0, d + 1):
if cnlorgrp == 2:
    input("\n- RENDI AMMINISTRATORI TUTTI I MEMBRI CHE TERMINANO CON 'VOIP RASPA', PREMERE INVIO UNA VOLTA FINITO.../")

random.shuffle(users)
usr = users
lens = len(usr)
us = 0
CLC = 1
ADD =0
while us < lens:
    for k in client:
        delaymom = random.randint(delay, delay + 20)
        #try:
        user = (users[0])
        us += 1
        if user['username'] != "":
            try:
                client[k].connect()
                v = True
            except:
                v = False
            if v:
                print("\n")
                from telethon.tl.functions.messages import AddChatUserRequest
                print(Fore.LIGHTBLUE_EX + "[ADDING] " + Fore.LIGHTWHITE_EX + (user['name']).upper() + Fore.RESET)
                user_to_add = client[k].get_input_entity(user['username'])
                if user["name"].upper() == "AMAR":
                    try:
                        client[k](InviteToChannelRequest(channel=target_group_entity[k], users=[user_to_add]))
                    except:
                        id = "-1001610240352"
                        user_to_add = user["username"]
                        client[k](AddChatUserRequest(id,user_to_add,fwd_limit=10 ))


                    print(Fore.LIGHTGREEN_EX +"[SUCCES ADDED] " + Fore.LIGHTWHITE_EX + "@" +(user['username']).upper() + Fore.RESET)
                """except Exception as e:
                                    print(e)"""
                #client[k].send_message(progress, "[SUCCES ADDED] @" + (user['username']).upper() + ", GRUPPO DI PROVENIENZA: @" + gruppoa + " GRUPPO DI DESTINAZIONE: @" + gruppob)
                ADD +=1
                if ADD > end:
                    exit()
                    quit()

                try:
                    client[k].disconnect()
                except:
                    pass

                if mode == 1:
                    if active==1:
                        time.sleep(5)
                else:
                    print(
                        Fore.LIGHTGREEN_EX + "[SLEEP TIME] " + Fore.LIGHTWHITE_EX + str(delaymom) + " SEC" + Fore.RESET)
                    time.sleep(int(delaymom))
        #except Exception as e:
            #print(e)
            #print(Fore.LIGHTRED_EX + "[FAIL OF ADDING] @" + Fore.LIGHTWHITE_EX + (user['username']).upper() + Fore.RESET)

    if mode == 1:
        print(Fore.LIGHTGREEN_EX + "[SLEEP TIME] " + Fore.LIGHTWHITE_EX + str(delaymom) + " SEC" + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + "\n\n\n\n[CIYCLE COUNT] " + Fore.LIGHTWHITE_EX + str(
            CLC) + " CICLI COMPLETATI" + Fore.RESET)
        print(Fore.LIGHTGREEN_EX + "[ADDING COUNTER] " + Fore.LIGHTWHITE_EX + str(
            ADD) + " UTENTI AGGIUNTI\n\n" + Fore.RESET)
        CLC += 1
        time.sleep(int(delaymom))





