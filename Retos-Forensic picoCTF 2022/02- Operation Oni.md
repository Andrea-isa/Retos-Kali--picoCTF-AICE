# Operation Oni
## Objetivo
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

-   [Download disk image](https://artifacts.picoctf.net/c/372/disk.img.gz)
-   Remote machine: `ssh -i key_file -p 64077 ctf-player@saturn.picoctf.net`

## Soluciòn

Primero tenemos que inicias una instancia con el botòn 'Launcher Instance'.

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ gzip -d disk2.img.gz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls     
'01- Sleuthkit Intro.md'  '02- Operation Oni.md'   disk2.img   disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -lb 
total 337929
-rwxrwx--- 1 root vboxsf      4590 Oct 31 22:48 01-\ Sleuthkit\ Intro.md
-rwxrwx--- 1 root vboxsf       503 Oct 31 22:49 02-\ Operation\ Oni.md
-rwxrwx--- 1 root vboxsf 241172480 Oct 31 22:50 disk2.img
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31 disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -lab
total 337957
drwxrwx--- 1 root vboxsf      4096 Oct 31 22:53 .
drwxrwx--- 1 root vboxsf     24576 Oct 31 22:29 ..
-rwxrwx--- 1 root vboxsf      4590 Oct 31 22:48 01-\ Sleuthkit\ Intro.md
-rwxrwx--- 1 root vboxsf       503 Oct 31 22:49 02-\ Operation\ Oni.md
-rwxrwx--- 1 root vboxsf 241172480 Oct 31 22:50 disk2.img
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31 disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -la 
total 337957
drwxrwx--- 1 root vboxsf      4096 Oct 31 22:53  .
drwxrwx--- 1 root vboxsf     24576 Oct 31 22:29  ..
-rwxrwx--- 1 root vboxsf      4590 Oct 31 22:48 '01- Sleuthkit Intro.md'
-rwxrwx--- 1 root vboxsf       503 Oct 31 22:49 '02- Operation Oni.md'
-rwxrwx--- 1 root vboxsf 241172480 Oct 31 22:50  disk2.img
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31  disk.img

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ mmls -V      
The Sleuth Kit ver 4.11.1

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ mmls disk2.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ man fls                                   

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ fls -o 206848 disk2.img                   
d/d 458:        home
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ fls -o 206848 disk2.img 470
r/r 2344:       .ash_history
d/d 3916:       .ssh

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ fls -o 206848 disk2.img 3916
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ man icat                    

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ icat -o 206848 disk2.img 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ icat -o 206848 disk2.img 2345 > key_file

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls    
'01- Sleuthkit Intro.md'  '02- Operation Oni.md'   disk2.img   disk.img   key_file

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ cat key_file                                                                   
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ chmod 400 key_file               

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ls -la
total 337957
drwxrwx--- 1 root vboxsf      4096 Oct 31 22:59  .
drwxrwx--- 1 root vboxsf     24576 Oct 31 22:29  ..
-rwxrwx--- 1 root vboxsf      4590 Oct 31 22:48 '01- Sleuthkit Intro.md'
-rwxrwx--- 1 root vboxsf       503 Oct 31 22:49 '02- Operation Oni.md'
-rwxrwx--- 1 root vboxsf 241172480 Oct 31 22:50  disk2.img
-rwxrwx--- 1 root vboxsf 104857600 Oct 31 22:31  disk.img
-rwxrwx--- 1 root vboxsf       411 Oct 31 22:59  key_file

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$ ssh -i key_file -p 64077 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:64077 ([18.217.86.78]:64077)' can't be established.
ED25519 key fingerprint is SHA256:5gIm/EJ9bYnoH4qed83W5HXLfN1DO55849f6Lze0lx8.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '[saturn.picoctf.net]:64077' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1025-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_339601ed}ctf-player@challenge:~$ Connection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2022]
└─$
```
picoCTF{}

## Referencias
- []()