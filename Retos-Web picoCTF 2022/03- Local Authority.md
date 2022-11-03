# Local Authority
## Objetivo
Can you get the flag? Go to this [website](http://saturn.picoctf.net:55826/) and see what you can discover.

## Soluciòn
Al entrar a la pàgina que nos da este reto podemos ver una pàgina para loggearnos.

![[Screenshot_2022-10-14_12_14_22.png]]

Si ententamos entrar con cualquier usuario y una contraseña random podemos ver que, al inspecionar la pàgina, en la parte de Network vemos dos dominos con los archvos *login.php* y *secure.js* , podemos analizar a ambos archivos dando click derecho y en abrir en nueva pestaña, nos abrirà una nueva penstaña. 

![[Screenshot_2022-10-14_12_21_45 1.png]]

El archivo *secure.js* nos muestra un còdigo.

![[Screenshot_2022-10-14_12_23_54.png]]

El còdigo es el siguiente, el cual nos da el usuario y la contraseña, ingresamos ambos datos a la pàgina de inicio para logearnos.
```shell
function checkPassword(username, password)
{
  if( username === 'admin' && password === 'strongPassword098765' )
  {
    return true;
  }
  else
  {
    return false;
  }
}
```

![[Screenshot_2022-10-14_12_33_21.png]]

Y al acceder nos dan inmediatamente la flag de este reto.

![[Screenshot_2022-10-14_12_34_14.png]]

picoCTF{j5_15_7r4n5p4r3n7_b0c2c9cb}

## Referencias
- []()