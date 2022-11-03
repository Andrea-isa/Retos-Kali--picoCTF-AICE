# Forbidden Paths
## Objetivo
Can you get the flag? Here's the [website](http://saturn.picoctf.net:55827/). We know that the website files live in `/usr/share/nginx/html/` and the flag is at `/flag.txt` but the website is filtering absolute file paths. Can you get past the filter to read the flag?

## Soluciòn
Al acceder a la pàgina nos muestra la siguiente

![[Screenshot_2022-10-14_13_00_09.png]]

Al buscar el documento *flag.txt* vemos que no existe.

![[Screenshot_2022-10-14_13_01_39.png]]

![[Screenshot_2022-10-14_13_01_50 1.png]]

Si intentamos buscar *..* nos manda a una pàgina que no contiene nada.

![[Screenshot_2022-10-14_13_06_10.png]]

Por lo que si intentamos con la siguiente estructura: **../../../../flag.txt** ; nos manda a una pàgina que contiene la flag.

![[Screenshot_2022-10-14_13_07_57.png]]

![[Screenshot_2022-10-14_13_08_06.png]]

picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}

## Referencias
- []()