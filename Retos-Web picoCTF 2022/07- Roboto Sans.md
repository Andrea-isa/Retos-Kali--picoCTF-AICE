# Roboto Sans
## Objetivo
The flag is somewhere on this web application not necessarily on the website. Find it. Check [this](http://saturn.picoctf.net:64710/) out.

## Soluciòn
Al acceder a la pàgina, e inspeccionamos la pàina, buscamos flag en el còdigo HTML.

![[Screenshot_2022-10-14_13_34_47.png]]

Y vemos que el còdio nos dice:  < -- six_box end six_box   The flag is not here but keep digging :)-- > <! -- We Do Yogas 
Por lo que si buscamos en el archivo de *styles.css* se nos dice lo siguiente: 
/** banner_main {{Flag}} ** 

![[Screenshot_2022-10-14_14_00_14.png]]

Asì que, la pàina no està protegida, vamos a acceder al documento llamado *robots.txt* y nos saldrà informaciòn.

![[Screenshot_2022-10-14_14_16_21.png]]

Vemos que puede que una de esas claves puede que estè en base64, asì que amos a un conversor para ver que nos dice cada una.
```shell
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

Usamos CyberChef para hacer la converciòn, y vemos que nos arrojan otro documento.

![[Screenshot_20221014-133557_Chrome.jpg]]
![[Screenshot_20221014-133607_Chrome.jpg]]

Por lo que accedemos a ese documento, nos mandan a una pàgina con la flag.

![[Screenshot_2022-10-14_14_39_01.png]]

picoCTF{Who_D03sN7_L1k5_90B0T5_032f1c2b}

## Referencias
- []()