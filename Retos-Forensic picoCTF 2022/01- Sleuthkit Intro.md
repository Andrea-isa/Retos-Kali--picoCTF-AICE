# Sleuthkit Intro
## Objetivo
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download disk image](https://artifacts.picoctf.net/c/114/disk.img.gz)
-   Access checker program: `nc saturn.picoctf.net 52279`

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls
'01- Sleuthkit Intro.md'  '02- Operation Oni.md'   disk.img.gz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ file disk.img.gz  
disk.img.gz: gzip compressed data, was "disk.img", last modified: Tue Sep 21 19:34:53 2021, from Unix, original size modulo 2^32 104857600

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ gzip -d disk.img.gz         

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls .la                 
ls: cannot access '.la': No such file or directory

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -la
total 102429
drwxrwx--- 1 root vboxsf      4096 Oct 31 22:41  .
drwxrwx--- 1 root vboxsf     24576 Oct 31 22:29  ..
-rwxrwx--- 1 root vboxsf       496 Oct 31 22:31 '01- Sleuthkit Intro.md'
-rwxrwx--- 1 root vboxsf       348 Oct 31 22:37 '02- Operation Oni.md'
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31  disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls    
'01- Sleuthkit Intro.md'  '02- Operation Oni.md'   disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -lab
total 102429
drwxrwx--- 1 root vboxsf      4096 Oct 31 22:41 .
drwxrwx--- 1 root vboxsf     24576 Oct 31 22:29 ..
-rwxrwx--- 1 root vboxsf       496 Oct 31 22:31 01-\ Sleuthkit\ Intro.md
-rwxrwx--- 1 root vboxsf       348 Oct 31 22:37 02-\ Operation\ Oni.md
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31 disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ mmls -v
Missing image name
mmls [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-BrvV] [-aAmM] [-t vstype] image [images]
        -t vstype: The type of volume system (use '-t list' for list of supported types)
        -i imgtype: The format of the image file (use '-i list' for list supported types)
        -b dev_sector_size: The size (in bytes) of the device sectors
        -o imgoffset: Offset to the start of the volume that contains the partition system (in sectors)
        -B: print the rounded length in bytes
        -r: recurse and look for other partition tables in partitions (DOS Only)
        -v: verbose output
        -V: print the version
Unless any of these are specified, all volume types are shown
        -a: Show allocated volumes
        -A: Show unallocated volumes
        -m: Show metadata volumes
        -M: Hide metadata volumes

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ mmls -V
The Sleuth Kit ver 4.11.1

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752           
202752
Great work!
picoCTF{mm15_f7w!}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$
```
picoCTF{mm15_f7w!}

## Referencias
- []()