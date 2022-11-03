# Secrets
## Objetivo
We have several pages hidden. Can you find the one with the flag? The website is running [here](http://saturn.picoctf.net:49917/).

## Soluciòn

```shell
┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://saturn.picoctf.net:49917/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                               
=====================================================================

000000718:   301        7 L      11 W       169 Ch      "secret"                                                                                              

Total time: 0
Processed Requests: 951
Filtered Requests: 950
Requests/sec.: 0


┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/secret/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://saturn.picoctf.net:49917/secret/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                               
=====================================================================

000000076:   301        7 L      11 W       169 Ch      "assets"                                                                                              
000000395:   301        7 L      11 W       169 Ch      "hidden"                                                                                              

Total time: 11.57636
Processed Requests: 951
Filtered Requests: 949
Requests/sec.: 82.15013


┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/secret/hidden/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://saturn.picoctf.net:49917/secret/hidden/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                               
=====================================================================


Total time: 0
Processed Requests: 951
Filtered Requests: 951
Requests/sec.: 0


┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/secret/hidden/index/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://saturn.picoctf.net:49917/secret/hidden/index/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                               
=====================================================================


Total time: 0
Processed Requests: 951
Filtered Requests: 951
Requests/sec.: 0

┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/secret/hidden/index.html/FUZZ"
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://saturn.picoctf.net:49917/secret/hidden/index.html/FUZZ
Total requests: 951

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                               
=====================================================================


Total time: 0
Processed Requests: 951
Filtered Requests: 951
Requests/sec.: 0
   
┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 "http://saturn.picoctf.net:49917/secret/hidden/index.html"     
 /usr/lib/python3/dist-packages/wfuzz/__init__.py:34: UserWarning:Pycurl is not compiled against Openssl. Wfuzz might not work correctly when fuzzing SSL sites. Check Wfuzz's documentation for more information.
 /usr/lib/python3/dist-packages/wfuzz/wfuzz.py:78: UserWarning:Fatal exception: FUZZ words and number of payloads do not match!

┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ curl "http://saturn.picoctf.net:49917/secret/hidden/index.html"
<!DOCTYPE html>
<html>
  <head>
    <title>LOGIN</title>
    <!-- css -->
    <link href="superhidden/login.css" rel="stylesheet" />
  </head>
  <body>
    <form>
      <div class="container">
        <form method="" action="/secret/assets/popup.js">
          <div class="row">
            <h2 style="text-align: center">
              Login with Social Media or Manually
            </h2>
            <div class="vl">
              <span class="vl-innertext">or</span>
            </div>

            <div class="col">
              <a href="#" class="fb btn">
                <i class="fa fa-facebook fa-fw"></i> Login with Facebook
              </a>
              <a href="#" class="twitter btn">
                <i class="fa fa-twitter fa-fw"></i> Login with Twitter
              </a>
              <a href="#" class="google btn">
                <i class="fa fa-google fa-fw"></i> Login with Google+
              </a>
            </div>

            <div class="col">
              <div class="hide-md-lg">
                <p>Or sign in manually:</p>
              </div>

              <input
                type="text"
                name="username"
                placeholder="Username"
                required
              />
              <input
                type="password"
                name="password"
                placeholder="Password"
                required
              />
              <input type="hidden" name="db" value="superhidden/xdfgwd.html" />

              <input
                type="submit"
                value="Login"
                onclick="alert('Thank you for the attempt but oops! try harder. better luck next time')"
              />
            </div>
          </div>
        </form>
      </div>

      <div class="bottom-container">
        <div class="row">
          <div class="col">
            <a href="#" style="color: white" class="btn">Sign up</a>
          </div>
          <div class="col">
            <a href="#" style="color: white" class="btn">Forgot password?</a>
          </div>
        </div>
      </div>
    </form>
  </body>
</html>

┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ curl "http://saturn.picoctf.net:49917/secret/hidden/superhidden/index.html"
<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <link rel="stylesheet" href="mycss.css" />
  </head>

  <body>
    <h1>Finally. You found me. But can you see me</h1>
    <h3 class="flag">picoCTF{succ3ss_@h3n1c@10n_790d2615}</h3>
  </body>
</html>

┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ 
```
picoCTF{succ3ss_@h3n1c@10n_790d2615}

## Referencias
- []()