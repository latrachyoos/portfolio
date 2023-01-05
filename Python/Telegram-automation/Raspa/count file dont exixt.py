import requests
proxies = {
  'http': 'http://xhyc3:qnzy5p30@169.197.83.74:6024',
  'https': 'http://xhyc3:qnzy5p30@169.197.83.74:6024'
}
response = requests.get('http://api.privateproxy.me:10738', proxies=proxies)
print(response.text)