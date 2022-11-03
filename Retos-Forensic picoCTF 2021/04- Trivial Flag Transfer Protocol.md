# Trivial Flag Transfer Protocol
## Objetivo
Figure out how they moved the [flag](https://mercury.picoctf.net/static/fb24ddcfaf1e297be525ba7474964fa5/tftp.pcapng).

## Soluciòn


```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls
'01- Matryoshka doll.md'  '03- MacroHard WeakEdge.md'              '0n- Nombre 1 3.md'     docProps    _dolls.jpg.extracted     ppt     tftp.pcapng
'02- tunn3l_v1s10n.md'    '04- Trivial Flag Transfer Protocol.md'  '[Content_Types].xml'   dolls.jpg  'Forensics is fun.pptm'   _rels   tunn3l_v1s10n

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file tftp.pcapng
tftp.pcapng: pcapng capture file - version 1.0

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ wireshark tftp.pcapng                                                                                                            
 ** (wireshark:8489) 15:56:38.750899 [(none) WARNING] ./ui/qt/main_window.cpp:1814 -- bool MainWindow::testCaptureFileClose(QString, MainWindow::FileCloseContext)(): Refusing to close "tftp.pcapng" which is being read.
zsh: segmentation fault  wireshark tftp.pcapng

```
Se abre la herramienta, 

![[Screenshot_2022-10-31_15_56_29 1.png]]

vamos a 'File' luego a 'Export objects',

![[Screenshot_2022-10-31_15_54_31.png]]

y guardamos el la carpeta que queramos.

![[Screenshot_2022-10-31_15_56_10.png]]



```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls
'01- Matryoshka doll.md'     '04- Trivial Flag Transfer Protocol.md'   docProps              'Forensics is fun.pptm'   plan          _rels
'02- tunn3l_v1s10n.md'       '0n- Nombre 1 3.md'                       dolls.jpg              instructions.txt         ppt           tftp.pcapng
'03- MacroHard WeakEdge.md'  '[Content_Types].xml'                     _dolls.jpg.extracted   picture1.bmp             program.deb   tunn3l_v1s10n

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat instructions.txt
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat instructions.txt | base64 -d
!�@Ed@<B�▒�▒CRIS��YQ�TT�TTAD�51�4RDbase64: invalid input

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat instructions.txt | base32 -d
4�(%��b0NC��^P�99M
�g�b�Xl�F���base32: invalid input

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat instructions.txt | tr [A-Z] [N-ZA-M]
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls 
'01- Matryoshka doll.md'     '04- Trivial Flag Transfer Protocol.md'   docProps              'Forensics is fun.pptm'   plan          _rels
'02- tunn3l_v1s10n.md'       '0n- Nombre 1 3.md'                       dolls.jpg              instructions.txt         ppt           tftp.pcapng
'03- MacroHard WeakEdge.md'  '[Content_Types].xml'                     _dolls.jpg.extracted   picture1.bmp             program.deb   tunn3l_v1s10n

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file plan       
plan: ASCII text

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat plan                                
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat plan | tr [A-Z] [N-ZA-M]
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ file program.deb
program.deb: Debian binary package (format 2.0), with control.tar.gz, data compression xz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ dpkg-deb -I program.deb
 new Debian package, version 2.0.
 size 138310 bytes: control archive=1250 bytes.
     826 bytes,    18 lines      control              
    1184 bytes,    17 lines      md5sums              
 Package: steghide
 Source: steghide (0.5.1-9.1)
 Version: 0.5.1-9.1+b1
 Architecture: amd64
 Maintainer: Ola Lundqvist <opal@debian.org>
 Installed-Size: 426
 Depends: libc6 (>= 2.2.5), libgcc1 (>= 1:4.1.1), libjpeg62-turbo (>= 1:1.3.1), libmcrypt4, libmhash2, libstdc++6 (>= 4.9), zlib1g (>= 1:1.1.4)
 Section: misc
 Priority: optional
 Description: A steganography hiding tool
  Steghide is steganography program which hides bits of a data file
  in some of the least significant bits of another file in such a way
  that the existence of the data file is not visible and cannot be proven.
  .
  Steghide is designed to be portable and configurable and features hiding
  data in bmp, wav and au files, blowfish encryption, MD5 hashing of
  passphrases to blowfish keys, and pseudo-random distribution of hidden bits
  in the container data.

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ ls
'01- Matryoshka doll.md'     '04- Trivial Flag Transfer Protocol.md'   docProps              'Forensics is fun.pptm'   plan          _rels
'02- tunn3l_v1s10n.md'       '0n- Nombre 1 3.md'                       dolls.jpg              instructions.txt         ppt           tftp.pcapng
'03- MacroHard WeakEdge.md'  '[Content_Types].xml'                     _dolls.jpg.extracted   picture1.bmp             program.deb   tunn3l_v1s10n

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ open picture1.bmp 

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ steghide --extract -sf picture3.bmp -p DUEDILIGENCE
wrote extracted data to "flag.txt".

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ cat flag.txt                
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
picoCTF{}

## Referencias
- []()