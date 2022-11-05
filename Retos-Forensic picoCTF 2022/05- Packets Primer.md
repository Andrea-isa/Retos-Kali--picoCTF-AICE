# Packets Primer
## Objetivo
Download the packet capture file and use packet analysis software to find the flag.

-   [Download packet capture](https://artifacts.picoctf.net/c/201/network-dump.flag.pcap)

## Soluciòn
Abrimos el archivo con la herramienta Wireshark.

![[Screenshot_2022-11-04_21_02_45.png]]

Copiamos ese texto y lo llevamos a la consola para quitar los espacios.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ echo 'p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }' | tr -d  ' '
picoCTF{p4ck37_5h4rk_01b0a0d6}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ 
```
picoCTF{p4ck37_5h4rk_01b0a0d6}

## Referencias
- []()