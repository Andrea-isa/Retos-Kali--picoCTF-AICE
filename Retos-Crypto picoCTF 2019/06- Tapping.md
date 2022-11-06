# Tapping
## Objetivo
Theres tapping coming in from the wires. What's it saying `nc jupiter.challenges.picoctf.org 9422`.

## Soluciòn

Nos conectamos al servidor y nos dan un mensaje cifrado, vemos que es còdigo morse.
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019/Help-pictures-notes]
└─$ nc jupiter.challenges.picoctf.org 9422  
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- -.... ---.. ...-- ---.. ..--- ....- -.... .---- ----- } 

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019/Help-pictures-notes]
└─$ 
```

Por lo que usamos la herramienta Cyberchef y sacamos la bandera.

![[Screenshot_2022-11-06_15_27_02.png]]

El còdigo morse no existen las llaves '{}', por lo que la flag se nos darà sin ellas, es cuatiòn de acomodarlas en su respectivo lugar.

PICOCTF{M0RS3C0D31SFUN2683824610}

## Referencias
- []()