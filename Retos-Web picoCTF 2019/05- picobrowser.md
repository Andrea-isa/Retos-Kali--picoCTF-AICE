# picobrowser
## Objetivo
This website can be rendered only by **picobrowser**, go and catch the flag! `https://jupiter.challenges.picoctf.org/problem/50522/` ([link](https://jupiter.challenges.picoctf.org/problem/50522/)) or http://jupiter.challenges.picoctf.org:50522

## Soluciòn
Podemos cambiar el navegador por el que estamos entrando a la página mediante la herramineta de inspeccion de nuestro navegador actual, así ingresamos "picobrowser" como el nuevo navegador para que nos de como respuesta la bandera. Debemos cambiar la informaciòn del User-Agent, eso lo hacemos yendo a la parte de Network, dar click derecho sobre el dominio que tiene el documento flag con estatus 200, y elegimos a editar y reenviar; se abrirà una ventana al lado de la tabla del Network para poder cambiar esa informaciòn.
![[Screenshot_2022-10-07_15_09_47.png]]
Le damos en el botòn azul que dice Send y se uardarà en otro dominio hasta abajo de la tabla, damos click, se abre otra ventana al lado. luego vamos a la parte de Response, Ahì se verà una preview de la pàgina ya con la flag.

![[Screenshot_2022-10-07_15_06_28.png]]

picoCTF{p1c0_s3cr3t_ag3nt_51414fa7}

## Referencias
- []()