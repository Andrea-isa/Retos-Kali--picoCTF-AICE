# shark on wire 1

## Objetivo
We found this [packet capture](https://jupiter.challenges.picoctf.org/static/483e50268fe7e015c49caf51a69063d0/capture.pcap). Recover the flag.

## Soluciòn
Usamos la herramienta que nos dicen las pistas, se llama Wireshark, viene incluida en nuestra màquina Kali Linux. La abrimos y en esa misma abrimos el archivo que descargamos con el link que nos proporciona la descipciòn de este reto.

Al momento de abri el archivo se nos muestra lo siguiente:

![[Screenshot_2022-10-14_18_52_27.png]]

Y a la opciòn que dice: Simple Service iscovery Protocol; le damos click derecho, despues a la opciòn `Follow` y a `UDP Stream`. Nos abrirà una ventana.

![[Screenshot_2022-10-14_19_01_17.png]]

E iremos subiendo en la parte de `Stream` el nùmero, buscamos entre el texto que nos salga la flag.

![[Screenshot_2022-10-14_19_02_24.png]]

En mi caso tuve que increntar hasta el 6 para obtener la flag.

picoCTF{StaT31355_636f6e6e}

## Referencias
- []()