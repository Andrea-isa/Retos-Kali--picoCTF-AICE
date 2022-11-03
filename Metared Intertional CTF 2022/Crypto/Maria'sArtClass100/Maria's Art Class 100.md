# Maria's Art Class 100
## Objetivo
For María’s art class the teacher ask for a MASTERPIECE that combains history and feelings, so María decided to créate a painting that describes an event in history close to her heart and her roots. She decided to paint a piece of Yucatán that everyone can relate to, so she paint the kukulkan pirámide. María says that she hide a Little message in the painting but I guess the teacher never find it because María got an F. Help María to pass de class, find the message and send it to the teacher:3

## Solucion

```shell
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $ls
'corrupted.dta?token=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk'
┌─[kali㉿kali]─[~/CTFMETA/BufaSecret]
└──╼ $xxd corrupted.dta\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjV9.Y09mhQ.z1qAw6uTgckhid411vJfjagbTyk | head

...

┌─[kali㉿kali]─[~/CTFMETA/crypto/Marias]
└──╼ $mv KUKULKAN.jpg\?token\=eyJ1c2VyX2lkIjoxODgzLCJ0ZWFtX2lkIjo1MDYsImZpbGVfaWQiOjh9.Y09p5A.50YaFZqYQI9L5Ww2HWbyawUHndo KUKULKAN.jpg
┌─[kali㉿kali]─[~/CTFMETA/crypto/Marias]
└──╼ $strings KUKULKAN.jpg | grep FLAG
_I LOVE FLAGS :3 
.MY FAVOURITE WORD IS FLAG 
THIS IS NOT THE FLAG, KEEP LOOKING BRO! 
/ FLAG Un PAso mas  BRO{Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalJsSlZVMnhPVlUxV2NEQlVWbEpUWVdzeFYxTnNhRmRpVkZaUVZrUktTMUl5VGtsaVJtUk9ZbTFvZVZadE1YcGxSbGw0Vkc1V2FsSnNXazlXYlRWRFYxWmFkR1JIUmxSTlZYQjVWR3hhYjFSc1duTmpSVGxhWWxoU1RGWnNXbUZXVmtaMFVteHdWMkpJUWpaV1ZFa3hWREZhV0ZOclpHcFNWR3hZV1ZSS1VrMUdWWGRYYlVacVZtdHdlbGRyV210VWJGcDFVV3R3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ==}   x

┌─[kali㉿kali]─[~/CTFMETA/crypto/Marias]
└──╼ $

*Usando CyberChef se decodifica 

Vm0weGQxTnRVWGxXYTFwUFZsZG9WRmxVU2xOalJsSlZVMnhPVlUxV2NEQlVWbEpUWVdzeFYxTnNhRmRpVkZaUVZrUktTMUl5VGtsaVJtUk9ZbTFvZVZadE1YcGxSbGw0Vkc1V2FsSnNXazlXYlRWRFYxWmFkR1JIUmxSTlZYQjVWR3hhYjFSc1duTmpSVGxhWWxoU1RGWnNXbUZXVmtaMFVteHdWMkpJUWpaV1ZFa3hWREZhV0ZOclpHcFNWR3hZV1ZSS1VrMUdWWGRYYlVacVZtdHdlbGRyV210VWJGcDFVV3R3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ==

```

8 veces,  se copea el output y se ingresa en el input 
		
		captura

flagMX{R3TURN_TH3_J4GUARS_EYES}
