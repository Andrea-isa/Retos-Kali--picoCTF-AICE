# logon
## Objetivo
The factory is hiding things from all of its users. Can you login as Joe and find what they've been looking at? `https://jupiter.challenges.picoctf.org/problem/15796/` ([link](https://jupiter.challenges.picoctf.org/problem/15796/)) or http://jupiter.challenges.picoctf.org:15796

## Soluciòn
El sitio web puede entrar con cualquier usuario siempre y cuando no se trate de "Joe", pero aún así no es un administrador y por lo tanto no nos muestra la bandera, es posible cambiar esto con una extensión para el manejo de cookies.

Al darle click al la lilga que nos dan, se nos abre un pagina de log in, la cual vamos a inspeccionar antes de realizar cualquier cosa, nos vamos al apatado de Network, nos loqueamos con cualquiere nombre de usuario y cualquier contraseña, nos mostrarà una pagina que dice que hemos entrado exitosamente, pero no tenemos una flag.  
![[Screenshot_2022-10-07_13_30_38.png]]
Entonces damos click sobre el Dominio que tiene el documento flag, con el estatus 200, se nos abre una segunda ventana al lado de la tabla de Network, la cual tiene los Response y Request Headers, asì como el de las Cookies. Si nos vamos al apartado de Cookies, vemos que el usuario con el que igresamos no tiene permisos como administrador, por lo que tenemos que cambiar el "false" a "true", para eso tenemos que instalar una extencion en nuestro navegador que nos permita modificar las cookies.
![[Screenshot_2022-10-07_13_40_19.png]]
![[Screenshot_2022-10-07_13_43_06.png]]
En la esquina inferior derecha tendremos una galleta como icono de la extencion, le damos click. Para esto, ya podemos cerrar el inspeccionador de la pàgina.
![[Screenshot_2022-10-07_13_44_09.png]]
Al dar click en la galleta se nos abre una ventana como la siguiente, buscamos el usuario que ingresamos, damos click y ahpi nos sale la info, cambiamos el "False· que biene por default por un "True", guardamos, y recargamos la pàgina.
![[20221007_125327.jpg]]
Y asì obtenemos la flag para este reto.
![[Screenshot_2022-10-07_14_17_05.png]]

picoCTF{th3_c0nsp1r4cy_l1v3s_6edb3f5f}

## Referencias
- []()