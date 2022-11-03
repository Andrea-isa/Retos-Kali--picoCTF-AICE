# extensions
## Objetivo
This is a really weird text file [TXT](https://jupiter.challenges.picoctf.org/static/e7e5d188621ee705ceeb0452525412ef/flag.txt)? Can you find the flag?

## Soluciòn
Descargamos el archivo, se llama flag.txt, haciendo un vaciado hexadecimal podemos ver que tipo de archivo es, vemos que en realidad es una imagen y si le cambiamos la extension deberiamos poder abrir el archivo como imagen. Al abrir la imagen podemos ver la bandera
```bash
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ file flag.txt
flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
                                                                         
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ xxd -gl flag.txt | head 
00000000: 89504e470d0a1a0a0000000d49484452  .PNG........IHDR
00000010: 000006a100000260080200000085ad5e  .......`.......^
00000020: 9a000000017352474200aece1ce90000  .....sRGB.......
00000030: 000467414d410000b18f0bfc61050000  ..gAMA......a...
00000040: 00097048597300001625000016250149  ..pHYs...%...%.I
00000050: 5224f00000269549444154785eeddd6b  R$...&.IDATx^..k
00000060: 421b39b705d03b2e0694f1309a4c2683  B.9...;....0.L&.
00000070: f9ae5f804e3d25bb4cb3f15abfbaa14a  .._.N=%.L..Z...J
00000080: 757424137927c0fffd0f000000004826  ut$.y'........H&
00000090: e303000000806c323e00000000c826e3  ......l2>.....&.
                                                                         
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ mv flag.txt flag.png
                                                                         
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ open flag.png
                                                                         
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$
```
![[Screenshot_2022-10-14_19_15_12.png]]

picoCTF{now_you_know_about_extensions}

## Referencias
- []()