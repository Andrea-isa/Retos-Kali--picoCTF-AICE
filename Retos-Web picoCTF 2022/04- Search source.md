# Search source
## Objetivo
The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is [here](http://saturn.picoctf.net:61941/)

## Soluciòn
Al acceder a la pàgina vamos a inspecionarlo, vemos en el còdigo HTML hay documentos de javascript ocultos.

![[Screenshot_2022-10-14_12_43_01.png]]

Ademàs de que si buscamos flag entre el còdig nos dice lo siguiente: 
-- six_box end six_box   The flag is not here but keep digging :)-- 

![[Screenshot_2022-10-14_12_46_29.png]]


Entonces demos seguir inspeccionando entre los archivos que podemos encontrar, por ejemplo en la secciòn de StylesEditor, en el cual encontrè la flag en el archivo llamado *style.css*. /** banner_main picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7} **/

![[Screenshot_2022-10-14_12_52_56.png]]

picoCTF{1nsp3ti0n_0f_w3bpag3s_8de925a7}
## Referencias
- []()