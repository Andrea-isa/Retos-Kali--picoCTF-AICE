# Wireshark twoo twooo two twoo...
## Objetivo
Can you find the flag? [shark2.pcapng](https://mercury.picoctf.net/static/7b8e53329b34946177a9b5f2860a0292/shark2.pcapng).

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls
'01- Matryoshka doll.md'                 '05- Wireshark twoo twooo two twoo....md'   _dolls.jpg.extracted     instructions.txt   program.deb     tunn3l_v1s10n
'02- tunn3l_v1s10n.md'                   '[Content_Types].xml'                       flag.txt                 picture1.bmp       _rels
'03- MacroHard WeakEdge.md'               docProps                                  'Forensics is fun.pptm'   plan               shark2.pcapng
'04- Trivial Flag Transfer Protocol.md'   dolls.jpg                                  Help-pictures-notes      ppt                tftp.pcapng

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file shark2.pcapng
shark2.pcapng: pcapng capture file - version 1.0

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ wireshark  shark2.pcapng
```


![[Screenshot_2022-10-31_15_56_29 1.png]]

![[Screenshot_2022-10-31_17_02_11.png]]

vamos a 'File', luego a 'Export Packet Dissections' y luego a 'As CSV', se abre una ventana y gurdamos el archivo.
![[Screenshot_2022-10-31_17_18_50.png]]

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls
'01- Matryoshka doll.md'                 '05- Wireshark twoo twooo two twoo....md'   _dolls.jpg.extracted     Help-pictures-notes   ppt             tftp.pcapng
'02- tunn3l_v1s10n.md'                   '[Content_Types].xml'                       flag-shark2.csv          instructions.txt      program.deb     tunn3l_v1s10n
'03- MacroHard WeakEdge.md'               docProps                                   flag.txt                 picture1.bmp          _rels
'04- Trivial Flag Transfer Protocol.md'   dolls.jpg                                 'Forensics is fun.pptm'   plan                  shark2.pcapng

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv
"No.","Time","Source","Destination","Protocol","Length","Info"
"1637","9.440363","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local"
"2046","11.972605","192.168.38.104","18.217.1.57","DNS","109","Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local"
"2448","14.605726","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local"
"3153","16.506492","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local"
"3442","18.340155","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local"
"3982","20.369626","192.168.38.104","18.217.1.57","DNS","105","Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local"
"4374","22.583745","192.168.38.104","18.217.1.57","DNS","105","Standard query 0x7418 A fQ==.reddshrimpandherring.com.windomain.local"

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ nano flag-shark2.csv

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv 
"1637","9.440363","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x1dd2 A cGljb0NU.reddshrimpandherring.com.windomain.local"
"2046","11.972605","192.168.38.104","18.217.1.57","DNS","109","Standard query 0xabb9 A RntkbnNf.reddshrimpandherring.com.windomain.local"
"2448","14.605726","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x9e21 A M3hmMWxf.reddshrimpandherring.com.windomain.local"
"3153","16.506492","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2ee1 A ZnR3X2Rl.reddshrimpandherring.com.windomain.local"
"3442","18.340155","192.168.38.104","18.217.1.57","DNS","109","Standard query 0x2a4b A YWRiZWVm.reddshrimpandherring.com.windomain.local"
"3982","20.369626","192.168.38.104","18.217.1.57","DNS","105","Standard query 0x4068 A fQ==.reddshrimpandherring.com.windomain.local"

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv | cut -d ' ' -f 5 
cGljb0NU.reddshrimpandherring.com.windomain.local"
RntkbnNf.reddshrimpandherring.com.windomain.local"
M3hmMWxf.reddshrimpandherring.com.windomain.local"
ZnR3X2Rl.reddshrimpandherring.com.windomain.local"
YWRiZWVm.reddshrimpandherring.com.windomain.local"
fQ==.reddshrimpandherring.com.windomain.local"

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv | cut -d ' ' -f 5 | cut -d '.' -f1
cGljb0NU
RntkbnNf
M3hmMWxf
ZnR3X2Rl
YWRiZWVm
fQ==

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv | cut -d ' ' -f 5 | cut -d '.' -f1 | tr -d '\n'
cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==                                                                                                                                                                       

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag-shark2.csv | cut -d ' ' -f 5 | cut -d '.' -f1 | tr -d '\n' | base64 -d
picoCTF{dns_3xf1l_ftw_deadbeef}                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$
```
picoCTF{dns_3xf1l_ftw_deadbeef}

## Referencias
- []()