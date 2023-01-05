from time import sleep

import requests
import sqlite3
def send_to_telegram(text):
    idchat = conn.execute("select channel from channel")
    apiToken = '5877675763:AAF4afrDXWY0i-DXIQL6-ZFrj3dC62_Zrjg'
    chatID = idchat.fetchall()[0][0]
    chatID = chatID.replace("/channel","")
    chatID = chatID.replace("/CHANNEL", "")
    chatID = chatID.replace(" ", "")
    #print(chatID)

    apiURL = f"https://api.telegram.org/bot{apiToken}/sendMessage?chat_id={chatID}&text={text}"

    try:
        response = requests.post(apiURL)
        print(response.text)
    except Exception as e:
        print(e)
def checktk(username):
    link = f"https://www.tiktok.com/@{username}"
    head = {

        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "cookie": "ttwid=1%7CMBsQDwEMlohHPtwjfiep6wgpTTpvNgHPmG0i5yp-0xs%7C1670790333%7C096edb9d6f758e1b525a9836119d6b3519fa31aa1279786562a9501ad08d4627; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227175989789448128006%22%2C%22timestamp%22:1670790334707}; passport_csrf_token=daf06e82e8a9f8cc6d212a7bbdbb23a5; passport_csrf_token_default=daf06e82e8a9f8cc6d212a7bbdbb23a5; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22}; tt_csrf_token=tUhDWECH-HHliKKfgByfwurfp0JHc2X2MQ9I; ak_bmsc=D64A38C46D20E6046BE3012BE26BB806~000000000000000000000000000000~YAAQVrg1VM9IcwSFAQAASaw7CxK5CShgEQPecak347DWmjcb/aPGchXL70J0WEla0WbmcEnWxuqmvQPvTbJVR8f8Ie0v7JuSZ2ZtYtz/NV476BbiRQqsIcrY7uZCMTPQEvmEEih7mcNJIeb0xbNzBhYqSuLjsqJk1krPZ/kOPIlV5yiN8drrTdZ7lMDuYHw03qQtoJ9Tr61u68rRtuUgrho3jI1mCtb3gZrARW+ZKx+WqJNSdf8VPknCE8a/b9jClJaFkYQ0GXgvJMoKwJfEuZAw8NZFBZz9NXIlbIpZIO4IK4x/UAJ6akmfmtroE1we+FvSQcsWRv7eWyDK0jo1N5OOeWH2jt9saQqaDxA7STwiZ6qTPHb9aOPcUsQtpxKyTvVk4o6GNJs=; s_v_web_id=verify_lbm50tno_6ZHt8c3c_lr40_4a7C_9UlC_Izli2G8hYY1Z; d_ticket=c2f1763154d3d1342e503cec61b586ca8b141; cmpl_token=AgQQAPPhF-RO0o3Jv8B_9508-felgih9_4RqYMtoeg; passport_auth_status=9992e17ce841a7659d390e0764a62e83%2C; passport_auth_status_ss=9992e17ce841a7659d390e0764a62e83%2C; sid_guard=fca8c2f7a50ce367e6fdc73e7e0ca99e%7C1670930794%7C5184000%7CSat%2C+11-Feb-2023+11%3A26%3A34+GMT; uid_tt=2b9d379a0e3258fbd05c95ee293fa417e04307868b15b3a7372cf2df692ad5ef; uid_tt_ss=2b9d379a0e3258fbd05c95ee293fa417e04307868b15b3a7372cf2df692ad5ef; sid_tt=fca8c2f7a50ce367e6fdc73e7e0ca99e; sessionid=fca8c2f7a50ce367e6fdc73e7e0ca99e; sessionid_ss=fca8c2f7a50ce367e6fdc73e7e0ca99e; sid_ucp_v1=1.0.0-KDYzNzUxMzRjNzEwM2VjNDhkMjllN2EzOTEwNWRlZWRhODYxNDBkNjYKIAiFiJW-_6zU-10Q6sLhnAYYswsgDDDGpd3vBTgCQPEHEAMaBm1hbGl2YSIgZmNhOGMyZjdhNTBjZTM2N2U2ZmRjNzNlN2UwY2E5OWU; ssid_ucp_v1=1.0.0-KDYzNzUxMzRjNzEwM2VjNDhkMjllN2EzOTEwNWRlZWRhODYxNDBkNjYKIAiFiJW-_6zU-10Q6sLhnAYYswsgDDDGpd3vBTgCQPEHEAMaBm1hbGl2YSIgZmNhOGMyZjdhNTBjZTM2N2U2ZmRjNzNlN2UwY2E5OWU; store-idc=maliva; store-country-code=it; store-country-code-src=uid; tt-target-idc=useast1a; tt-target-idc-sign=OTu6Bemo_60FctqKXz4jlHMimh9TAfqoeFwfNYJtBl0q9vfFkn_TDRhaS-yIx0cP_GKyYPe8sY3fhIW55jBF3B8kgHUrg2VNWt2LTAcHn0wo6cbAgc7y_ZZJe_4YIYu1i4yW4ijPHfkypVW9va0XhCkrRhMBE0edszx6FNQ_uClWzhTUntB89eIxK8q5G-JFzTbjQ25r_W4VD3-1denwdwL9Qu4iSw2-qKQKXSqkZG6otTiiuAvghlWQt8VcXoIxM38RcXbE53vucVQbh6taewhqGPVae5OGe88EVMV86zmK1VB8rTFGvl6smtlHwBxPgAaQ1G0ZVtAOFF_NpQDaLvFlcgwxfvu85DX0whvb6sJdD6ivQ2j3LOySGfM3XQiasO5gE303OcJIvJWZvOGfxX5AAjbGZjVGEV6vYmKBko1gXY-EH66AQUjoZLfEDafci3_BCEN_2_IcjNlTx3XqjyzL1HtS6U2Ecx61y15H86moV0KlqqcsG6mT5tbgJ9Q1; tt_chain_token=a5jPPrthnfA1/YABuiPFAQ==; tiktok_webapp_theme=dark; csrf_session_id=b2698afcbe206271353b7303ed3a98cb; bm_mi=B19FA8594318E24F3B679A71498BF6E4~YAAQVrg1VAFJcwSFAQAA++U8CxLuRI+6nDPNOSUxjRWhlI5jG3LvawKCLyjUOW1w4SKIpdbtvmOQdDoIABN5XPWwtzvLv5JkpOzy2+fpJxvD4tIru4a0JejZd3zrz/8kFbP5Bf37+GeHqzT3XE2yQ+L3EF6bP3l1MVNfB6+8QO/VF7iI4ls1z/Tz1RDsz6eWb1lbgEDnBzccdL/3tqMJVucF8gMaG0C7IKt0fXxzGjLYzdCv2KGHAEuYsAbes0o9qOb+moxyHiJv1zMEWQZ/q3P5E4JfLy0j120thmPVqfxNejZDgKJsxc5GCSKcdW4/NlRXW9Vf17w=~1; odin_tt=571a7446c4cc083fb5745f60b091d179dc6df5b1de1c22df03b9333c8bd9d654a5d819ddefe58b7b788ec7ad186b0d8689167ddb0df974c6bb149e0b6b690fbe05e0ce88c837635659b15b4d369b111a; ttwid=1%7CMBsQDwEMlohHPtwjfiep6wgpTTpvNgHPmG0i5yp-0xs%7C1670930822%7C09236097efbeea345797e94f0369e794034bc9e0cd2843e81abf2ed69bc2438c; bm_sv=344F5357CE3C585FDA242A6DE114A9D1~YAAQVrg1VAlJcwSFAQAAjAI9CxKqquPRaJku7bMJCjK3GXfb479oy/FX3Gc+6L+ubk2EX7uB4VQlh/XipGd8f3vz51r+aVzHQvzhgwJ6IzdPXAfuuXBse357BlX5wRW9qBjQ5jU0H7kdpqLZ0Vze6+ZfM2q1RXgSsZw1IpZ/iD4UAPYPpvQk461xLzL+nfasAlzhpWvzX+Iq4jCHTOL5wk5z/bsD2OGQO1smqJ4kmyKxhd16jCWQKFXWPa9/plNgZQ==~1; msToken=IgBLL8SDKJewIeHUnIH_KPP_Jt4JLDLGaClLYgD9_hZyX3s6IaofhK-8dWfoRt6gE5RkuW4lb_4Q6GYM8886NosKuWEcLJKJnHIKXN66JQndPPK5z8AxQ7zvr9Bvtgmb3GMLBw==; msToken=IgBLL8SDKJewIeHUnIH_KPP_Jt4JLDLGaClLYgD9_hZyX3s6IaofhK-8dWfoRt6gE5RkuW4lb_4Q6GYM8886NosKuWEcLJKJnHIKXN66JQndPPK5z8AxQ7zvr9Bvtgmb3GMLBw==; passport_fe_beating_status=false",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    }

    r = requests.session()
    req = r.get(link, headers=head)
    status = req.status_code
    cod = status
    text = req.text
    print(text[0:500])
    if "ultimo video di ." in text or str(status) == "404":
        cod = "0"
    else:
        cod = "1"

    return cod


conn = sqlite3.connect("tkcheck.sql", check_same_thread=False)

while True:
    sql = "select open from open"
    open = conn.execute(sql).fetchall()[0][0]
    if open == 1:
        sql = "select distinct user from users where type='tk' order by id desc"
        rows = conn.execute(sql)
        for row in rows.fetchall():
            print(row[0])
            sleep(15)
            code = checktk(row[0])
            if str(code) == "1":
                send_to_telegram(f"tiktok.com/@{row[0]} ACTIVE ✅")
            elif str(code) != "0":
                send_to_telegram(f"Latrachyoo_bot non riesce a capire la situazione di: {row[0]}, \nerrore:  -> {code}")


