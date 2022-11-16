# morse-code
## Objetivo
Morse code is well known. Can you decrypt this? Download the file [here](https://artifacts.picoctf.net/c/235/morse_chal.wav). Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ ls
'01- basic-mod1.md'  '02- credstuff.md'  '03- morse-code.md'  '04- rail fence.md'   Help-pictures-notes   leak   leak.tar   message.txt   morse_chal.wav   msg.py

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ file morse_chal.wav
morse_chal.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 44100 Hz

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$
```

Usè una decodificador de audios en còdigo morse.

![[Screenshot_2022-11-16_15_01_44.png]]

Click sobre `Upload` y elegimos el audio.

![[Screenshot_2022-11-16_15_02_56.png]]

![[Screenshot_2022-11-16_15_04_02.png]]

![[Screenshot_2022-11-16_15_05_55.png]]

Damos click en `Play`  y en la barra de abajo saldràn las letras ya decodificadas.

![[Screenshot_2022-11-16_15_08_04.png]]

![[Screenshot_2022-11-16_15_13_20.png]]

Ahora solo es cuestiòn de que acomodemos la flag para dar con la correcta, en mi caso es la siguiente:
- picoCTF{wh47_h47h_90d_w20u9h7}

## Referencias
- []()