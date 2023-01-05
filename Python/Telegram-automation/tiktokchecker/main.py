import requests
import sqlite3

from telegram.ext import MessageHandler
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.filters import Filters
import os
from telegram.ext.commandhandler import CommandHandler
#structuredb = "create table users(iduser int auto_incremental,user varchar(100),type varchar(100))"



def add(update, context):
    global aut
    if aut:
        aut = True
        user = str(update.message.text).lower()
        user = user.replace("/", "")
        user = user.replace("add", "")
        user = user.replace("@", "")
        user = user.replace(" ", "")
        user = user.replace("\n", "")
        if ";" in user:
            usr = user.split(";")
            for u in usr:
                sql = f"insert into users(user,type) values('{u}','tk')"
                conn.execute(sql)
                conn.commit()
            user = user.replace(';', '\n')
            update.message.reply_text(f"{user}\naggiunti correttamente:)")

        else:
            sql = f"insert into users(user,type) values('{user}','tk')"
            conn.execute(sql)
            conn.commit()
            update.message.reply_text(f"{user} aggiunto :)")

    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI AGGIUNGERE USERS")







def startcheck(update, context):
    global aut
    if aut:
        aut = True
        os.system("taskkill /f /im checker.exe")
        sql = f"update open set open=1"
        conn.execute(sql)
        conn.commit()
        os.system("cmd /c start  c:\\checker\\checker.exe")
    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI AVVIARE LA RICERCA ")

def remove(update, context):
    global aut
    if aut:
        aut = True
        user = str(update.message.text).lower()
        user = user.replace("/", "")
        user = user.replace("del", "")
        user = user.replace("@", "")
        user = user.replace(" ", "")
        user = user.replace("\n", "")
        if ";" in user:
            usr = user.split(";")
            for u in usr:
                sql = f"delete from users where user='{u}' and type='tk'"
                conn.execute(sql)
                conn.commit()
            user = user.replace(';',  '\n' )
            update.message.reply_text(f"{user} \nrimmossi correttamente :)")

        else:
            sql = f"delete from users where user='{user}' and type='tk'"
            conn.execute(sql)
            conn.commit()
            update.message.reply_text(f"{user} rimmosso :)")
    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI RIMUOVERE USERS ")

def start(update, context):
    update.message.reply_text("hey ciao :),\necco a te un po' di comandi utili:\n"
                              "-/add user, formato: /add tag, es: /add latrachyoo. Non servono @ o parole maiuscole. \n\n\n"
                              "-/del user, formato /del tag, es. /del latrachyoo. Non servono @ o parole maiuscole. \n\n\n"
                              "-/list per visualizzare tutti gli user.\n\n\n"
                              "-/check per iniziare a cercare.\n\n\n"
                              "-/stop per stoppare la ricerca.\n\n\n"
                              "-/channel t.me/channel, formato: /channel link o nome canale, es. /channel\n P.S AGGIUNGERE IL BOT NEL CANALE INTERESSATO. \n\n\n"
                                  "-/out per disconnettersi")
def stop(update, context):
    global aut
    if aut:
        aut = True
        os.system("taskkill /f /im checker.exe")
        sql = f"update open set open=0"
        conn.execute(sql)
        conn.commit()
        os.system("cmd /c start  c:\\checker\\checker.exe")
    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI INTERROMPERE LA RICERCA")


def view(update, context):
    global aut
    if aut:
        aut = True
        sql = "select distinct user from users"
        rows = conn.execute(sql).fetchall()
        if len(rows) > 0:

            users = f"ECCO LA LISTA DEGLI USERS \ni doppioni vengono uniti,\nConteggio users:{len(rows)}\n\n"
            for row in rows:
                users += f"@{row[0]}\n"
        else:
            users = "DATABASE VUOTO ;c"
        update.message.reply_text(users)
    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI VISUALLIZAE GLI USERS ")


def channel(update, context):
    global aut
    if aut:
        aut = True
        channel = str(update.message.text).lower()
        channel = channel.replace("https://web.telegram.org/k/#", "")
        channel = channel.replace("http://web.telegram.org/k/#", "")
        channel = channel.replace("web.telegram.org/k/#", "")
        channel = channel.replace("https://t.me/", "")
        channel = channel.replace("http://t.me/", "")
        channel = channel.replace("t.me/", "")
        channel = channel.replace("@", "")
        sql = f"update channel set channel='@{channel}'"
        conn.execute(sql)
        conn.commit()
        update.message.reply_text("CANALE AGGIORNATO")

    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI CAMBIARE LINK CANALE ")



def auth(update, context):
    global aut
    if update.message.text == "l056SAFd58FDAS65467uygfrud)&/()" or update.message.text == "Trachy00?":
        aut = True
        update.message.reply_text("BENVENUTO")
        update.message.reply_text("hey ciao :),\necco a te un po' di comandi utili:\n"
                                  "-/add user, formato: /add tag, es: /add latrachyoo. Non servono @ o parole maiuscole. \n\n\n"
                                  "-/del user, formato /del tag, es. /del latrachyoo. Non servono @ o parole maiuscole. \n\n\n"
                                  "-/list per visualizzare tutti gli user.\n\n\n"
                                  "-/check per iniziare a cercare.\n\n\n"
                                  "-/stop per stoppare la ricerca.\n\n\n"
                                  "-/channel t.me/channel, formato: /channel link o nome canale, es. /channel\n P.S AGGIUNGERE IL BOT NEL CANALE INTERESSATO.\n\n\n"
                                  "-/out per disconnettersi")
    else:
        aut = False
        update.message.reply_text("USER NON AUTORIZZATO")
        send_to_telegram(f"USER NON AUTORIZZATO @{update.message.chat.username} STA CECANDO DI ACCEDERE ")
def send_to_telegram(text):
    idchat = conn.execute("select channel from channel")
    apiToken = '5877675763:AAF4afrDXWY0i-DXIQL6-ZFrj3dC62_Zrjg'
    chatID = idchat.fetchall()[0][0]
    chatID = chatID.replace("/channel", "")
    chatID = chatID.replace("/CHANNEL", "")
    chatID = chatID.replace(" ", "")

    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatID}&text={text}"

    try:
        response = requests.post(apiURL)
        print(response.text)
    except Exception as e:
        print(e)
def out(update, context):
    global aut
    update.message.reply_text("DISCONESSIONE EFFETTUATA!")

aut = False
updater = Updater("5877675763:AAF4afrDXWY0i-DXIQL6-ZFrj3dC62_Zrjg",use_context=True)
conn = sqlite3.connect("tkcheck.sql", check_same_thread=False)
updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('check', startcheck))
updater.dispatcher.add_handler(CommandHandler('del', remove))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('list', view))
updater.dispatcher.add_handler(CommandHandler('channel', channel))
updater.dispatcher.add_handler(CommandHandler('out', out))
updater.dispatcher.add_handler(MessageHandler(Filters.text, auth))
updater.start_polling()
updater.idle()