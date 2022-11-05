#  Lookey here
## Objetivo
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. Download the data [here](https://artifacts.picoctf.net/c/296/anthem.flag.txt).

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls
'01- Sleuthkit Intro.md'  '02- Operation Oni.md'  '03- Enhance!.md'  '04- Lookey here.md'   anthem.flag.txt   disk2.img   disk.img   drawing.flag.svg   key_file

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ file anthem.flag.txt 
anthem.flag.txt: Unicode text, UTF-8 text

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ wc -w anthem.flag.txt   
19139 anthem.flag.txt

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ cat anthem.flag.txt | grep "picoCTF"                                  
      we think that the men of picoCTF{gr3p_15_@w3s0m3_2116b979}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$
```
picoCTF{gr3p_15_@w3s0m3_2116b979}

## Referencias
- []()