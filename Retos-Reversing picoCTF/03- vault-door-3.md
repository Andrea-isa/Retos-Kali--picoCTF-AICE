# vault-door-3
## Objetivo
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://jupiter.challenges.picoctf.org/static/943ea40e3f54fca6d2145fa7aadc5e09/VaultDoor3.java)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ls
'01- vault-door-training.md'  '03- vault-door-3.md'   flagdoor1         VaultDoor3.java
'02- vault-door-1.md'         '04- vault-door-4.md'   VaultDoor1.java   VaultDoorTraining.java

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat VaultDoor3.java                                                 
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
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

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 

```

Usamosesta parte del còdigo para poder conseguir una contraseña, la cual nos servirà para confirmar que la flag es correcta.

```JavaScript
for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
```

El siguiente còdigo lo ejecutaremos en la consola del inspeccionador de còdigo de las pàginas web en uestro navegador, o bien, un ejecutador de còdigo online.

```JavaScript
var password="jU5t_a_sna_3lpm18g947_u_4_m9r54f";
var buffer=Array(32);

for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
    
console.log(buffer.join(""))
```


![[Screenshot_2022-11-18_16_45_03.png]]

![[Screenshot_2022-11-18_16_45_40.png]]


```shell
Microsoft Windows [Versión 10.0.19043.2130]
(c) Microsoft Corporation. Todos los derechos reservados.

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>dir
 El volumen de la unidad C es Windows
 El número de serie del volumen es: 3D5D-BDE0

 Directorio de C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019

18/11/2022  02:56 p. m.    <DIR>          .
18/11/2022  02:56 p. m.    <DIR>          ..
18/11/2022  02:31 p. m.             2,279 01- vault-door-training.md
18/11/2022  02:53 p. m.             3,495 02- vault-door-1.md
18/11/2022  02:27 p. m.               283 03- vault-door-3.md
18/11/2022  02:28 p. m.               289 04- vault-door-4.md
18/11/2022  02:43 p. m.             1,438 flagdoor1
18/11/2022  02:32 p. m.             2,264 VaultDoor1.java
18/11/2022  02:54 p. m.             1,474 VaultDoor3.java
18/11/2022  02:29 p. m.               943 VaultDoorTraining.java
               8 archivos         12,465 bytes
               2 dirs  229,309,997,056 bytes libres

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>javac VaultDoor3.java

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>java VaultDoor3
Enter vault password: jU5t_a_s1mpl3_an4gr4m_4_u_1fb380
Access denied!

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>java VaultDoor3
Enter vault password: jU5t_a_s1mpl3_an
Access denied!

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>java VaultDoor3
Enter vault password: picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}
Access granted.

C:\Users\Angie\Documents\Kali Linux-No borrar\Carpeta Compartida-Kali\RetosKali-exam--editar\CarpetaKali-exam1\Retos-Reversing\2019>
```

picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}

## Referencias
- []()