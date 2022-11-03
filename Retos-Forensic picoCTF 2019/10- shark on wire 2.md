# shark on wire 2
## Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Soluciòn
Usamos wireshark para analizar el documento que descaramos, en mi caso lo tuve que renombrar, originalmente se llamaba capture.pcap, y como ya tenìa un documento que se llama de la misma forma que se usò en un reto similar a este, lo renombrè a capture2.pcap.

Parapoder analizar, teneos que abrirlo desde el programa Wireshark, el cual ya habìamos usado en un reto anterior.

![[Screenshot_2022-10-16_21_03_16.png]]

![[Screenshot_2022-10-16_21_04_45.png]]

![[Screenshot_2022-10-16_21_05_53.png]]

En la parte  de `User Datagram Protocol` damos click derecho, luego a `Follow` y a `UDP Stream`,  se abrirà una ventana e iremos modifiando los numeros de la parte de Stream, pero es un poco tardado.

![[Screenshot_2022-10-16_21_11_38.png]]

Asì que usaremos un programa en python para poder sacar la flag màs ràpidamente.

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ nano shark2.py  
```
	En el archivo, desde nano, ponemos este còdigo, lo guardamos y ejecutamos.
```python
from scapy.all import *

packets = rdpcap('capture2.pcap')
flag=''
for p in packets:
 if UDP in p and p [UDP].dport==22:
  if p[UDP].sport > 5000: 
   flag += chr (p[UDP].sport - 5000)
print(flag)
```

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ python shark2.py
Matplotlib is building the font cache; this may take a moment.
picoCTF{p1LLf3r3d_data_v1a_st3g0}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ 
```
picoCTF{p1LLf3r3d_data_v1a_st3g0}

## Referencias
- []()