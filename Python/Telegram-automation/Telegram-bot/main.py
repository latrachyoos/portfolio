#5743046086:AAGlFUJm5I4aJeQWW66nasyp7PBFOT6ugm8
import sqlite3

import pyodbc
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
#https://gofile.io/d/g8IG3m
import accept_req
global autorizzato, amm

def send_to_telegram(text):

    apiToken = '5743046086:AAGlFUJm5I4aJeQWW66nasyp7PBFOT6ugm8'
    chatID = '-1001840826711'

    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatID}&text={text}"

    try:
        response = requests.post(apiURL)
        print(response.text)
    except Exception as e:
        print(e)

#send_to_telegram("https://en.wikipedia.org/static/images/project-logos/enwiki.png")

updater = Updater("5743046086:AAGlFUJm5I4aJeQWW66nasyp7PBFOT6ugm8",
                  use_context=True)


autorizzato = False
amm = False




def reply(update, context):
    global autorizzato, amm, conn

    if "USER" in str(update.message.text).upper()[0:4]:


        user_input = str(update.message.text).upper().replace(" ","")
        sql = f"select id_user from users where id_user='{user_input.lower()}'"
        print(sql)

        row = conn.execute(sql)
        if len(row.fetchall())==1:
            update.message.reply_text("User: " + (user_input))
            rows = conn.execute("select send from amm").fetchall()
            if rows[0][0] ==1:
                update.message.reply_text("INSERISCI IL MESSAGGIO: ")
                autorizzato = True
            else:
                update.message.reply_text("CHAT NON ATTIVA, CONTATTARE L'AMMINISTRATORE PER ATTIVARE L'INVIO DEI MESSAGGI NEL CANALE ")
                autorizzato = False

        else:
            update.message.reply_text("User non esistente ")
            autorizzato=False
        amm = False
    elif "amm_2004" == str(update.message.text).lower():
        amm = True
        update.message.reply_text("/open per attivare l'invio dei messaggi")
        update.message.reply_text("/close per disattivare l'invio dei messaggi")
        update.message.reply_text("/add per aggiungere uno user")
        update.message.reply_text("/remove per eliminare uno user")
        update.message.reply_text("/show per visualizzare tutti gli users")

    elif amm and "usradd" in str(update.message.text).lower():
        stringa = str(update.message.text).lower().replace("usradd","")
        stringa = stringa.replace(":","")
        stringa = stringa.replace(" ","")
        stringa = stringa.split("-")
        try:
            name = stringa[0]
            lastname = stringa[1]
            tag = stringa[2]

            if name == "nan":
                name = "null"

            if lastname == "nan":
                lastname = "null"
            if tag == "nan":
                tag = "null"



            #zfil
            ind = "0"
            rows = conn.execute("select ind from amm")
            for r in rows.fetchall():
                ind = str(r[0])
            codver = ind.zfill(6)

            id_user = "user" + codver

            data = [id_user, name, lastname, tag]

            sql = "insert into users(id_user, name, lastname, tag) values (?,?,?,?)"

            conn.execute(sql,data)
            conn.commit()

            ind = int(ind) + 1

            conn.execute(f"update amm set ind={ind}")

            conn.commit()

            update.message.reply_text(
                f"user aggiunto, il suo codice è: {id_user}" )
        except Exception as e:
            print(e)
            update.message.reply_text(
                "errore")














    elif amm and "usrdel" in str(update.message.text).lower():
        try:
            stringa = str(update.message.text).lower().replace("usrdel", "")
            stringa = stringa.replace(":", "")
            stringa = stringa.replace(" ", "")

            conn.execute(f"delete from users where id_user='{stringa}'")
            conn.commit()
            update.message.reply_text(
                "user rimosso")
        except:
            update.message.reply_text(
                "errore")







    elif "CODICE" in str(update.message.text).upper() and autorizzato:

        user_input = str(update.message.text).upper()

        user_input = user_input.replace("CODICE","")
        user_input = user_input.replace(":", "")
        user_input = user_input.replace(" ", "")
        if len(user_input) != 5:
            update.message.reply_text("Codice schedina sbagliata!")
        else:
            #send_to_telegram(user_input.replace("messagio da mandare:",""))
            send_to_telegram(user_input)
            update.message.reply_text("codice inviato!")
            update.message.reply_text("premere /start per ricominciare")

            autorizzato=False
    else:
        update.message.reply_text("codice non identificato")


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "codice identificativo: ")


def opens(update: Update, context: CallbackContext):
    global amm
    if amm:
        conn.execute("update amm set send=1")
        conn.commit()
        update.message.reply_text(
            "Chat aperta")

    else:
        update.message.reply_text(
            "non autorizzato")


def close(update: Update, context: CallbackContext):
    global amm
    if amm:
        conn.execute("update amm set send=0")
        conn.commit()
        update.message.reply_text(
            "Chat chiusa")

    else:
        update.message.reply_text(
            "non autorizzato")
def add(update: Update, context: CallbackContext):
    global amm
    if amm:
        update.message.reply_text(
            "Per aggiungere uno user devi inserire i dati in questo formato usradd: nome-cognome-tag_telegram, in caso mancasse un dato scrivi nan es usradd: Rossi-nan-@rossi")


    else:
        update.message.reply_text(
            "non autorizzato")
def remove(update: Update, context: CallbackContext):
    global amm
    if amm:
        update.message.reply_text("per rimuovere uno user scrivere usrdel: codice identificativo es: usrdel: user000001")


    else:
        update.message.reply_text(
            "non autorizzato")
def show(update: Update, context: CallbackContext):
    rows = conn.execute("select id_user, tag from users").fetchall()
    for row in rows:
        str = f"codice: {row[0]} - tag: @{row[1]}"
        update.message.reply_text(str)


conn = sqlite3.connect("bot_resender.db", check_same_thread=False)
updater.dispatcher.add_handler(CommandHandler('open', opens))
updater.dispatcher.add_handler(CommandHandler('close', close))
updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('remove', remove))
updater.dispatcher.add_handler(CommandHandler('show', show))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()
updater.idle()