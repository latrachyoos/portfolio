import random
import string
from time import sleep

from requests_toolbelt import MultipartEncoder
import requests

r = requests.Session()
link = "https://www.tiktok.com/login?redirect_url=https%3A%2F%2Fwww.tiktok.com%2F&lang=en&enter_method=mandatory"

req = r.get(url=link)
tt_csrf_token = req.cookies["tt_csrf_token"]
ttwid=req.cookies["ttwid"]
cookie ="s_v_web_id=verify_lb9bmm6w_NWpt7ook_4Fhy_43at_B9v4_kfxhODlB0dBq; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22};"+f"tt_csrf_token={tt_csrf_token}; ak_bmsc=22F55612299D134CF540A3DF21D27E91~000000000000000000000000000000~YAAQZbg1VCQnpHSEAQAAyDAQ3RK9Uj+fLje9JDCY7M0Xfha1MBYL80+kUcjTXIluw6gHfOJP1964BCM2+k4zElJ2OADr6xG05Spo5YPqu3v2NKr2t8QlH78SsgOqCEZw0pi82aeGlYaitaW5DqmWbCE8/scRt8go+tofvUFBdJmWUwj1Ls4tqnHfE6ubq3QgXax/ZMzul/gYvrQzMGvrr/X5oYc5s/QfdvRQ18dZ8Q8QQJq3gqYcUdrKJGB9fjsVz9fhJduKkoKDC4Fs3t9emPyKNM+2CnO0SXW39nZltAcfGPHkEBwTnZVubXOONulfjL0tFFn+X5kl1WMT/2KTJk5cRl0McD3j2RGQCZEIkSagwZ8pI04oCQJUhYvpN6GEMjr9bffeR/4=; ttwid={ttwid};"+" __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227173265919224989189%22%2C%22timestamp%22:1670156138410};"+f" ttwid={ttwid}; msToken=G7OPWV35oFjdRF3GFmlmD-S_4vm9v_8doBILTygW-iRUI8YQj6hxqsb2SUeNh7parBlKnQiOKRnDeC9mug0d9yQAsaSwc3XmivjALlBVLZ5SOvjKGWCx; msToken=G7OPWV35oFjdRF3GFmlmD-S_4vm9v_8doBILTygW-iRUI8YQj6hxqsb2SUeNh7parBlKnQiOKRnDeC9mug0d9yQAsaSwc3XmivjALlBVLZ5SOvjKGWCx"





data = {
    "verify": "0",
    "email": "spun50gr@gmail.com",
    "username": "undefined",
    "option": "Account ban/suspension",
    "feedback": "help me to unban me please aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "agreement": "I ensure, to the best of my ability and knowledge, that all the information disclosed above is accurate and true.,By submitting, I acknowledge that TikTok will process my data in accordance with TikTok's Privacy Policy.",
    "option2": "Banned account (age-related)",
    "formTopicVal": "feedback_webform_dropdown_main_opt2",
    "formTellUsMoreVal": "feedback_webform_dropdown_main_opt2_c",
    "formReportReasonVal": "",

}
boundary = '----WebKitFormBoundary' \
           + ''.join(random.sample(string.ascii_letters + string.digits, 16))
print(boundary)
m = MultipartEncoder(fields=data, boundary=boundary)

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

link = "https://www.tiktok.com/legal/report/feedback/send"

req1 = r.post(url=link, headers=head, data=m)
print(req1.text)
print(r.cookies.get_dict())
print(req1.status_code)

r.close()
# cookie: s_v_web_id=verify_lb9bmm6w_NWpt7ook_4Fhy_43at_B9v4_kfxhODlB0dBq; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22}
# cookie: s_v_web_id=verify_lb9bmm6w_NWpt7ook_4Fhy_43at_B9v4_kfxhODlB0dBq; cookie-consent={%22ga%22:true%2C%22af%22:true%2C%22fbp%22:true%2C%22lip%22:true%2C%22bing%22:true%2C%22ttads%22:true%2C%22reddit%22:true%2C%22criteo%22:true%2C%22version%22:%22v9%22}
