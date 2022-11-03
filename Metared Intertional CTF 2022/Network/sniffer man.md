# Sniffer man
## Objetivo
 Mi organización ha aprendido sobre seguridad cibernética de la manera más difícil en los últimos años.

## Solucion

```shell
┌──(kali㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ ls
challenge.pcapng
                                                                                 
┌──(kali㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ file challenge.pcapng  
challenge.pcapng: pcapng capture file - version 1.0
                                                                                 
┌──(kali㉿kali)-[~/Escritorio/HakinKali/MetaCTF/siffer man]
└─$ wireshark challenge.pcapng

```

xdsyEP{E2f_9f_Lz1_E9vvd1_2ll2uc}
flagMX{M2n_9n_Th1_M9ddl1_2tt2ck}
modificamos la bandera cambiando los 2 por 4 los 9 por 1 y los 1 por 3


flagMX{M4n_1n_Th3_M1ddl3_4tt4ck}