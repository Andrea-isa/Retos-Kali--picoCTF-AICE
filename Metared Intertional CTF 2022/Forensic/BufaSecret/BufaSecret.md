# BufaSecret
## Objetivo
Juan the explororer extracted this file from the site on the last expedition, but it appears to have been **corrupted**. This may be the secret code to open Francisco Villa vault that was found inside the "Cerro de la Bufa" in Zacatecas City. Can you identify what it once was and possibly fix it ? .

On June 23, 1914, this place was the scene of the "La toma de Zacatecas" (1914), where the revolutionary troops of General Francisco Villa defeated the Huertista army, defining the destiny of the nation.

<�div class="row challenge-files text-center pb-3"> <�div class="col-md-4 col-sm-4 col-xs-12 file-button-wrapper d-block"> <�a class="btn btn-info btn-file mb-1 d-inline-block px-2 w-100 text-truncate" href="https://ctfd2022.anuies.mx/files/fcbf72d846e85a2c53e96f00d0d9edae/corrupted.dta?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk"> <�i class="fas fa-download"><�/i> <�small> corrupted.dta <�/small> <�/a> <�/div> <�/div>

## Solucion


```shell
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $ls
'corrupted.dta?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk'
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $xxd corrupted.dta\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk | head
00000000: 5047 890a 4e0d 0a1a 0d48 4400 5200 0049  PG..N....HD.R..I
00000010: 0000 0258 0000 0151 0806 0000 00a8 81d3  ...X...Q........
00000020: 8900 0001 8569 4343 5049 4343 2070 726f  .....iCCPICC pro
00000030: 6669 6c65 0000 2891 7d91 3d48 c340 1cc5  file..(.}.=H.@..
00000040: 5fd3 4a8b 5444 ec20 e290 a10a 8205 5111  _.J.TD. ......Q.
00000050: 47ad 4211 2a84 5aa1 5507 934b bfa0 4943  G.B.*.Z.U..K..IC
00000060: 92e2 e228 b816 1cfc 58ac 3ab8 38eb eae0  ...(....X.:.8...
00000070: 2a08 821f 208e 4e4e 8a2e 52e2 ff92 428b  *... .NN..R...B.
00000080: 580f 8efb f1ee dee3 ee1d 20d4 cb4c b302  X......... ..L..
00000090: e380 a6db 662a 1117 33d9 5531 f88a 0082  ....f*..3.U1....
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $mv corrupted.dta\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk corrupted.png
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $ls
corrupted.png
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $hexedit corrupted.png 

		captura
		captura2
		
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $open corrupted.png 
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $

```

flagMX{you_found_my_secret_vault}



## Notas adicionales
## Referencias
