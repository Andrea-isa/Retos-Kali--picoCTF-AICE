# rail fence
## Objetivo
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it? Download the message [here](https://artifacts.picoctf.net/c/274/message.txt). Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ ls
'01- basic-mod1.md'  '02- credstuff.md'  '03- morse-code.md'  '04- rail fence.md'   Help-pictures-notes   leak   leak.tar   message.txt   morse_chal.wav   msg.py

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ file message.txt   
message.txt: ASCII text, with no line terminators

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$ cat message.txt           
Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA   

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2022]
└─$
```

![[Screenshot_2022-11-16_15_34_02.png]]

picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_D00AFDD3}

## Referencias
- []()