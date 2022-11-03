# Glory of the Garden
## Objetivo
This [garden](https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg) contains more than it seems.

## Soluciòn
Antes de comenzar, debemos descargar la imagen que se nos da en la descripciòn del reto, se llama `garden.jpg`.
Tenemos 3 soluciones para este reto.

Gracias a la pista que nos da el reto podemos suponer que la soluciòn es usar el hex editor,lo usamos desde la consola, por lo tanto esta es la primera soluciòn.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam-- editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ hexeditor garden.jpg
```
Nos abrirà una vetana con muchos numeros.

![[Screenshot_2022-10-14_16_59_09.png]]

Ahora precionamos `ctrl+w` desde el teclado, y abrirà una ventana de bùsqueda, damos enter en donde dice `search for text string`.

![[Screenshot_2022-10-14_17_00_13.png]]

Nos aparecerà una ventana con un campo donde buscaremos `picoCTF` y damos enter.

![[Screenshot_2022-10-14_17_01_49.png]]
![[Screenshot_2022-10-14_17_03_13.png]]
![[Screenshot_2022-10-14_17_03_40.png]]

Y veremos la flag del lado derecho. Para salir de esa vetana, desde teclado damos `ctrl+c`.

Las otras dos soluciones, que son las màs ràpidas, son las siguientes.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ strings garden.jpg | grep pico
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ strings -n 15 garden.jpg | grep picoCT
Here is a flag "picoCTF{more_than_m33ts_the_3y3eBdBd2cc}"
```
picoCTF{more_than_m33ts_the_3y3eBdBd2cc}

## Referencias
- []()