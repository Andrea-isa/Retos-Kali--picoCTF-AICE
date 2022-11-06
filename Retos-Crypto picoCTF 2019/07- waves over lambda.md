# waves over lambda
## Objetivo
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 13758`.

## Soluciòn

El texto que se nos da es un cifrado por sustituciòn, por lo que usamos una herramienta llamada 'Substitution Solver.'
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2019/Help-pictures-notes]
└─$ nc jupiter.challenges.picoctf.org 13758
-------------------------------------------------------------------------------
bqweytai phyh mi sqfy clte - cyhvfhwbs_mi_b_quhy_ltjoxt_xwuacyatsf
-------------------------------------------------------------------------------
nh nhyh wqa jfbp jqyh aptw t vftyahy qc tw pqfy qfa qc qfy ipmk amll nh itn phy imwz, twx aphw m fwxhyiaqqx cqy aph cmyia amjh npta nti jhtwa os t ipmk cqfwxhymwe mw aph iht.  m jfia tbzwqnlhxeh m ptx ptyxls hshi aq lqqz fk nphw aph ihtjhw aqlx jh iph nti imwzmwe; cqy cyqj aph jqjhwa apta aphs ytaphy kfa jh mwaq aph oqta aptw apta m jmepa oh itmx aq eq mw, js phtya nti, ti ma nhyh, xhtx nmapmw jh, ktyals nmap cymepa, ktyals nmap pqyyqy qc jmwx, twx aph apqfepai qc npta nti sha ohcqyh jh.
```

Elegimos el lenguaje en inglès y damos click en el botòn 'Break Cipher'

![[Screenshot_2022-11-06_15_35_56.png]]

Y el resultado es un texto en inglès, el cual ya contiene la flag.

![[Screenshot_2022-11-06_15_36_10.png]]


```text
-------------------------------------------------------------------------------
congrats here is your flag - frequency_is_c_over_lambda_dnvtfrtayu
-------------------------------------------------------------------------------
we were not much more than a quarter of an hour out of our ship till we saw her sink, and then i understood for the first time what was meant by a ship foundering in the sea.  i must acknowledge i had hardly eyes to look up when the seamen told me she was sinking; for from the moment that they rather put me into the boat than that i might be said to go in, my heart was, as it were, dead within me, partly with fright, partly with horror of mind, and the thoughts of what was yet before me.
```

La pista que nos da el reto dice que la flag no està en el formato que comunmente usamos: picoCTF{}; asì que la llave es: frequency_is_c_over_lambda_dnvtfrtayu

## Referencias
- []()