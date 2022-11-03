# tunn3l_v1s10n
## Objetivo
We found this [file](https://mercury.picoctf.net/static/7b2d7c26630e977197022d0af09e3aeb/tunn3l_v1s10n). Recover the flag.

## Soluciòn


```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ exiftool tunn3l_v1s10n                                                                
ExifTool Version Number         : 12.41
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.8 MiB
File Modification Date/Time     : 2021:03:15 14:24:47-04:00
File Access Date/Time           : 2022:06:07 22:29:28-04:00
File Inode Change Date/Time     : 2022:06:07 22:29:18-04:00
File Permissions                : -rwxrwx---
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Unknown (53434)
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Red Mask                        : 0x27171a23
Green Mask                      : 0x20291b1e
Blue Mask                       : 0x1e212a1d
Alpha Mask                      : 0x311a1d26
Color Space                     : Unknown (,5%()
Rendering Intent                : Unknown (826103054)
Image Size                      : 1134x306
Megapixels                      : 0.347

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file tunn3l_v1s10n 
tunn3l_v1s10n: data

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ xxd -g1 tunn3l_v1s10n | head
00000000: 42 4d 8e 26 2c 00 00 00 00 00 ba d0 00 00 ba d0  BM.&,...........

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ xxd -g1 tunn3l_v1s10n | head
00000000: 42 4d 8e 26 2c 00 00 00 00 00 28 00 00 00 28 00  BM.&,.....(...(.

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file tunn3l_v1s10n          
tunn3l_v1s10n: PC bitmap, Windows 3.x format, 1134 x 306 x 24, image size 2893400, resolution 5669 x 5669 px/m, cbSize 2893454, bits offset 40

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ xxd -g1 tunn3l_v1s10n | head
00000000: 42 4d 8e 26 2c 00 00 00 00 00 28 00 00 00 28 00  BM.&,.....(...(.
00000010: 00 00 6e 04 00 00 32 01 00 00 01 00 18 00 00 00  ..n...2.........

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ xxd -g1 tunn3l_v1s10n | head
00000000: 42 4d 8e 26 2c 00 00 00 00 00 28 00 00 00 28 00  BM.&,.....(...(.
00000010: 00 00 6e 04 00 00 40 03 00 00 01 00 18 00 00 00  ..n...@.........

```

Cambiamos donde estaba **32 01** por **40 03** y asi aumentamos el tamaño, abrimos la imagen y nos aparece la bandera derntro de la imagen.
picoCTF{qu1t3_a_v13w_2020}

## Referencias
- []()