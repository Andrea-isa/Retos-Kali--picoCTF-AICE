# Cookies
## Objetivo
Who doesn't love cookies? Try to figure out the best one. [http://mercury.picoctf.net:29649/](http://mercury.picoctf.net:29649/)
## Soluciòn
```shell
for i in {0..25}; do curl -s http://mercury.picoctf.net:29649/check -H "Cookie: name=$i"; done | grep picoCTF

┌──(kali㉿kali)-[~]
└─$ for i in {0..25}; do curl -s http://mercury.picoctf.net:29649/check -H "Cookie: name=$i"; done | grep picoCTF
            <p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{3v3ry1_l0v3s_c00k135_a1f5bdb7}</code></p>
 
┌──(kali㉿kali)-[~]
└─$

hay otra forma con python
┌──(kali㉿kali)-[~]
└─$ nano exp.py                
                                                                      
┌──(kali㉿kali)-[~]
└─$ python exp.py   
^CTraceback (most recent call last):
  File "/home/kali/exp.py", line 6, in <module>
    r = requests.get(url, cookies=cookies)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 61, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 529, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 645, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 440, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 704, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 450, in _make_request
    six.raise_from(e, None)
  File "<string>", line 3, in raise_from
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 445, in _make_request
    httplib_response = conn.getresponse()
  File "/usr/lib/python3.10/http/client.py", line 1374, in getresponse
    response.begin()
  File "/usr/lib/python3.10/http/client.py", line 318, in begin
    version, status, reason = self._read_status()
  File "/usr/lib/python3.10/http/client.py", line 279, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
  File "/usr/lib/python3.10/socket.py", line 705, in readinto
    return self._sock.recv_into(b)
KeyboardInterrupt

                                                                      
┌──(kali㉿kali)-[~]
└─$ cd /home/kali/Desktop/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF/pico-2021/
cd: string not in pwd: /home/kali/Desktop/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web
                                                                      
┌──(kali㉿kali)-[~]
└─$ nano exp.py



```
picoCTF{3v3ry1_l0v3s_c00k135_a1f5bdb7}

## Referencias
- []()