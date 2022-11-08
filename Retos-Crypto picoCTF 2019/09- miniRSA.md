# miniRSA
## Objetivo
Let's decrypt this: [ciphertext](https://jupiter.challenges.picoctf.org/static/ee7e2388b45f521b285334abb5a63771/ciphertext)? Something seems a bit small.

## Soluciòn

Antes de dar la soluciòn,  debemos tener encuenta estos puntos para poder dar respuesta:
```text
c - texto cifrado
m - mensajo en texto plano (lo que se va encriptar)
p - primo 1
q - primo 2
n - modulo
tn - totient n (euler)
e - exponente (llave publica, suele ser 216 + 1=65537 )
d - llave privada
```
Y estas operaciones base son las que necesitaremos:
```text
n = p * q
tn = (p-1)*(q-1)
d = e mod inv tn / python -> inverse(e,tn)

Encriptar c = m^e mod n / python -> pow(m,e,n)

Desencriptar m = c^d mod n / python -> pow(c,d,n)
```

Para este reto usaremos solamente:
```text
c=m^e mod n
c=m^3
m=3 raìz c
```

Como en el reto anterior, usaremos dos terminales diferentes.

![[Screenshot_2022-11-07_20_06_27.png]]


```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ ls            
'01- The numbers.md'  '03- 13.md'      '05- la cifra de.md'  '07- waves over lambda.md'  '09- miniRSA.md'       caesar.py    Help-pictures-notes   the_numbers.png
'02- Easy 1.md'       '04- caesar.md'  '06- Tapping.md'      '08- rsa-pop-quiz.md'       '10- b00tl3gRSA2.md'   ciphertext   table.txt

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ file ciphertext
ciphertext: ASCII text, with very long lines (620)

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ cat ciphertext

N: 29331922499794985782735976045591164936683059380558950386560160105740343201513369939006307531165922708949619162698623675349030430859547825708994708321803705309459438099340427770580064400911431856656901982789948285309956111848686906152664473350940486507451771223435835260168971210087470894448460745593956840586530527915802541450092946574694809584880896601317519794442862977471129319781313161842056501715040555964011899589002863730868679527184420789010551475067862907739054966183120621407246398518098981106431219207697870293412176440482900183550467375190239898455201170831410460483829448603477361305838743852756938687673
e: 3

ciphertext (c): 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125 

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ sudo python -m pip install gmpy2 
[sudo] password for kali: 
Collecting gmpy2
  Downloading gmpy2-2.1.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.6/3.6 MB 2.1 MB/s eta 0:00:00
Installing collected packages: gmpy2
Successfully installed gmpy2-2.1.2
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ sudo python -m pip install pycryptodome
Requirement already satisfied: pycryptodome in /usr/local/lib/python3.10/dist-packages (3.15.0)
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv                                                                                                                 

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ 
```


En la terminal de python:
```python
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ python                  
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from gmpy2 import *
>>> from Crypto.Util.number import long_to_bytes
>>> gmpy2.get_context().precision=2048
>>> 
>>> e=3
>>> c=2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171277838056821437115883619169702963504606017565783537203207707757768473109845162808575425972525116337319108047893250549462147185741761825125
>>> root, exact=iroot(c,e)
>>> root                                                                                                                                                               
mpz(13016382529449106065894479374027604750406953699090365388202874238148389207291005)                                                                                  
>>> print(long_to_bytes(root))                                                                                                                                        
b'picoCTF{n33d_a_lArg3r_e_606ce004}'                                                                                                                                   
>>> 
```


picoCTF{n33d_a_lArg3r_e_606ce004}

## Referencias
- []()