# basic-mod1
## Objetivo
We found this weird message being passed around on the servers, we think we have a working decryption scheme. Download the message [here](https://artifacts.picoctf.net/c/394/message.txt). Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore. Wrap your decrypted message in the picoCTF flag format (i.e. `picoCTF{decrypted_message}`)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ ls
'01- basic-mod1.md'   message.txt

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ cat message.txt             
202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ nano msg.py 
  
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ python msg.py
['202', '137', '390', '235', '114', '369', '198', '110', '350', '396', '390', '383', '225', '258', '38', '291', '75', '324', '401', '142', '288', '397']
picoCTF{R0UND_N_R0UND_B6B25531}
 
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ 
```

```python
datos=open('message.txt').read().split()

print(datos)

flag=''

for n in datos:
 c=int(n) % 37
 if c >= 0 and c <=  25:
  s=chr(c + 65)
 elif c >= 26 and c <= 35:
  s=chr(c + 22)
 else:
  s='_'
 flag+=s

print(f"picoCTF{{{flag}}}")

```

picoCTF{R0UND_N_R0UND_B6B25531}

## Referencias
- []()