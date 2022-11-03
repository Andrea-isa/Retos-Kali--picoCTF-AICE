# Scavenger Hunt
## Objetivo
There is some interesting information hidden around this site [http://mercury.picoctf.net:39698/](http://mercury.picoctf.net:39698/). Can you find it?

## Soluciòn
Vamos a inspeccionar la pàgina que carga al dar click en el link que nos da este reto.
Si buscamos en el còdigo html nos sale esto:
```shell
	
	<!-- Here's the first part of the flag: picoCTF{t -->
      
```
![[Screenshot_2022-10-07_20_19_39.png]]

Asì nos damos cuenta de que debemos inspeccionar el el resto de còdigo como CSS y JvaScript para ver si estàn las demàs partes de la flag.
La otra parte està en el còdigo CSS
```shell
/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

![[Screenshot_2022-10-07_20_23_22.png]]

En el javascript esta esto
```shell
/* How can I keep Google from indexing my website? */
```

![[Screenshot_2022-10-07_20_29_05.png]]

por esto podemos pensar que estara en robots.txt
```shell
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

![[Screenshot_2022-10-07_20_38_51.png]]

Existe un archivo que no podemos verlo, el cual es .htaccess, ahi se encuentra otra parte de la bandera
```shell
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

![[Screenshot_2022-10-07_20_40_47.png]]

Un error de los desarrolladores, si lo hacen desde Mac, es subir toda la carpeta, esta incluye un archivo .DS_Store, aqui la subieron, asi que ahì se encuentra la ùltima parte de la flag de este reto.
```shell
Congrats! You completed the scavenger hunt. Part 5: _fa04427c}
```

![[Screenshot_2022-10-07_20_40_47 1.png]]

Solo nos queda juntar todas las partes para formar la flag.
picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_fa04427c}

## Referencias
- []()