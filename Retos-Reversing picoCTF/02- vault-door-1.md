# vault-door-1
## Objetivo
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://jupiter.challenges.picoctf.org/static/ff2585f7afd21b81f69d2fbe37c081ae/VaultDoor1.java)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls
'01- vault-door-training.md'  Help-pictures-notes  VaultDoorTraining.java
'02- vault-door-1.md'    VaultDoor1.java       

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat VaultDoor1.java
import java.util.*;

class VaultDoor1 {
    public static void main(String args[]) {
        VaultDoor1 vaultDoor = new VaultDoor1();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    // I came up with a more secure way to check the password without putting
    // the password itself in the source code. I think this is going to be
    // UNHACKABLE!! I hope Dr. Evil agrees...
    //
    // -Minion #8728
    public boolean checkPassword(String password) {
        return password.length() == 32 &&
               password.charAt(0)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(4)  == 'r' &&
               password.charAt(2)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(3)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(1)  == '3' &&
               password.charAt(7)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(5)  == '4' &&
               password.charAt(9)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(8)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(6)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e';
    }
}
```
Vamos a copiar y pegar en un archivo todos los `password.charAt` desde `password.charAt(0)  == 'd' &&` al `password.charAt(31) == 'e';`, y les agregamos un `0` al inicio a cada `charAt` que tenga un solo dìgito.

```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ nano flag     

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag                                                            
               password.charAt(00)  == 'd' &&
               password.charAt(29) == '9' &&
               password.charAt(04)  == 'r' &&
               password.charAt(02)  == '5' &&
               password.charAt(23) == 'r' &&
               password.charAt(03)  == 'c' &&
               password.charAt(17) == '4' &&
               password.charAt(01)  == '3' &&
               password.charAt(07)  == 'b' &&
               password.charAt(10) == '_' &&
               password.charAt(05)  == '4' &&
               password.charAt(09)  == '3' &&
               password.charAt(11) == 't' &&
               password.charAt(15) == 'c' &&
               password.charAt(08)  == 'l' &&
               password.charAt(12) == 'H' &&
               password.charAt(20) == 'c' &&
               password.charAt(14) == '_' &&
               password.charAt(06)  == 'm' &&
               password.charAt(24) == '5' &&
               password.charAt(18) == 'r' &&
               password.charAt(13) == '3' &&
               password.charAt(19) == '4' &&
               password.charAt(21) == 'T' &&
               password.charAt(16) == 'H' &&
               password.charAt(27) == '5' &&
               password.charAt(30) == '2' &&
               password.charAt(25) == '_' &&
               password.charAt(22) == '3' &&
               password.charAt(28) == '0' &&
               password.charAt(26) == '7' &&
               password.charAt(31) == 'e'

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag|sort                  
               password.charAt(00)  == 'd' &&
               password.charAt(01)  == '3' &&
               password.charAt(02)  == '5' &&
               password.charAt(03)  == 'c' &&
               password.charAt(04)  == 'r' &&
               password.charAt(05)  == '4' &&
               password.charAt(06)  == 'm' &&
               password.charAt(07)  == 'b' &&
               password.charAt(08)  == 'l' &&
               password.charAt(09)  == '3' &&
               password.charAt(10) == '_' &&
               password.charAt(11) == 't' &&
               password.charAt(12) == 'H' &&
               password.charAt(13) == '3' &&
               password.charAt(14) == '_' &&
               password.charAt(15) == 'c' &&
               password.charAt(16) == 'H' &&
               password.charAt(17) == '4' &&
               password.charAt(18) == 'r' &&
               password.charAt(19) == '4' &&
               password.charAt(20) == 'c' &&
               password.charAt(21) == 'T' &&
               password.charAt(22) == '3' &&
               password.charAt(23) == 'r' &&
               password.charAt(24) == '5' &&
               password.charAt(25) == '_' &&
               password.charAt(26) == '7' &&
               password.charAt(27) == '5' &&
               password.charAt(28) == '0' &&
               password.charAt(29) == '9' &&
               password.charAt(30) == '2' &&
               password.charAt(31) == 'e'

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag|sort|awk '{print($3)}'                               
'd'
'3'
'5'
'c'
'r'
'4'
'm'
'b'
'l'
'3'
'_'
't'
'H'
'3'
'_'
'c'
'H'
'4'
'r'
'4'
'c'
'T'
'3'
'r'
'5'
'_'
'7'
'5'
'0'
'9'
'2'
'e'

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag|sort|awk '{print($3)}'|tr -d "'"                     
d
3
5
c
r
4
m
b
l
3
_
t
H
3
_
c
H
4
r
4
c
T
3
r
5
_
7
5
0
9
2
e

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag|sort|awk '{print($3)}'|tr -d "'"|tr -d '\n'          
d35cr4mbl3_tH3_cH4r4cT3r5_75092e                                                                                                                                                                      
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat flag|sort|awk '{print($3)}'|tr -d "'"|tr -d '\n'|tr -d ';' 
d35cr4mbl3_tH3_cH4r4cT3r5_75092e                                                                                                                                                                      
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_75092e}

## Referencias
- []()