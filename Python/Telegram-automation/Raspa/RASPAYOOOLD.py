from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from colorama import Fore, init
import sys
import csv
import traceback
import time
import os
import requests
init(convert=True)
import random
print(Fore.LIGHTWHITE_EX+"-------------------------------------------------------")
print('             BENVENUTO NEL TUO BOT RASPA')
print(Fore.LIGHTWHITE_EX+'        DEVOLPED BY LATRACHYOO AND UBRASELEIRO')
print("-------------------------------------------------------")
text = ('RASPAYOO')
r = requests.get('http://artii.herokuapp.com/make?text='+text)
print(Fore.LIGHTRED_EX+r.text)
print(Fore.LIGHTWHITE_EX+"-------------------------------------------------------")
print(Fore.WHITE+'                      VERSIONE 1 ')
print(Fore.LIGHTWHITE_EX+"-------------------------------------------------------")

dati = {list: 10}

while True:
    try:
        scelta = int(input('\n- se vuoi usare dati vecchi inserisci => (1)\n- Se vuoi usare dati nuovi inserisci => (2):'))
        if scelta == 1 or scelta == 2:
            break
        else:
            print(Fore.LIGHTRED_EX+'- SCEGLI UNA DELLE DUE OPZIONI'+Fore.LIGHTWHITE_EX)
    except:
        print(Fore.LIGHTRED_EX+'- SCEGLI UNA DELLE DUE OPZIONI'+Fore.LIGHTWHITE_EX)

if scelta == 1:
    while True:
        nomefile = input(' - nome profilo: ')
        try:
            file = open("c:/raspayoo/accdata/"+ nomefile+ ".txt", "r")
            linea = file.readline()
            dati = linea.split(";")
            break
        except:
            print(Fore.LIGHTRED_EX+' NESSUN PROFILO, RIPROVARE'+Fore.LIGHTWHITE_EX)
else:
    print(Fore.LIGHTRED_EX+'\n\n\n ISTRUZIONI, LEGGERE ATTENTAMENTE')
    print(Fore.RED+'\n RECARSI SU '+Fore.LIGHTBLUE_EX+'"www.my.telegram.org"'+Fore.RED+', ACCEDERE E ANDARE SU:'+Fore.BLUE+ ' API development tools'+Fore.RED+ '.\n'
          ' IN CASO NON AVETE UN API E UN HASH SIGIFICA CHE DOVRETE CREARLO,\n'
          ' - METTEREUN UN NOME CHE SI VUOLE SU '+Fore.BLUE+ '"App title"'+Fore.RED+ ' E SU '+Fore.BLUE+ '"Short name"'+Fore.RED+ ' E POI SULLA SEZIONE\n'
                   ' URL METTETE: '+Fore.LIGHTBLUE_EX+'"www.my.telegram.org"'+Fore.RED+' E POI FAT ECREA,\n'
          ' SUBITO DOPO COMPARIRRANO LE VOCI '+Fore.BLUE+ '"App api_id" '+Fore.RED+ 'E '+Fore.BLUE+ '"App api_hash"'+Fore.LIGHTWHITE_EX+'  \n\n\n')
    dati[0] = input(' - numero di telefono: ')
    if dati[0][0:1] != "+":
        dati[0] = "+"+dati[0]
    while True:
        try:
            dati[1] = int(input(' - API ID: '))
            break
        except: print(Fore.LIGHTRED_EX+"INSERISCI CORETTAMENTE L'ID (SOLO VALORI NUMERICI)"+Fore.LIGHTWHITE_EX)
    dati[2] = input(' - INSERISCI IL HASH: ')
    nome = input('- NOME PROFILO: ')
    try:
        file = open('C:/memory/'+nome+".txt", 'w')
    except:
        os.mkdir('C:/memory')
        file = open('C:/memory/' + nome + ".txt", 'w')
    file.write(dati[0]+";"+str(dati[1])+";"+dati[2])
    file.close()
phone = dati[0]
api_id = dati[1]
api_hash = dati[2]
#'6b7ce1dcbb059ea88847234343c33639'
#7804488
#'+16093882573'
try:
    client = TelegramClient("C:\\RASPAYOO\\accdatasess\\"+phone, api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))

    chats = []
    last_date = None
    chunk_size = 200
    groups=[]

    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue

    print(Fore.BLUE+"\n- Scegli un gruppo da cui prendere i membri:\n"+Fore.LIGHTWHITE_EX)
    i=0
    for g in groups:
        print(Fore.LIGHTMAGENTA_EX+str(i)+Fore.LIGHTWHITE_EX + '- ' + g.title)
        i+=1

    while True:
        try:
            scr = int(input("\n- Scegli un numero: "))

            if (scr) > i-1:
                print(Fore.LIGHTRED_EX + '- INSERIRE UN NUMERO VALIDO COMPRESO DA 0 A ' + str(i-1) + Fore.LIGHTWHITE_EX)
            elif (scr) < i:
                break
        except:
            print(Fore.LIGHTRED_EX + '- INSERIRE UN NUMERO VALIDO COMPRESO DA 0 A ' + str(i-1)  + Fore.LIGHTWHITE_EX)


    g_index = scr
    target_group=groups[int(g_index)]

    print(Fore.LIGHTRED_EX+'\nFetching Members...' + Fore.LIGHTWHITE_EX)
    all_participants = []
    all_participants = client.get_participants(target_group, aggressive=True)

    print('Salvataggio del file...')
    with open("members.csv","w",encoding='UTF-8') as f:
        writer = csv.writer(f,delimiter=",",lineterminator="\n")
        writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
        for user in all_participants:
            if user.username:
                username= user.username
            else:
                username= ""
            if user.first_name:
                first_name= user.first_name
            else:
                first_name= ""
            if user.last_name:
                last_name= user.last_name
            else:
                last_name= ""
            name= (first_name + ' ' + last_name).strip()
            writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
    print('File salvato')

    input_file = 'c:/raspayoo/accdata/members.csv'
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f,delimiter=",",lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['username'] = row[0]
            user['id'] = int(row[1])
            user['access_hash'] = int(row[2])
            user['name'] = row[3]
            users.append(user)
    try:
        for user in users:
            print(user["username"])
    except:
        print("bib")
        pass
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    random.shuffle(users)

    result = client(GetDialogsRequest(
                 offset_date=last_date,
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=chunk_size,
                 hash = 0
             ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup== True:
                groups.append(chat)
        except:
            continue

    print(Fore.LIGHTBLUE_EX+'\n- Scegli un gruppo in cui aggiungere gli utenti:\n'+Fore.LIGHTWHITE_EX)
    i=0
    for group in groups:
        print(Fore.LIGHTMAGENTA_EX+str(i)+Fore.LIGHTWHITE_EX + '- ' + group.title)
        i+=1
    while True:
        try:
            scr = int(input("\n- Scegli un numero: "))

            if (scr) > i - 1:
                print(Fore.LIGHTRED_EX + '- INSERIRE UN NUMERO VALIDO COMPRESO DA 0 A ' + str(i-1)  + Fore.LIGHTWHITE_EX)
            elif (scr) < i:
                break
        except:
            print(Fore.LIGHTRED_EX + '- INSERIRE UN NUMERO VALIDO COMPRESO DA 0 A ' + str(i-1)  + Fore.LIGHTWHITE_EX)

    g_index = scr
    target_group=groups[int(g_index)]

    target_group_entity = InputPeerChannel(target_group.id,target_group.access_hash)
    while True:
        try:
            mode = int(input("\n\n- se vuoi aggiungere mebri in base all'username Inserisci (1):\n- se vuoi aggiungere i mebri in base all ID (Consigliato) inserisci (2): "))
            if mode == 1 or mode == 2:
                break
            else:
                print(Fore.LIGHTRED_EX + '- SCEGLI UNA DELLE DUE OPZIONI' + Fore.LIGHTWHITE_EX)
        except:
            print(Fore.LIGHTRED_EX + '- SCEGLI UNA DELLE DUE OPZIONI' + Fore.LIGHTWHITE_EX)

    delay = 0
    delay = input('''- Scegli un tempo di attesa tra l'aggiunta di un membro e l'altro (Consigliato: 30): ''')

    for user in users:
        try:
            print ("Aggiungendo {}".format(user['id']))
            if mode == 1:
                if user['username'] == "":
                    continue
                user_to_add = client.get_input_entity(user['username'])
            elif mode == 2:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
            else:
                sys.exit(Fore.LIGHTRED_EX+"Modalità non valida. Riprova."+Fore.LIGHTWHITE_EX)
            client(InviteToChannelRequest(target_group_entity,[user_to_add]))
            print("Attendendo " + str(delay) + " secondi per non essere bannato da telegram")
            time.sleep(int(delay))
        except PeerFloodError:
            print(Fore.LIGHTRED_EX+"Telegram ha restituito un flood error. Riprova tra un po."+Fore.LIGHTWHITE_EX)
        except UserPrivacyRestrictedError:
            print(Fore.LIGHTRED_EX+"Le impostazioni della privacy dell utente bloccano la aggiunta ai gruppi. Salto questo utente."+Fore.LIGHTWHITE_EX)
        except:
            traceback.print_exc()
            print(Fore.BLUE+"Unexpected Error"+Fore.LIGHTWHITE_EX)
            continue
except:
    print(Fore.LIGHTRED_EX+' HAI MESSO DEI DATI ERRATI, RIAVVIARE IL BOT'+Fore.LIGHTWHITE_EX)
