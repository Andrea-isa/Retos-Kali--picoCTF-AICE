# vault-door-4
## Objetivo
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://jupiter.challenges.picoctf.org/static/c695ee23309d453a3ef369c34cc1bccb/VaultDoor4.java)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls
'01- vault-door-training.md'  '03- vault-door-3.md'   flagdoor1         VaultDoor3.class   VaultDoor4.java
'02- vault-door-1.md'         '04- vault-door-4.md'   VaultDoor1.java   VaultDoor3.java    VaultDoorTraining.java

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat VaultDoor4.java                                                 
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
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

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
            '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```

![[Screenshot_2022-11-18_17_13_12.png]]

```shell
Microsoft Windows [Versión 10.0.19043.2130]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>dir
 El volumen de la unidad C es Windows
 El número de serie del volumen es: 3D5D-BDE0

 Directorio de C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019

18/11/2022  03:59 p. m.    <DIR>          .
18/11/2022  03:59 p. m.    <DIR>          ..
18/11/2022  02:31 p. m.             2,279 01- vault-door-training.md
18/11/2022  03:57 p. m.             5,845 02- vault-door-1.md
18/11/2022  03:54 p. m.             5,682 03- vault-door-3.md
18/11/2022  04:06 p. m.               322 04- vault-door-4.md
18/11/2022  02:43 p. m.             1,438 flagdoor1
18/11/2022  02:32 p. m.             2,264 VaultDoor1.java
18/11/2022  03:00 p. m.             1,347 VaultDoor3.class
18/11/2022  02:54 p. m.             1,474 VaultDoor3.java
18/11/2022  03:58 p. m.             1,497 VaultDoor4.java
18/11/2022  02:29 p. m.               943 VaultDoorTraining.java
              10 archivos         23,091 bytes
               2 dirs  229,285,113,856 bytes libres

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>javac VaultDoor4.java

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>java VaultDoor4
Enter vault password: picoCTF{jU5t_4_bUnCh_0f_bYt3s_8fundefined}
Access denied!

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>java VaultDoor4
Enter vault password: picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}
Access granted.

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>
```

picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}

## Referencias
- []()