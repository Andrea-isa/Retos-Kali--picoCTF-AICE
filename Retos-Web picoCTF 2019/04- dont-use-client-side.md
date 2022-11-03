# dont-use-client-side
## Objetivo
Can you break into this super secure portal? `https://jupiter.challenges.picoctf.org/problem/29835/` ([link](https://jupiter.challenges.picoctf.org/problem/29835/)) or http://jupiter.challenges.picoctf.org:29835

## Soluciòn
Al inspeccioar el codigo de la página que se nos da, nos vamos en la parte de Debug para ver el còdigo, encontramos una funciòn con la bandera distribuida en diferentes condicionales if, entonces podemos obtener la bandera guiandonos con los numeros que tiene cada if
![[Screenshot_2022-10-07_14_24_55.png]]
```Javascript
if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == '723c') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_7') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == 'e}') {
                  alert("Password Verified")

1- if (checkpass.substring(0, split) == 'pico')
2- if (checkpass.substring(split, split*2) == 'CTF{') 
3- if (checkpass.substring(split*2, split*3) == 'no_c')
4- if (checkpass.substring(split*3, split*4) == 'lien')
5- if (checkpass.substring(split*4, split*5) == 'ts_p')
6- if (checkpass.substring(split*5, split*6) == 'lz_7')
7- if (checkpass.substring(split*6, split*7) == '723c')
8- if (checkpass.substring(split*7, split*8) == 'e}')
``` 
picoCTF{no_clients_plz_7723ce}

## Referencias
- []()