# B1ll_Gat35
## Objetivo
Can you reverse this [Windows Binary](https://jupiter.challenges.picoctf.org/static/0ef5d0d6d552cd5e0bd60c2adbddaa94/win-exec-1.exe)?

## Soluciòn

```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls
'01- vault-door-training.md'  '04- vault-door-4.md'  '07- asm1.md'  '10- asm4.md'            '13- B1ll_Gat35.md'    miProyec.lock    need-for-speed 
'02- vault-door-1.md'         '05- vault-door-5.md'  '08- asm2.md'  '11- reverse_cipher.md'   Help-pictures-notes   miProyec.lock~   test.S
'03- vault-door-3.md'         '06- vault-door-6.md'  '09- asm3.md'  '12- Need For Speed.md'   miProyec.gpr          miProyec.rep     win-exec-1.exe

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file win-exec-1.exe
win-exec-1.exe: PE32 executable (console) Intel 80386, for MS Windows

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ wine win-exec-1.exe     
Input a number between 1 and 5 digits: 1
Initializing...
Enter the correct key to get the access codes: 1234
Incorrect key. Try again.

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ghidra &                     
[1] 43129

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true
Picked up _JAVA_OPTIONS: -Dawt.useSystemAAFontSettings=on -Dswing.aatext=true

[1]  + done       ghidra
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```

![[Screenshot_2022-11-25_21_20_14.png]]

![[Screenshot_2022-11-25_21_21_01.png]]

![[Screenshot_2022-11-25_21_22_29.png]]

![[Screenshot_2022-11-25_21_24_02.png]]

![[Screenshot_2022-11-25_21_44_25.png]]

![[Screenshot_2022-11-25_21_44_41.png]]

![[Screenshot_2022-11-25_21_45_22.png]]

![[Screenshot_2022-11-25_21_49_20.png]]

![[Screenshot_2022-11-25_21_49_35.png]]

![[Screenshot_2022-11-25_21_52_19.png]]

![[Screenshot_2022-11-25_21_53_35.png]]

```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls                  
'01- vault-door-training.md'  '04- vault-door-4.md'  '07- asm1.md'  '10- asm4.md'            '13- B1ll_Gat35.md'    miProyec.rep     win-exec-1.exe
'02- vault-door-1.md'         '05- vault-door-5.md'  '08- asm2.md'  '11- reverse_cipher.md'   Help-pictures-notes   need-for-speed   win-exec-2.exe.bin
'03- vault-door-3.md'         '06- vault-door-6.md'  '09- asm3.md'  '12- Need For Speed.md'   miProyec.gpr          test.S

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ mv win-exec-2.exe.bin win-exec-2.exe

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls                  
'01- vault-door-training.md'  '04- vault-door-4.md'  '07- asm1.md'  '10- asm4.md'            '13- B1ll_Gat35.md'    miProyec.rep     win-exec-1.exe
'02- vault-door-1.md'         '05- vault-door-5.md'  '08- asm2.md'  '11- reverse_cipher.md'   Help-pictures-notes   need-for-speed   win-exec-2.exe
'03- vault-door-3.md'         '06- vault-door-6.md'  '09- asm3.md'  '12- Need For Speed.md'   miProyec.gpr          test.S

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ wine win-exec-2.exe
Input a number between 1 and 5 digits: 1
Initializing...
Enter the correct key to get the access codes: 1234
Correct input. Printing flag: PICOCTF{These are the access codes to the vault: 1063340}                                                                                                                                                                      
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```
flag: PICOCTF{These are the access codes to the vault: 1063340}

## Referencias
- []()
