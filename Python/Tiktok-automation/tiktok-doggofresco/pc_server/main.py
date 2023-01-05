import pyodbc, enlighten, os, random
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from ctypes import windll, byref, wintypes
from time import sleep
from art import text2art
from colorama import Fore, init
from colorama import Fore
global is_reboot
    #https://chrome.google.com/webstore/detail/fastsave-repost-for-insta/fdedigfpeejoaoicpppjcpicekleaedb/related estensione instagram


#function
def click_path(path):
    global driver
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, path))
    ).click()
def start():
    global driver
    os.system("TASKKILL /F /IM chrome.exe")
    options = Options()
    options.add_argument("start-maximized")
    # Chrome is controlled by automated test software
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    # avoiding detection
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--log-level=3")
    # Default User Profile
    file = open("chromesettings.txt","r")
    sett_chrome=file.read().split(";")

    options.add_argument("--profile-directory=" + sett_chrome[0])
    options.add_argument("--window-size=1936,1048")
    options.add_argument("--user-data-dir="+sett_chrome[1]) #user config

                                          #
    options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": r"C:\tiktok-doggofresco\media"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.tiktok.com/upload?lang=it-IT')

    link = send_query("select * from Link_progetto_canva", 3).fetchall()[0][0]
    driver.execute_script('''window.open("'''+link+'''","_blank");''')
    driver.execute_script('''window.open("https://snaptik.app/it","_blank");''')
    driver.execute_script('''window.open("https://tiktok.com","_blank");''')

    return driver

def send_query(query, case):
    global conn
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\tiktok-doggofresco\history_of_posts.accdb;')
    #
    cursor = conn.cursor()
    cursor.execute(query)
    if case != 3:
        conn.commit()
    return cursor
def canva_edit(path_video):
    global a, driver
    esisteva = False
    try:
        driver.switch_to.window(driver.window_handles[3])
        #driver.refresh()
        driver.switch_to.parent_frame()
        try:
            click_path(
                "/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div/button")
        except:
            click_path("/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[1]/div/div[1]/div/div[1]/div[4]/button")
        sleep(5)
        try:
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                               "/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/input"))).send_keys(
                    path_video)                                                #/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/input
            except:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                               "/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/input"))).send_keys(
                    path_video)                                               #/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/div/div/input
        except Exception as e:
            #print(e)
            pass


            #
        sleep(10)
        try:
            try:
                click_path(
                    "/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div[2]/div/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]")
                    #/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div
            except:
                click_path("/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[1]/div[1]/div/div[3]/div[3]/div/div[1]/div/div[2]/div/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div")
        except:

            click_path(
            "/html/body/div[2]/div/div/div/div[4]/div/div/aside/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div/div/div/section/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div/div/div")


        # condividi
        click_path("/html/body/div[2]/div/div/div/header/div/nav/div[3]/div[7]/div/div/div/div/div/div/button")
                   #/html/body/div[2]/div/div/div/header/div/nav/div[3]/div[7]/div/div/div/div/div/div/button
        click_path(
            "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div/div[5]/button[1]")
        while True:
            try:
                click_path(
                    "/html/body/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div[2]/div/form/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/button")
                break
            except:
                pass
        check_video = 0
        while True:
            try:
                rip = driver.find_element(By.XPATH,
                                          "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span").text
                #
                                         #/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/div[2]/div[2]/div/span
                if "Abbiamo riscontrato un errore" in rip:
                    click_path(
                        "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/span/a")


            except:
                if check_video > 500:
                    break
                sleep(1)
                check_video += 1


            lista = os.listdir("C:\\tiktok-doggofresco\\media")
            if len(lista) != 0:
                # print(lista[0])
                if "Progetto" in lista[0] and not "crdownload" in lista[0] and not ".tmp" in lista[0]:
                    try:
                        os.remove(path_video)
                    except:
                        pass
                    try:
                        click_path("/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/div[1]")
                    except:
                        driver.refresh()
                        sleep(5)

                    sleep(2)
                    driver.find_element(By.XPATH, "/html/body").send_keys(Keys.CONTROL + "z")
                    sleep(2)
                    """action = ActionChains(driver)
                    #(x=1184, y=605)
                    #(x=1222, y=573)
                    action.move_by_offset(1222, 573).click().perform()
                    sleep(1)
                    a = driver.switch_to.active_element
                    a.send_keys(Keys.DELETE)
                    action.reset_actions()"""
                    upload_on_tiktok("C:\\tiktok-doggofresco\\media\\" + lista[0])
                    os.remove("C:\\tiktok-doggofresco\\media\\" + lista[0])
                    sleep(1)
                    break
                else:
                    if "crdownload" in lista[0]:
                        esisteva = True
            else:
                check_video +=1
                if check_video > 2000:
                    break

                if esisteva == True:
                    click_path(
                        "/html/body/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/span/a")
                    esisteva = False

    except Exception as e:
        lista = os.listdir("C:\\tiktok-doggofresco\\media")
        if len(lista) != 0:
            if "mp4" in lista[0] and not "crdownload" in lista[0] and not ".tmp" in lista[0]:
                #upload_on_tiktok("C:\\tiktok-doggofresco\\media\\" + lista[0])
                pass


    #Link_progetto_canva




#download and post
def download_media_from_url_tiktok(link_tik):

    try:
        list = os.listdir("C:\\tiktok-doggofresco\\media")
        for files in list:
            try:
                os.remove("C:\\tiktok-doggofresco\\media\\" + files)
            except:
                pass
    except:
        pass
    try:
        driver.switch_to.window(driver.window_handles[2])
        driver.get("https://snaptik.app/it")
        click_path("/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]")
        driver.find_element(By.XPATH, "/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]").send_keys(link_tik)
        click_path("/html/body/main/section[1]/div[3]/div/div/form/button")
        ck_counter = 0
        while True:
            try:
                #driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/main/section[2]/div/iframe"))
                click_path("/html/body/main/section[2]/div/div/article/div[2]/div/a[1]")
                break
            except Exception as e:
                ck_counter +=1
                if ck_counter >10:
                    driver.get("https://snaptik.app/it")
                    click_path("/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]")
                    driver.find_element(By.XPATH,
                                        "/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]").send_keys(
                        link_tik)
                    click_path("/html/body/main/section[1]/div[3]/div/div/form/button")
                    ck_counter = 0


                #print(e)
                pass
        sleep(5)
        check_video = 0
        video_link_is_ok = True
        while True:
            try:
                driver.find_element(By.XPATH,"/html/body/pre")
                video_link_is_ok = False
                break
            except:
                lista = os.listdir("C:\\tiktok-doggofresco\\media")
                if len(lista) != 0:
                    if "mp4" in lista[0] and not "crdownload" in lista[0] and not ".tmp" in lista[0]:
                        canva_edit("C:\\tiktok-doggofresco\\media\\" + lista[0])
                        video_link_is_ok = True
                        break
                    else:
                        if ".tmp" in lista[0]:
                            try:
                                os.remove("C:\\tiktok-doggofresco\\media\\" + lista[0])
                            except:
                                pass
                        if check_video > 50:
                            driver.get("https://snaptik.app/it")
                            click_path("/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]")
                            driver.find_element(By.XPATH,
                                                "/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]").send_keys(
                                link_tik)
                            click_path("/html/body/main/section[1]/div[3]/div/div/form/button")
                            ck_counter = 0
                            while True:
                                try:
                                    # driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/main/section[2]/div/iframe"))
                                    click_path("/html/body/main/section[2]/div/div/article/div[2]/div/a[1]")
                                    break
                                except Exception as e:
                                    ck_counter += 1
                                    if ck_counter > 10:
                                        driver.get("https://snaptik.app/it")
                                        click_path("/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]")
                                        driver.find_element(By.XPATH,
                                                            "/html/body/main/section[1]/div[3]/div/div/form/div[2]/input[1]").send_keys(
                                            link_tik)
                                        click_path("/html/body/main/section[1]/div[3]/div/div/form/button")
                                        ck_counter = 0

                        if check_video > 200:
                            video_link_is_ok = False
                            break
                        check_video += 1
                        sleep(2.5)
        return video_link_is_ok
    except:
        pass
def download_media_from_instagram():
    try:
        list = os.listdir("C:\\tiktok-doggofresco\\media")
        for files in list:
            try:
                os.remove("C:\\tiktok-doggofresco\\media\\" + files)
            except:
                pass
    except:
        pass
    try:
        sleep(5)
        click_path(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[4]/div/span[1]")
        check_video = 0
        sleep(5)
        while True:
            lista = os.listdir("C:\\tiktok-doggofresco\\media")
            if len(lista) != 0:
                if "mp4" in lista[0] and not "crdownload" in lista[0] and not ".tmp" in lista[0]:
                    canva_edit("C:\\tiktok-doggofresco\\media\\" + lista[0])

                    break
                else:
                    if ".tmp" in lista[0]:
                        try:
                            os.remove("C:\\tiktok-doggofresco\\media\\" + lista[0])
                        except:
                            pass
                    if check_video > 500:
                        break
                    check_video += 1
                    sleep(5)




    except Exception as e:
        pass
        #print("a: " + e)



#post
def upload_on_tiktok(path_video):
    global driver, bio, n_bio, k
    try:
        #start()
        driver.switch_to.window(driver.window_handles[0])
        #driver.get('https://www.tiktok.com/upload?lang=it-IT')
        try:
            driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/iframe"))
        except:
            pass

        #click_path("/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button")
        sleep(10)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/input"))
        ).send_keys(path_video)
        sleep(10)


        check = 0
        sleep(5)
        while True:
            try:
                driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]")
                                              #/html/body/div[1]/div/div/div/div/div[2]/div[1]/div[2]
                try:
                    try:

                        driver.find_element(By.CSS_SELECTOR,
                                            "#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div").send_keys(
                            Keys.CONTROL + "a")
                        ##root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div > div > div > div
                        ##root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div > div > div > div

                        driver.find_element(By.CSS_SELECTOR,
                                            "#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div").send_keys(
                            Keys.BACKSPACE)
                    except:
                        pass
                    try:
                        bio_da_usare = bio[k]
                        k += 1
                        if k >= n_bio - 1:
                            k = 0
                    except:
                        bio_da_usare = bio[0]

                    sleep(5)
                    try:

                        driver.find_element(By.CSS_SELECTOR,
                                            "#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.jsx-2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div").send_keys(
                            bio_da_usare + " ")
                    except:
                        driver.find_element(By.CSS_SELECTOR,
                                            "#root > div > div > div > div > div.jsx-410242825.contents-v2 > div.j2580397738.form-v2 > div.jsx-2580397738.caption-wrap-v2 > div > div:nth-child(1) > div.jsx-1717967343.margin-t-4 > div > div.jsx-1043401508.jsx-723559856.jsx-1657608162.jsx-3887553297.editor > div > div > div").send_keys(
                            bio[0] + " ")


                except:
                    pass
                sleep(10)

                try:
                    sleep(2)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                   # e = driver.find_element(By.CLASS_NAME,"css-1ielthz").click()
                    e = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]').click()
                    action = ActionChains(driver)
                    action.move_by_offset(e.location["x"], e.location["y"]).double_click().perform()
                    action.reset_actions()
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]').click()

                except:
                    pass
                print("fatto")
                break
            except Exception as e:
                sleep(1)
                print(e)
                check+=1
                if check > 1000:
                    print("stop")
                    break
                #print("eee" + str(e))

        video = 0
        sleep(120)
        while True:
            try:
                click_path("/html/body/div[3]/div/div/div[1]/div[2]")
                break
            except:
                video +=1
                if video > 2:
                    break
                pbar = enlighten.Counter(total=10000, desc='PAUSA X SPAM', unit='ticks', color="red")
                for _ in range(10000):
                    pbar.update()
                    sleep(1)
                click_path("/html/body/div[1]/div/div/div/div/div[2]/div[2]/div[7]/div[2]/button")
    except Exception as e:
        print(e)




#engine post inteligence
def post_engine_tiktok():
    global is_reboot, driver, cont
    if not is_reboot:
        driver = start()
    is_reboot = True
    print("chrome avviato...\/")
    sleep(10)
    while True:

        cursor_users = send_query("SELECT USERNAME FROM USERS where type='tk'", 3).fetchall()
        random.shuffle(cursor_users)
        for row in cursor_users:
            try:
                driver.switch_to.window(driver.window_handles[1])
                driver.get("https://www.tiktok.com/@" + row[0])
                driver.switch_to.parent_frame()
                click_path("/html/body/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/a")
                error_counter = 0
                while True:
                    link = driver.current_url.split("?")[0]
                    query = "select link from links where link = '" + link + "'"
                    cursora = send_query(query, 3)
                    if len(cursora.fetchall()) == 0:
                        if download_media_from_url_tiktok(link) == True:
                            results = send_query("select id_user from users where username='" + row[0] + "'", 3)
                            id = results.fetchall()[0][0]
                            # print(id)
                            today = datetime.now()
                            # print("insert into links (id_user, link,data) values ("+str(id)+", '"+link+"',#"+today.strftime("%d/%m/%Y")+"#)")
                            send_query("insert into links (id_user, link,data) values (" + str(
                                id) + ", '" + link + "',#" + today.strftime("%d/%m/%Y") + "#)", 1)
                            # print("fatto! ora pausa")
                            pbar = enlighten.Counter(total=pausa, desc='PAUSA IN SEC', unit='ticks', color="green")
                            for _ in range(pausa):
                                pbar.update()
                                sleep(1)
                            print(today.strftime("%m/%d/%Y, %H:%M:%S"))
                            cont +=1
                            if cont > 5:
                                driver.quit()
                                driver = start()
                                cont = 0
                            break
                        else:

                            sleep(0.5)
                            try:
                                click_path("/html/body/div[2]/div[2]/div[3]/div[1]/button[3]")
                            except:
                                try:
                                    driver.find_element(By.XPATH,
                                                        "/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]/button[1]")
                                except:
                                    pass
                            if error_counter == 10000:
                                break
                            error_counter += 1
                    else:
                        results = send_query("select id_user from users where username='" + row[0] + "'", 3)
                        id = results.fetchall()[0][0]
                        # print(id)
                        today = datetime.now()
                        # print("insert into links (id_user, link,data) values ("+str(id)+", '"+link+"',#"+today.strftime("%d/%m/%Y")+"#)")
                        send_query("insert into links (id_user, link,data) values (" + str(
                            id) + ", '" + link +"/error_snap" + "',#" + today.strftime("%d/%m/%Y") + "#)", 1)
                        sleep(0.5)
                        try:
                            click_path("/html/body/div[2]/div[2]/div[3]/div[1]/button[3]")
                        except:
                            try:
                                driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[2]/button[1]")
                            except:
                                pass

                        if error_counter == 10000:
                            break
                        error_counter += 1
            except Exception as e:
                #print(e)
                pass
def post_engine_instagram():
    global is_reboot, driver, cont
    if not is_reboot:
        driver = start()
    is_reboot = True
    print("chrome avviato...\/")
    sleep(10)
    while True:
        cursor_users = send_query("SELECT USERNAME FROM USERS ", 3).fetchall()
        random.shuffle(cursor_users)
        for row in cursor_users:
            try:
                driver.switch_to.window(driver.window_handles[1])
                driver.get("https://www.instagram.com/" + row[0])
                sleep(2)
                try:
                    click_path("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a")
                except:
                    click_path("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a")
                error_counter = 0

                while True:
                    try:
                        sleep(2)
                        try:
                            click_path("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div[4]/button")
                                   #/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div[4]/button
                        except:
                            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div/div/div/div/video")
                        try:
                            link = driver.current_url
                            query = "select link from links where link = '"+link + "'"
                            cursora  = send_query(query, 3)
                            if len(cursora.fetchall()) == 0:
                                download_media_from_instagram()
                                results = send_query("select id_user from users where username='"+row[0]+"'",3)
                                id = results.fetchall()[0][0]
                                #print(id)
                                today = datetime.now()
                                #print("insert into links (id_user, link,data) values ("+str(id)+", '"+link+"',#"+today.strftime("%d/%m/%Y")+"#)")
                                send_query("insert into links (id_user, link,data) values ("+str(id)+", '"+link+"',#"+today.strftime("%d/%m/%Y")+"#)",1)
                                #print("fatto! ora pausa")
                                pbar = enlighten.Counter(total=pausa, desc='PAUSA IN SEC', unit='ticks', color="green")
                                for _ in range(pausa):
                                    pbar.update()
                                    sleep(1)
                                print(today.strftime("%m/%d/%Y, %H:%M:%S"))
                                cont += 1
                                if cont > 5:
                                    driver.quit()
                                    driver = start()
                                    cont = 0
                                break


                            else:
                                if error_counter > 0:
                                    click_path(
                                        "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                                else:
                                    click_path(
                                        "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")
                                if error_counter == 5000:
                                    break
                                error_counter +=1
                        except Exception as e:
                            #print(e)
                            try:
                                if error_counter > 0:
                                    click_path("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                                    #           /html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button
                                else:
                                    click_path(
                                    "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")

                            except:
                                pass
                    except Exception as e:
                        #print(e)
                        if error_counter > 0:
                            click_path(
                                "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button")
                        else:
                            click_path(
                                "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button")
                        if error_counter == 5500:
                            break
                        error_counter += 1
            except Exception as e:
                pass#print("ee" + str(e))

if __name__=="__main__":


    """
    cd\
    cd tiktok-doggofresco
    python main.py
    
    """
    __author__ = "latrachyoo S.P.A"
    __copyright__ = "Copyright (C) 2921 " + __author__
    __license__ = "Private Domain"
    __version__ = "6.0"
    init(convert=True)
    STDOUT = -11

    hdl = windll.kernel32.GetStdHandle(STDOUT)
    rect = wintypes.SMALL_RECT(0, 35, 74, 74)  # (left, top, right, bottom)
    windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))
    print(Fore.LIGHTWHITE_EX + "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n--------------------------------------------------------------------------")
    print('                        BENVENUTO NEL TUO BOT REPOST')
    print(Fore.LIGHTWHITE_EX + '                          DEVOLPED BY LATRACHYOO')
    print("--------------------------------------------------------------------------")
    text = ('                   MEDIA')
    rI = text2art(text)
    print(Fore.LIGHTRED_EX + "" + rI)
    text = ('      REPOSTYOO')
    r = text2art(text)
    stri = "latrachyoo devolpment sys"
    print(Fore.LIGHTRED_EX + r)
    print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
    print(Fore.WHITE + '                                VERSIONE ' + __version__)
    print(Fore.LIGHTWHITE_EX + "--------------------------------------------------------------------------")
    #i am posting automatically with a python bot, taking posts from different instagram users #repost #python #instagram #automation
    global query,pausa, select, n_bio
    k = 0
    cont = 0
    bio = {list: 1000}
    is_reboot = False
    while True:
        if not is_reboot:
            try:
                select = int(input("Scegli cosa fare: \n"
                                  
                                   "- [1] Aggiungere uno user IG. \n"
                                   "- [2] Rimuovere uno user IG/TK. \n"
                                   "- [3] Edita link progetto canva.\n"
                                   "- [4] Visualizza link di canva.\n"
                                   "- [5] Visualizza tutti gli users IG.\n"
                                   "- [6] START BOT! ->IG \n"
                                   
                                   "- [7] Aggiungere uno user TIKTOK. \n"
                                   "- [8] Visualizza tutti gli users TIKTOK.\n"
                                   "- [9] START BOT! ->TIKTOK \n"
                                   " --> "))
                match str(select):

                    case "1":
                        user = input("- INSERISCI UNO USERNAME VALIDO DA AGGIUNGERE SENZA @: ").replace("@", "").strip()
                        query = "insert into users(username, type) values('" + user + "','ig')"
                        query_di_ver = "select count(username) as c from users where username='"+user+"' and type = 'ig'"
                        res = send_query(query_di_ver, 3).fetchall()[0][0]

                        if str(res).strip() == "0":
                            send_query(query, select)
                            print("\nuser aggiunto!\n\n\n")
                        else:
                           print("\nesiste già uno user!\n\n\n")

                    case "2":
                        user = input("- INSERISCI UNO USERNAME VALIDO DA RIMUOVERE SENZA @: ").replace("@", "").strip()
                        query = "DELETE from users WHERE USERNAME='" + user + "'"
                        query_di_ver = "select count(username) as c from users where username='" + user + "'"
                        res = send_query(query_di_ver, 3).fetchall()[0][0]

                        if str(res).strip() != "0":
                            send_query(query, select)
                            print("\nuser rimosso!\n\n\n")
                        else:
                            print("\nnessun user esistente\n\n\n")
                    case "3":
                        link_da_aggiungere = input("[LINK] - INCOLLA IL LINK DEL PROGETTO DI CANVA: ")
                        link = send_query("select * from Link_progetto_canva", 3)
                        if len(link.fetchall()) == 0:
                            send_query("insert into Link_progetto_canva(link) values ('"+link_da_aggiungere+"')", 1)

                        else:
                            send_query("delete from Link_progetto_canva", 1)
                            send_query("insert into Link_progetto_canva(link) values ('" + link_da_aggiungere + "')", 1)




                    case "4":
                        link_canva = send_query("select * from Link_progetto_canva", 3)
                        try:
                            link_canv = link_canva.fetchall()[0][0]
                        except:
                            link_canv = 0

                        if link_canva ==0:
                            print("\n\n\n nessun link \n\n\n")
                        else:

                            print("\n\n\n "+link_canv+"\n\n\n")



                    case "5":
                        cursor = send_query("SELECT USERNAME FROM USERS where type='ig' ",3)
                        if len(cursor.fetchall())==0:
                            print("lista vuota!\n\n\n")
                        else:
                            print("\n\n\n")
                            cursor = send_query("SELECT USERNAME FROM USERS where type='ig' ",3).fetchall()
                            random.shuffle(cursor)
                            for row in cursor:
                                print(row[0])
                            print("\n\n\n")

                    case "6":

                        cursor = send_query("SELECT USERNAME FROM USERS where type='ig'", 3)
                        if len(cursor.fetchall()) == 0:
                            print("lista vuota, aggiungere almeno uno user!\n\n\n")

                        else:
                            have_link = send_query("select * from Link_progetto_canva", 3)
                            if len(have_link.fetchall()) == 0:
                                print("Inserire un link progetto canva!\n\n\n")

                            else:
                                while True:
                                    try:
                                        pausa = int(input("[SLEEP IN SECONDI] Scrivi una pausa in secondi senza 'sec etc.': "))
                                        break
                                    except:
                                        print("inserisci una pausa in secondi valida")
                                while True:
                                    try:
                                        n_bio = int(input("[n_bio] QUANTE BIO VUOI USARE: "))
                                        for _ in range(n_bio):
                                            while True:
                                                bio_mom = input("[BIO " + str(_+1) + "] Inserisci una descrizione.: ")
                                                if len(bio_mom) > 149:
                                                    print("bio troppo lunga: " + str(len(bio_mom)) + r"\150")
                                                else:
                                                    bio[_] = bio_mom
                                                    break

                                        break
                                    except:
                                        print("inserisci un numero bio valido")
                                post_engine_instagram()
                    case "7":
                        user = input("- INSERISCI UNO USERNAME VALIDO DA AGGIUNGERE SENZA @: ").replace("@", "").strip()
                        query = "insert into users(username, type) values('" + user + "','tk')"
                        query_di_ver = "select count(username) as c from users where username='" + user + "' and type = 'tk'"
                        res = send_query(query_di_ver, 3).fetchall()[0][0]

                        if str(res).strip() == "0":
                            send_query(query, select)
                            print("\nuser aggiunto!\n\n\n")
                        else:
                            print("\nesiste già uno user!\n\n\n")
                    case "8":
                        cursor = send_query("SELECT USERNAME FROM USERS where type='tk' ", 3)
                        if len(cursor.fetchall()) == 0:
                            print("lista vuota!\n\n\n")
                        else:
                            print("\n\n\n")
                            cursor = send_query("SELECT USERNAME FROM USERS where type='tk' ", 3).fetchall()
                            random.shuffle(cursor)
                            for row in cursor:
                                print(row[0])
                            print("\n\n\n")
                    case "9":
                        cursor = send_query("SELECT USERNAME FROM USERS where type='tk' ", 3)
                        if len(cursor.fetchall()) == 0:
                            print("lista vuota, aggiungere almeno uno user!\n\n\n")

                        else:
                            have_link = send_query("select * from Link_progetto_canva", 3)
                            if len(have_link.fetchall()) == 0:
                                print("Inserire un link progetto canva!\n\n\n")

                            else:
                                while True:
                                    try:
                                        pausa = int(
                                            input("[SLEEP IN SECONDI] Scrivi una pausa in secondi senza 'sec etc.': "))
                                        break
                                    except:
                                        print("inserisci una pausa in secondi valida")
                                while True:
                                    try:
                                        n_bio = int(input(
                                            "[n_bio] QUANTE BIO VUOI USARE: "))
                                        for _ in range(n_bio):
                                            while True:
                                                bio_mom = input("[BIO "+str(_+1)+"] Inserisci una descrizione.: ")
                                                if len(bio_mom) > 149:
                                                    print("bio troppo lunga: " + str(len(bio_mom)) + r"\150")
                                                else:
                                                    bio[_] = bio_mom
                                                    break

                                        break
                                    except:
                                        print("inserisci un numero bio valido")
                                #print(bio)
                                post_engine_tiktok()


            except Exception as e:
                #C:\tiktok-doggofresco\media\Snaptik_7126478594699758853_pota-boyz.mp4
                print(e)
                print("\ninserire una opzione valida!\n\n\n")
        else:
            if select==6:
                post_engine_instagram()
            else:
                post_engine_tiktok()

