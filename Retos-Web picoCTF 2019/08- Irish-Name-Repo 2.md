# Irish-Name-Repo 2
## Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/53751/` ([link](https://jupiter.challenges.picoctf.org/problem/53751/)). Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login! or http://jupiter.challenges.picoctf.org:53751

## Soluciòn
Es parecido al anterior, sòlo que aquì no se necesita inspeccionar el còdigo de la pàgina, ni cambiar nada de ello.

Si la inyeccion la hacemos de la siguiente forma nos arrojara la bandera, en el campo de username ponemos algùn usuario + '; 
``` shell
andrea_castro';
```
luego cualquier password, damos login y nos debera mostrar la bandera en una nueva pàgina de la siguiente manera
``` shell
# Logged in!

Your flag is: picoCTF{m0R3_SQL_plz_c34df170}
```
picoCTF{m0R3_SQL_plz_c34df170}

## Referencias
- []()