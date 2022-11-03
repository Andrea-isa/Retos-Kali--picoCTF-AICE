# Includes
## Objetivo
Can you get the flag? Go to this [website](http://saturn.picoctf.net:57833/) and see what you can discover.

## Soluciòn
Al inspeccionar la pàgina a la que nos dirige el link que no proporsiona este reto, vemos que en el còdigo hay una parte oculta, trata de un archivo llamado *script.js*, posiblemente se trate de una pista, asì que vamos a ver ese archivo.

![[Screenshot_2022-10-12_15_19_41.png]]

Para ver ese archivo, vamos a la parte de Debuger para inspeccionarlo, y vemos una parte de la flag, està en un comentario. Debmos seguir inspeccionando para ver donde màs podemos encontrar las otras partes de la flag.

![[Screenshot_2022-10-12_15_24_47.png]]

Y asì llegamos a la parte de Style Editor, en donde inspeccionamos un acrchivo llamado *style.css* y encontramos la otra parte de la flag comentada.

![[Screenshot_2022-10-12_15_26_59.png]]

Y lo ùnico que queda por hacer es juntar ambas partes.

picoCTF{1nclu51v17y_1of2_f7w_2of2_b8f4b022}

## Referencias
- []()