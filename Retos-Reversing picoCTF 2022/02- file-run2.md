# file-run2
## Objetivo
Another program, but this time, it seems to want some input. What happens if you try to run it on the command line with input "Hello!"? Download the program [here](https://artifacts.picoctf.net/c/353/run).

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ ls
'01- file-run1.md'  '02- file-run2.md'  run

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ file run
run: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=e923d195967f2f793c6de52cee78b8fb7f3c0a2a, for GNU/Linux 3.2.0, not stripped
  
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ ./run Hello!
The flag is: picoCTF{F1r57_4rgum3n7_f65ed63e}   

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2022]
└─$ 
```
picoCTF{F1r57_4rgum3n7_f65ed63e} 

## Referencias
- []()