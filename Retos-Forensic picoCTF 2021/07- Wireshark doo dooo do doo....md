# Wireshark doo dooo do doo...
## Objetivo
Can you find the flag? [shark1.pcapng](https://mercury.picoctf.net/static/81c7862241faf4a48bd64a858392c92b/shark1.pcapng).

## Soluciòn
Abrimos el archivo descargado en la herramienta Wireshark. Y en la barra de bùsqueda escribimos 'tcp.stream eq 5', nos darà una lista y damos click derecho sobre el primer protocolo, o el que està resaltado, luego damos en 'Follow', nos abrirà una nueva ventana.

![[Screenshot_2022-11-04_20_26_46.png]]

luego tomamos el texto que està al final, lo llevamos a la consola para decodificarlo con ROT13.

![[Screenshot_2022-11-04_20_27_04.png]]

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$ echo 'cvpbPGS{c33xno00_1_f33_h_qrnqorrs}' | tr 'A-Za-z' 'N-ZA-Mn-za-m'
picoCTF{p33kab00_1_s33_u_deadbeef}

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2021]
└─$
```
picoCTF{p33kab00_1_s33_u_deadbeef}

## Referencias
- []()