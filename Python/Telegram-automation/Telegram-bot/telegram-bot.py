from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from time import sleep
import json

from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest
from telethon.tl.types import InputChannel


def registrazione_login():
    print("-- registrazione user login info../")
    while True:
        try:
            id = int(input("--> inserisci l'api id telegram: "))
            break
        except:
            print("INSERISCI UN ID NUMERICO")
    while True:
        try:
            phone = int(input("--> inserisci numero di telefono con prefisso senza + di telegram: "))
            break
        except:
            print("INSERISCI UN NUMERO DI TELEFONO VALID SENZA +")
    hash = input("--> inserisci l'hash telegram: ")
    path = "accdatasess/" + str(phone) + ".session"

    file = {"login_info": [{"phone":phone,"id": id, "hash": hash, "path_session_file": path}]}
    try:
        client = TelegramClient(path,id, hash)
        client.connect()
        while True:
            try:
                if not client.is_user_authorized():
                    client.send_code_request(str(phone))
                    client.sign_in(str(phone), input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))
                    client.disconnect()
                    break
            except:
                print("codice errato")
    except Exception as e:
        print(e)



    with open("login-info.json","w") as f:
        json.dump(file, f)
        f.close()



def start_bot():
    global client
    gruppi = []
    f = open("login-info.json")
    login = json.load(f)

    phone = login["login_info"][0]["phone"]
    id = login["login_info"][0]["id"]
    hash = login["login_info"][0]["hash"]
    path = login["login_info"][0]["path_session_file"]
    f.close()

    try:
        client = TelegramClient(path, id, hash)
        client.connect()
        while True:
            try:
                if not client.is_user_authorized():
                    client.send_code_request(str(phone))
                    client.sign_in(str(phone), input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))

                    break
                else:
                    break
            except:
                print("codice errato")

        chat_a = "test_yoo_send"
        try:
            try:
                client(JoinChannelRequest(chat_a))
            except:
                client(ImportChatInviteRequest(chat_a))
        except Exception as e:
            print(e)
        n_g = 2
        for _ in range(n_g):
            grp = input("["+str(_+1)+"] @gruppo senza @-->")
            try:
                try:
                    client(JoinChannelRequest(grp))
                except:
                    client(ImportChatInviteRequest(grp))
            except Exception as e:
                print(e)

        print("let's go")
        a = client
        print(a)
        #1710424600
        #3729245100620546762
        input_channel = InputChannel(1710424600, 3729245100620546762)
        print(input_channel)
        cl = client.get_messages(input_channel,"ciao")
        print(cl)
        user = client.is_user_authorized()




        while True:
            for gruppo in gruppi:

                ordine = -1
                messages = client.get_messages(gruppo, 20)
                try:
                    file = open("accdatasess/last_"+gruppo+".txt","r")
                    last = file.readline()
                except:
                    file = open("accdatasess/last_" + gruppo + ".txt", "w")
                    file.write(str(0))
                file = open("accdatasess/last_" + gruppo + ".txt", "r")
                last = file.readline()

                k = 0
                lung = len(messages) -1

                for message in messages:
                    #print(k, last, lung)


                    if last == str(message.id):
                        if k > 0 and k < len(messages):

                            ordine = k
                        break
                    if int(k) == int(lung):
                        last = messages[0].id


                    k += 1

                if ordine > 0:
                    k = 0
                    for k in range(ordine):
                        client.send_message(chat_a,messages[ordine-1-k].message )
                        last = messages[ordine-1-k].id
                file.close()
                file = open("accdatasess/last_"+gruppo+".txt","w")
                file.write(str(last))
            sleep(5)






    except Exception as e:
        print(e)


















global client
f = open("login-info.json")
login = json.load(f)
id = login["login_info"][0]["id"]
f.close()

if id=="":
    registrazione_login()
while True:
    try:
        choose = int(input("SCEGLI |_>\n [1] modificare i dati di login\n [2] avviare:\n -->"))
        if choose==1 or choose==2:
            start_bot()

        else:
            print("scegli un opzione valida")

    except Exception as e:
        try:
            client.disconnect
        except:
            pass
        print(e)
        print("scegli un opzione valida!")









