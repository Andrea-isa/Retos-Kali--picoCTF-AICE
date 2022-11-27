# file-run1
## Objetivo
A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](https://artifacts.picoctf.net/c/310/run).

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ ls
'01- file-run1.md'  run
 
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ file run           
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0514683255a9ef58abe3c729e7418d07210a759e, for GNU/Linux 3.2.0, not stripped

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ ./run  
The flag is: picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b}   

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ 

```
picoCTF{U51N6_Y0Ur_F1r57_F113_47cf2b7b} 

## Referencias
- []()