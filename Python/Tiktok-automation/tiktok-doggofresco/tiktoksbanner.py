#DATA CREAZIONE SBANYOO: 18/03/2020
#AGGIORNAMENTO DEFINITIVO - PASSAGGIO DA SELENIUM A REQUESTS 4/02/2022, ACCANTONATO E ELIMINATO TUTTO DI SBANYOO SELENIUM :(
#reintegro selenium mod4 21/07 - migraggio richesto a windows
import string
from requests_toolbelt import MultipartEncoder
from time import sleep
from selenium import webdriver
from colorama import init, Fore, Style
from telethon.sync import TelegramClient
import requests, random, os, pandas as pd
#169.197.83.75:11748@4k81j:rci9l8e5


def plusservice(LINK, data, head, r=None):
    global k, txt, send,modplus, tentativi
    send = True
    txt = ""
    varnum = 0

    if verprox:
        proxies = {
            'http': 'http://' + proxi,
            'https': 'http://' + proxi
        }
        if r==None:
            r = requests.session()

        req = r.post(LINK, data=data, headers=head, timeout=10, proxies=proxies)
    else:
        r = requests.session()

        req = r.post(LINK, data=data, headers=head, timeout=10)
    #print(req.text)


    print(Fore.LIGHTYELLOW_EX + "[STARUS CODE]" + Style.RESET_ALL, req.status_code)
    if '"statusCode":0,"body":{"statusCode":0}' in req.text:
        pass

    elif '"statusCode":3119' in req.text:
        txt += ", SPAM"
        message("@" + user[k] + ' SPAM')
        send = False
    else:
        txt += ", ERRORE GENERICO"
        message("@" + user[k] + ' ERRORE GEN ERICO: ' + req.text)
        send = False
        print(req.text)


    if req.status_code == 429:
        txt += ", TROPPE RICHIESTE, RIAVVIARE LA CONNESSIONE"
        message("@" + user[k] + ' TROPPE RICHIESTE, CONSIGLIO DI RIAVVIARE LA CONNESSIONE')
        varnum += 1
        send = False
    if req.status_code == 500:
        txt += ", MODULO NON MANDATO"
        message("@" + user[k] + ' NON MANDATO')
        send = False
    try:
        r.close()
    except Exception as e:
        #print(e)
        pass

    return send
def message(testo):
    global nomepc
    if logins.lower() == "si":
        try:
            client.send_message(msg, message=nomepc + ": " + testo)
        except:
            pass
def slept():
    try:
        if tempo > 30:
            tempomom = random.randint(tempo - 10, tempo + 10)
        else:
            tempomom = random.randint(tempo, tempo + 10)
        print(Fore.LIGHTYELLOW_EX + "[TIME]" + Style.RESET_ALL + " PAUSA DI: ", tempomom, "SECONDI")
        sleep(tempomom)
    except:
        pass
def login():
    global client, dati, nomepc
    try:
        phone = dati[0]
        api_id = int(dati[1])
        api_hash = dati[2]

        client = TelegramClient(nomepc, api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone)
            client.sign_in(phone, input('Inserisci il codice che dovrebbe esserti arrivato su telegram: '))
        message('IS ONLINE')
    except:
        print('LOGIN FAIL')
def mails():
    mail = ""
    value = random.randint(5, 15)
    dizio = {1: 'a', 3: 'c', 2: 'b', 5: 'e', 4: 'd', 7: 'g', 6: 'f', 9: 'i', 8: 'h', 11: 'k', 10: 'j', 13: 'm', 12: 'l',
             15: 'o', 14: 'n', 17: 'q', 16: 'p', 19: 's', 18: 'r', 21: 'u', 20: 't', 23: 'w', 22: 'v', 25: 'y', 24: 'x',
             26: 'z'}
    for i in range(0, value):
        x = dizio[random.randint(1, 26)]
        mail += x
    mail += "@gmail.com"
    return mail
def phones():
    number = "+393"
    for i in range(0, 9):
        number += str(random.randint(0, 9))
    return number
def modtk(typeban):
    #Banned account (not age-related)   #Banned account (age-related)    #Other
    global k
    r = requests.Session()
    link = "https://www.tiktok.com/login?redirect_url=https%3A%2F%2Fwww.tiktok.com%2F&lang=en&enter_method=mandatory"

    req = r.get(url=link)
    tt_csrf_token = req.cookies["tt_csrf_token"]
    ttwid = req.cookies["ttwid"]
    cookie = "s_v_web_id=verify_lb9bmm6w_NWpt7ook_4Fhy_43at_B9v4_kfxhODlB0dBq; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22};" + f"tt_csrf_token={tt_csrf_token}; ak_bmsc=22F55612299D134CF540A3DF21D27E91~000000000000000000000000000000~YAAQZbg1VCQnpHSEAQAAyDAQ3RK9Uj+fLje9JDCY7M0Xfha1MBYL80+kUcjTXIluw6gHfOJP1964BCM2+k4zElJ2OADr6xG05Spo5YPqu3v2NKr2t8QlH78SsgOqCEZw0pi82aeGlYaitaW5DqmWbCE8/scRt8go+tofvUFBdJmWUwj1Ls4tqnHfE6ubq3QgXax/ZMzul/gYvrQzMGvrr/X5oYc5s/QfdvRQ18dZ8Q8QQJq3gqYcUdrKJGB9fjsVz9fhJduKkoKDC4Fs3t9emPyKNM+2CnO0SXW39nZltAcfGPHkEBwTnZVubXOONulfjL0tFFn+X5kl1WMT/2KTJk5cRl0McD3j2RGQCZEIkSagwZ8pI04oCQJUhYvpN6GEMjr9bffeR/4=; ttwid={ttwid};" + " __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227173265919224989189%22%2C%22timestamp%22:1670156138410};" + f" ttwid={ttwid}; msToken=G7OPWV35oFjdRF3GFmlmD-S_4vm9v_8doBILTygW-iRUI8YQj6hxqsb2SUeNh7parBlKnQiOKRnDeC9mug0d9yQAsaSwc3XmivjALlBVLZ5SOvjKGWCx; msToken=G7OPWV35oFjdRF3GFmlmD-S_4vm9v_8doBILTygW-iRUI8YQj6hxqsb2SUeNh7parBlKnQiOKRnDeC9mug0d9yQAsaSwc3XmivjALlBVLZ5SOvjKGWCx"

    LINK = "https://www.tiktok.com/legal/report/feedback/send"
    datam = {
        "verify": "0",
        "email": maill[k],
        "username": user[k],
        "option": "Account ban/suspension",
        "feedback": text[k],
        "agreement": "I ensure, to the best of my ability and knowledge, that all the information disclosed above is accurate and true.,By submitting, I acknowledge that TikTok will process my data in accordance with TikTok's Privacy Policy.",
        "option2": typeban,
        "formTopicVal": "feedback_webform_dropdown_main_opt2",
        "formTellUsMoreVal": "feedback_webform_dropdown_main_opt2_c",
        "formReportReasonVal": "",

    }
    boundary = '----WebKitFormBoundary' \
               + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    data = MultipartEncoder(fields=datam, boundary=boundary)

    head = {
        "authority": "www.tiktok.com",
        "method": "POST",
        "path": "/legal/report/feedback/send",
        "scheme": "https",
        "Host": "www.tiktok.com",
        "Connection": "close",
        "Content-Length": "1444",
        "sec-ch-ua-platform": "Windows",
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Origin": "https://www.tiktok.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.tiktok.com/legal/report/feedback?lang=en",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cookie": cookie,
    }
    return plusservice(LINK, data, head,r)












def mod(user, tempo):
    try:
        global txt, k, send,modplus,righe,nomefile, motind, indmotper, contindmot, mailind, indmailper, contindmail
        while True:
            b = 1
            k = 1
            while k < righe:



                send = True
                if str(modd1[k]).lower() == "nan" and str(modd2[k]).lower() == "nan" and str(
                        modd3[k]).lower() == "nan" and str(modd4[k]).lower() == "nan" and str(
                    modd5[k]).lower() == "nan" and str(modd6[k]).lower() == "nan" and str(modd7[k]).lower() == "nan":
                    pass
                else:
                    try:
                        text[k] = motind[k][indmotper[k]]
                        maill[k] = mailind[k][indmailper[k]]
                        if not indmotper[k] >= contindmot[k]:
                            indmotper[k] += 1
                        else:
                            indmotper[k] = 0

                        if not indmailper[k] >= contindmail[k]:
                            indmailper[k] += 1
                        else:
                            indmailper[k] = 0
                    except:
                        pass




                    try:
                        print("\n" + Fore.LIGHTCYAN_EX + "[SUMMARY]" + Style.RESET_ALL + " USER: @" + user[
                            k].upper() + Fore.LIGHTBLUE_EX + "\n[COUNT]" + Style.RESET_ALL, count[k])
                    except:
                        print("\n" + Fore.LIGHTCYAN_EX + "[SUMMARY]" + Style.RESET_ALL + " USER: @" + user[
                            k].upper())
                # mod1
                if str(modd1[k]).lower() == str("x").lower() or str(modd1[k]).lower() == str("xx").lower() or str(
                        modd1[k]).lower() == str("xxx").lower():
                    typeban = ""
                    try:

                        # Banned account (not age-related)   #Banned account (age-related)    #Other

                        if str(modd1[k]).lower() == str("xx").lower():
                            send = modtk("Banned account (not age-related)")
                            typeban = "Banned account (not age-related)"
                        elif str(modd1[k]).lower() == str("xxx").lower():
                            send = modtk("Other")
                            typeban = "Other"
                        else:
                            send = modtk("Banned account (age-related)")
                            typeban = "Banned account (age-related)"

                        if send == False:
                            print(Fore.LIGHTCYAN_EX + "[MINIMAL ERROR]" + Style.RESET_ALL + "USER: @" + user[k].upper() + f" MOD tiktok {typeban} COMPILATO CORETTAMENTE, MA SI SONO VERIFICATI I SEGUENTI CODERROR :" + Fore.RED + txt[2:len(txt)])
                        else:
                            print(Fore.LIGHTGREEN_EX + "[SUCCESS]" + Style.RESET_ALL + " USER: @" + user[k].upper() + f" MOD tiktok {typeban} MANDATO CORRETTAMENTE SENZA NESSUN ERRORE ")
                        slept()
                        count[k] += 1
                    except Exception as e:
                        print(e)
                        print(
                            Fore.LIGHTRED_EX + "[FAILURE]" + Style.RESET_ALL + f" CI SONO STATE DELLE COMPLICANZE NEL MANDARE IL MOD tiktok {typeban} PER @" + user[k].upper() + " CHE SBANYOO NON RIESCE A GESTIRE")


                b += 1
                k+=1
            message("CICLI DI MODULI SU TUTTE LE PAGE FATTO! ")
            sleep(tempoc)
            aggiornamentofile(nomefile)
    except Exception as e:
        print(e)
        print("bot error")
        try:
            if logins == "si":
                insta = login()
        except:
            pass
        message(" ERRORE BOT, BOT FERMO")
        quit()
def lettura(df):
    try:
        global username, password, msg, paese, tempo, tempoc, scelta, logins, cmb, proxi, nomepc,verprox,dati,prox, righe, motind, indmotper, contindmot, mailind, indmailper, contindmail
        cont = 1
        righe = df.shape[0]
        nomepc = df.iloc[0][1]
        msg = df.iloc[0][2]
        textmom = df.iloc[0][11]
        paese = df.iloc[0][12]
        tempo = int(df.iloc[0][13])
        tempoc = int(df.iloc[0][14])
        logins = (str(df.iloc[0][15])).lower()
        cmb = (str(df.iloc[0][16])).lower()
        try:
            prox = (str(df.iloc[0][17])).lower().split("@")
        except:
            pass
        if prox[0] != "nan":
            proxi = prox[1] + "@" + prox[0]
            verprox = True
        else:
            verprox = False
        if logins.lower() == "si":
            if logins.lower() == "si":
                nomefile1 = df.iloc[0][0]
                try:
                    file = open("/Users/PYTHONBOT/TELEGRAMDATA/" + nomefile1 + ".txt", "r")
                    linea = file.readline()
                    dati = linea.split(";")

                except:
                    print(Fore.LIGHTRED_EX + ' PROFILO INESISTENTE, NON SARA EFFETTUATO IL LOGIN' + Fore.LIGHTWHITE_EX)
                    logins = "no"
        for cont in range(1,righe):
            user[cont], nomis[cont], maill[cont], phonis[cont], modd1[cont], modd2[cont], modd3[cont], modd4[cont], \
            modd5[
                cont], modd6[cont], modd7[cont], path[cont], text[cont] = df.iloc[cont][0], df.iloc[cont][1], df.iloc[cont][
                2], phones(), df.iloc[cont][3], df.iloc[cont][4], df.iloc[cont][5], df.iloc[cont][6], df.iloc[cont][7], \
                                                              df.iloc[cont][8], df.iloc[cont][9], df.iloc[cont][10],df.iloc[cont][11]

            if str(text[cont]).lower() == "nan":
                text[cont] = textmom
            motind[cont] = text[cont].split(";")
            contindmot[cont] = len(motind[cont])
            indmotper[cont] = 0
            mailind[cont] = maill[cont].split(";")
            contindmail[cont] = len(mailind[cont])
            indmailper[cont] = 0


        scelta = righe

        print(Fore.LIGHTGREEN_EX + "\n\n[SUCCESS]" + Style.RESET_ALL + "RILETTURA ESEGUITA CORRETTAMENTE SENZA NESSUN ERRORE ")
    except:
        print(Fore.LIGHTGREEN_EX + "\n\n[FAILURE]" + Style.RESET_ALL + "RILETTURA NON ESEGUITA CORRETTAMENTE")
def aggiornamentofile(nomefile):
    global df
    try:
        df = pd.read_excel(nomefile)
        lettura(df)
    except:
        print('rilettura file fallita')
if __name__ == "__main__":
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '                    SBANYOO TK' + Style.RESET_ALL)
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    global insta, client, nomefile, tentativi
    tentativi = 0
    modplus = 1
    init(convert=False)
    send = False
    df = None
    verprox = True
    txt = ""
    prox = ["nan", "nan"]
    count, nomis, user, maill, phonis, modd1, modd2, modd3, modd4, modd5, modd6, modd7, path, sban, dati, text, motind, indmotper, contindmot, mailind, indmailper, contindmail = {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list: 1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}, {
                                                                                                               list:1000000}
    while True:
        try:
            try:
                nomefile = input( Fore.LIGHTGREEN_EX + "[INPUT FILE]" + Style.RESET_ALL + ' INSERISCI IL PERCORSO DEL FILE EXCEL: ').replace('"',"")
                if nomefile == "t" or nomefile=="":
                    nomefile = r"C:\PYTHONBOT\ACCOUNTABBANDONATI.xlsx"
                nomefile = nomefile.strip()
                df = pd.read_excel(nomefile.strip())
                break
            except Exception as e:
                print(e)
                print(Fore.LIGHTRED_EX + "[ERRORE]" + Style.RESET_ALL + ' FILE NON TROVATO')

        except Exception as e:
            print(Fore.LIGHTRED_EX + "[ERRORE]" + Style.RESET_ALL + '  - FILE NON TROVATO - ')
    # lettura
    cont = 1
    righe = df.shape[0]
    nomepc = df.iloc[0][1]
    msg = df.iloc[0][2]
    textmom = df.iloc[0][11]
    paese = df.iloc[0][12]
    tempo = int(df.iloc[0][13])
    tempoc = int(df.iloc[0][14])
    logins = (str(df.iloc[0][15])).lower()
    cmb = (str(df.iloc[0][16])).lower()
    try:
        prox = (str(df.iloc[0][17])).lower().split("@")

    except:
        pass
    if prox[0] != "nan":
        proxi = prox[1] + "@" + prox[0]
        verprox = True
    else:
        verprox = False
    if logins.lower() == "si":
        if logins.lower() == "si":
            nomefile1 = df.iloc[0][0]
            try:
                file = open("/Users/PYTHONBOT/TELEGRAMDATA/" + nomefile1 + ".txt", "r")
                linea = file.readline()
                dati = linea.split(";")

            except:
                print(Fore.LIGHTRED_EX + ' PROFILO INESISTENTE, NON SARA EFFETTUATO IL LOGIN' + Fore.LIGHTWHITE_EX)
                logins = "no"
    for cont in range(1,righe):
        user[cont], nomis[cont], maill[cont], phonis[cont], modd1[cont], modd2[cont], modd3[cont], modd4[cont], modd5[
            cont], modd6[cont], modd7[cont], path[cont], text[cont] = df.iloc[cont][0], df.iloc[cont][1], df.iloc[cont][
            2], phones(), df.iloc[cont][3], df.iloc[cont][4], df.iloc[cont][5], df.iloc[cont][6], df.iloc[cont][7],df.iloc[cont][8], df.iloc[cont][9], df.iloc[cont][10],df.iloc[cont][11]
        if str(text[cont]).lower() == "nan":
            text[cont] = textmom
        motind[cont] = text[cont].split(";")
        contindmot[cont] = len(motind[cont])
        indmotper[cont] = 0
        mailind[cont] = maill[cont].split(";")
        contindmail[cont] = len(mailind[cont])
        indmailper[cont] = 0




    scelta = righe

    for indice in range(1,righe-1):



        count[indice] = 1
        sban[indice] = 0

    # finelettura
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '                     RIEPILOGO' + Style.RESET_ALL)
    print(Fore.BLUE + "------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Nome pc: ' + Fore.RED + nomepc.upper())
    if logins.lower() == "si":
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Numero che manda lo status bot: ' + Fore.RED + str(dati[0]).upper())
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Il messaggio arriva a: ' + Fore.RED + msg.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Paese: ' + Fore.RED + paese.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + ' Login Status: ' + Fore.RED + logins.upper())
    print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " SBAN METHOD: " + Fore.RED + "SBAN +")
    if prox[0] != "nan":
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " PROXY STATUS: " + Fore.RED + "ON")
    else:
        print(Fore.LIGHTBLUE_EX + '[-]' + Style.RESET_ALL + " PROXY STATUS: " + Fore.RED + "OFF")
    print(Fore.BLUE + "------------------------------------------------------\n" + Style.RESET_ALL)
    if logins == "si":
        insta = login()
    mod(user, tempo)