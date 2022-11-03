# Insp3ct0r
## Objetivo
Kishor Balan tipped us off that the following code may need inspection: `https://jupiter.challenges.picoctf.org/problem/44924/` ([link](https://jupiter.challenges.picoctf.org/problem/44924/)) or http://jupiter.challenges.picoctf.org:44924

## Soluciòn
Al dat click al link nos abre una pàgina que debemos inspeccionar, hay dos botones, da mos click en el que dice "How"  nos dice que debemos usar este sitio para hacer còdigo de HTML, CSS y JavaSript. 
Ahora lo que tenemos que hacer es dar click derecho sobre la pàgina y le damos en inspeccionar, se abrirà una ventana, e inspeccioamos primero el còdigo HTML, nos damos cuenta que en una parte del còdigo dice : *Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3*; por lo que asì nos damos cuenta de que debemos impeccionar el còdigo CSS y JavaScript para obtener la fla completa. Entonces hay tres partes a revisar en la página que nos dan.

```shell
Còdigo HTML
	Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3
	
Còdigo CSS
	You need CSS to make pretty pages. Here's' part 2/3 of the flag: 
    t3ct1ve_0r_ju5t
    
Còdigo JavaSript
	Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?f10be399}

```
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?f10be399}
 
## Referencias
- []()