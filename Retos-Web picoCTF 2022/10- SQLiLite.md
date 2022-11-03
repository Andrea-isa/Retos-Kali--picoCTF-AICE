# SQLiLite
## Objetivo
Can you login to this website?

## Soluciòn
Igual que con el reto anterior, lo primero que debemos hacer es iniciar la instancia con el botòn que dice *Launch Instance*.
Luego en la descripciòn de este reto nos darà un link: Try to login [here](http://saturn.picoctf.net:64863/).
Damos clik y os mandarà a esta pàgina:

![[Screenshot_2022-10-14_15_59_37.png]]

Intentaremos loguearnos con un usuario y contraseña random, y nos saldrà lo siguiente.

![[Screenshot_2022-10-14_16_06_42.png]]

Por lo que debemos hacer algo similar a retos pasados. Ingresamos: 
'or 1=1 -- -
en el usuario y en la contraseña, asì logramos acceder a una pàgina que nos dice que si accedimos, pero que podremos ve la flag inspeccionando el còdigo de la pàgina.

![[Screenshot_2022-10-14_16_07_34.png]]
![[Screenshot_2022-10-14_16_07_41.png]]

Inspeccionamos.

![[Screenshot_2022-10-14_16_08_09.png]]
![[Screenshot_2022-10-14_16_09_19.png]]

Y como vemos, la gla se encuentra en un campo oculto.
`Your flag is: picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}`

picoCTF{L00k5_l1k3_y0u_solv3d_it_ec8a64c7}

## Referencias
- []()