import os
from time import sleep
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, FloodWaitError
from colorama import Fore, init
import csv
import traceback
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import time
from colorama import Fore
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser, InputUser, InputChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.account import UpdateProfileRequest
import requests
import random


"""INPUT SECTION"""

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
"""rI = requests.get('http://artii.herokuapp.com/make?text='+text)
print(Fore.LIGHTRED_EX+""+rI.text)
text = ('           PANELYOO')
r = requests.get('http://artii.herokuapp.com/make?text='+text)
stri ="latrachyoo devolpment sys" """
#print(Fore.LIGHTRED_EX+r.text)
print(Fore.LIGHTWHITE_EX+"--------------------------------------------------------------------------")
print(Fore.WHITE+'                                VERSIONE ' + __version__)
print(Fore.LIGHTWHITE_EX+"--------------------------------------------------------------------------")
"""a = int(input("[RANGE] RANGE-start --> "))
b = int(input("[RANGE] RANGE-end -->  "))
gruppoa = str(input("[-] @ Del gruppo dove prende i membri --> "))"""
#gruppob = str(input("\n[+] @ Del gruppo dove inserisce i membri --> "))
a = 10

b = 498
gruppoa="CryptoItaliaBitcoin"
gruppob="cryptoworldverified"
file = open("grp.txt","r",encoding="utf-8")
grb = file.readline().split(";")
file.close()
file = open("txt.txt","r",encoding="utf-8")
txt = file.read()
file.close()
print(txt)
target_group_entity = {list:10000000}
for i in grb:
    print(i)
client = {list:10000000}
target_group = {list:10000000}
def errors(frase):
    print(Fore.LIGHTRED_EX + "[ERROR] " + Fore.LIGHTWHITE_EX + frase.upper())

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


""" LOGICAL SECTION"""

progress = tgfather
contacc = a
while True:
    while contacc<b:
        file = open("C:\\RASPAYOO\\accdata\\acc" + str(contacc) + ".txt")
        dati = file.readline().split(";")
        file.close()
        client[0] = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + dati[0], int(dati[1]), dati[2])
        try:
            client[0].connect()
            if client[0].is_user_authorized():
                try:
                    """user_to_add = client[0].get_input_entity("danknazz")
                    print(user_to_add.user_id)
                    sleep(1)
                    client[0].send_message(user_to_add.user_id, "ciao")
                    print("messaggio mandato")"""
                    client[0](UpdateProfileRequest(first_name="LUCA", last_name="VALORI MASTER"))
                    client[0](UploadProfilePhotoRequest(client[0].upload_file("C:\\RASPAYOO\\filepy\\LUCAVALORI.jpg")))



                    sleep(1)
                    for i in grb:
                        try:
                            client[0](JoinChannelRequest(i))
                        except:
                            pass
                    try:
                        client[0](JoinChannelRequest(progress))
                    except:
                        pass
                    client[0].send_message(progress,txt)

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
                            try:
                                if chat.megagroup == True:
                                    groups.append(chat)
                            except:
                                continue
                        kl = 0
                        print("inizio ricerca")
                        for i in grb:

                            o = 0
                            g_index = -1
                            for g in groups:
                                try:
                                    if i.upper() in g.username.upper():
                                        g_index = o
                                        target_group[kl] = groups[int(g_index)]
                                        #print("gr: "+i)
                                        kl += 1
                                except:
                                    try:
                                        if i.lower() in g.username.lower():
                                            g_index = o
                                            target_group[kl] = groups[int(g_index)]
                                            #print("gr: " + i)
                                            kl += 1
                                    except:
                                        pass
                                o += 1
                            if g_index == -1:
                                print("gruppo: " + i + "non valido")
                            else:
                                pass
                        break
                    for i in target_group:
                        print(target_group[i])
                    users = []
                    csf = 0
                    print("inizio raccolta.")
                    try:
                        for i in target_group:
                            try:
                                for u in client[0].iter_participants(target_group[i], limit=10000):
                                    try:

                                        csf +=1
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
                                                    usert = {}
                                                    usert['username'] = username
                                                    usert['id'] = u.id
                                                    usert['name'] = name
                                                    users.append(usert)
                                        except:
                                            pass
                                    except Exception as e:
                                        #print(e)
                                        pass
                            except Exception as e:
                                #print(e)
                                pass


                    except Exception as e:
                        #print(e)
                        csf -= 1
                    print("HO RACCOLTO:",csf , " MEMBRI" )
                    break
                except Exception as e:
                    #print(e)
                    contacc +=1
            else:

                contacc += 1


        except Exception as e:

            #print(e)
            contacc += 1
    try:
        client[0].disconnect()
    except:
        pass
    d = b - a
    po = a

    data = {list: 10000}
    k = 0
    zk = 0
    import codecs
    ranges = b-a
    color = "white"
    import enlighten
    pbar = enlighten.Counter(total=ranges, desc='Basic', unit='ticks', color = color)
    while zk<=d:
        pbar.update()
        try:
            file1 = open("C:\\RASPAYOO\\accdata\\acc" + str(po) + ".txt", "r")
            linea = file1.readline()
            data[k] = linea
            file1.close()
            datis = linea.split(";")
            client[k] = TelegramClient("C:\\RASPAYOO\\accdatasess\\" + datis[0], int(datis[1]), datis[2])
            #print(datis)
            client[k].connect()
            #print("entered")
           # print(k)
            #print(client[k])
            sleep(2)
            client[k](JoinChannelRequest(progress))
            #print("a")
            try:
                client[k](UpdateProfileRequest(first_name="MARTIN", last_name="EARN"))
            except:
                pass
            try:
                client[k](UploadProfilePhotoRequest(client[k].upload_file(r"C:\RASPAYOO\filepy\pctr.png")))

            except:
                pass
            try:
                client[k].send_message(tgfather,"HELLO I'M ON")
            except:
                pass
            #client[k].send_message(progress,"HEY CIAO SONO ACC" + str(po-1) + " - ATTIVAZIONE COMPLETA")
            #print("acc"+str(po - 1)+ " is active")

            print(datis[0])
            client[k].disconnect()
            k += 1
        except Exception as e:
            print(e)

        po +=1
        zk +=1






    #random.shuffle(users)
    usr = users
    lens = len(usr)
    us = 0
    CLC = 1
    ADD =0
    send = 0
    err = 0
    while us < lens:
        for k in client:
            if err == 200:
                break
            delaymom = delay
                #random.randint(delay, delay + 40)
            try:

                user = (users[us])
                us += 1
                if user['username'] != "":
                    client[k].connect()
                    print("\n")
                    print(Fore.LIGHTBLUE_EX + "[SENDING] " + Fore.LIGHTWHITE_EX + (user['name']).upper() + Fore.RESET)

                    client[k].send_message(user['username'],txt)
                    send +=1
                    print(Fore.LIGHTGREEN_EX +"[SUCCES SENDING: "+ str(send) + "] " + Fore.LIGHTWHITE_EX + "@" +(user['username']).upper() + Fore.RESET)

                    try:
                        client[k].send_message(progress, "[SUCCES SENDING: "+ str(send) + "] @" + (user['username']).upper() + " MESSAGGIO INVIATO CORETTAMENTE!")
                    except:
                        pass
                    ADD +=1
                    err = 0
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
            except Exception as e:
                err +=1

                print(e)
                print(Fore.LIGHTRED_EX + "[FAIL OF ADDING] @" + Fore.LIGHTWHITE_EX + (user['username']).upper() + Fore.RESET)

        if mode == 1:
            print(Fore.LIGHTGREEN_EX + "[SLEEP TIME] " + Fore.LIGHTWHITE_EX + str(delaymom) + " SEC" + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + "\n\n\n\n[CIYCLE COUNT] " + Fore.LIGHTWHITE_EX + str(
                CLC) + " CICLI COMPLETATI" + Fore.RESET)
            print(Fore.LIGHTGREEN_EX + "[ADDING COUNTER] " + Fore.LIGHTWHITE_EX + str(
                ADD) + " UTENTI AGGIUNTI\n\n" + Fore.RESET)
            CLC += 1
            time.sleep(int(delaymom))





