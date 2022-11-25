# vault-door-6
## Objetivo
This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://jupiter.challenges.picoctf.org/static/937a166e2c8c5bf34928a2dab22e8ade/VaultDoor6.java)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file VaultDoor6.java
VaultDoor6.java: C++ source, ASCII text

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat VaultDoor6.java
import java.util.*;

class VaultDoor6 {
    public static void main(String args[]) {
        VaultDoor6 vaultDoor = new VaultDoor6();
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

    // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
    // and I learned this really cool encryption system. This will be the
    // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
    // Well, I didn't exactly read the *whole* book, but I'm sure there's
    // nothing important in the last 750 pages.
    //
    // -Minion #3091
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
            0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
            0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
            0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d,
        };
        for (int i=0; i<32; i++) {
            if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                return false;
            }
        }
        return true;
    }
}

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ python
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> myBytes=[0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
...             0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
...             0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
...             0xa , 0x6c, 0x61, 0x6d, 0x37, 0x6d, 0x6d, 0x6d]
>>> myBytes
[59, 101, 33, 10, 56, 0, 54, 29, 10, 61, 97, 39, 17, 102, 39, 10, 33, 29, 97, 59, 10, 45, 101, 39, 10, 108, 97, 109, 55, 109, 109, 109]
>>> flag=[i ^ 0x55 for i in myBytes]
>>> flag
[110, 48, 116, 95, 109, 85, 99, 72, 95, 104, 52, 114, 68, 51, 114, 95, 116, 72, 52, 110, 95, 120, 48, 114, 95, 57, 52, 56, 98, 56, 56, 56]
>>> flag=[chr(i) for i in flag]
>>> flag
['n', '0', 't', '_', 'm', 'U', 'c', 'H', '_', 'h', '4', 'r', 'D', '3', 'r', '_', 't', 'H', '4', 'n', '_', 'x', '0', 'r', '_', '9', '4', '8', 'b', '8', '8', '8']
>>> ''.join(flag)
'n0t_mUcH_h4rD3r_tH4n_x0r_948b888'
>>> exit()

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_948b888}

## Referencias
- []()