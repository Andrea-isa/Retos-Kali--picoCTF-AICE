# Power Cookie
## Objetivo
Can you get the flag? Go to this [website](http://saturn.picoctf.net:61304/) and see what you can discover.

## Soluciòn
La pista nos menciona como es posible cambiar las cookies, al entrar a la página que se nos da podemos ver en las cookies que no somos administradores, así que cambiamos ese 0 por un 1 y recargamos para poder observar la bandera.

Al acceder a la pàgina se os muestra esto:

![[Screenshot_2022-10-14_13_13_59.png]]

Y si hacemos click en el botòn nos muestra esto:

![[Screenshot_2022-10-14_13_22_01.png]]

Entonces... ¿donde podemos encontrar la flag? La pista nos pregunta si podremos modificar la cookie, gracias a una de las extenciones que usamos en varios retos anteriores llamada *Cookie Editor*, al ver la cookie debemos modificar el 0 que viene ahpi por un 1, regarcamos la pàgina y nos da la flag.

![[Screenshot_2022-10-14_13_30_31.png]]

picoCTF{gr4d3_A_c00k13_0d351e23}

## Referencias
- []()