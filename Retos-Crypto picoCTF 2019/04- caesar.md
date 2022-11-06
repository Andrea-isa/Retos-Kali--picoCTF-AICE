# caesar
## Objetivo
Decrypt this [message](https://jupiter.challenges.picoctf.org/static/49f31c8f17817dc2d367428c9e5ab0bc/ciphertext).

## Soluciòn
El cifrado ROT 13 es un cifrado caaesar rotado 13 veces. En este caso rotamos 30 veces.

![[Screenshot_2022-11-06_14_43_09.png]]

Ademàs, podemos usar la terminal y hacemos un còdigo en phyton.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ ls
'01- The numbers.md'  '02- Nombre 1.md'  '03- 13.md'  '04- caesar.md'   ciphertext   the_numbers.png

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ file ciphertext     
ciphertext: ASCII text, with no line terminators

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ cat ciphertext                       
picoCTF{ynkooejcpdanqxeykjrbdofgkq}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ nano caesar.py

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019]
└─$ python caesar.py
crossingtherubiconvfhsjkou
```
El còdigo es el siguiente:
```python
import string
import re

abc = string.ascii_letters

encriptado = open('ciphertext','r').read()
encriptado = re.findall('\{(.*?)\}',encriptado)[0]

rot = 30 //esta son las veces en que se rotò el texto, en mi caso 30.
salida = ''
for car in encriptado:
 salida += abc[ (abc.find(car) + rot) % 26 ]

print(salida)

```

picoCTF{crossingtherubiconvfhsjkou}

## Referencias
- []()