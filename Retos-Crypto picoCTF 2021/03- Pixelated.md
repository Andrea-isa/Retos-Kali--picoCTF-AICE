# Pixelated
## Objetivo
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/e8054e22552c6aba591cdf7440eb25e4/scrambled2.png)

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ ls
'01- Mind your Ps and Qs.md'  '02- No Padding, No Problem.md'  '03- Pixelated.md'   Help-pictures-notes   scrambled1.png   scrambled2.png   values

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ nano exp.py

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ ls
'01- Mind your Ps and Qs.md'  '02- No Padding, No Problem.md'  '03- Pixelated.md'   exp.py   Help-pictures-notes   scrambled1.png   scrambled2.png   values

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ python exp.py
[[[136 247 125]
  [208  80 246]
  [143 106 187]
  ...
  [179 117 100]
  [205 111  94]
  [251 222 172]]

 [[ 76  54 213]
  [223 253   2]
  [210  52 254]
  ...
  [223 150 249]
  [174 205  47]
  [ 61 105  66]]

 [[159  26 231]
  [243 100 162]
  [ 50  43 104]
  ...
  [ 52  81 209]
  [214 147 172]
  [145 121 151]]

 ...

 [[215 213 222]
  [180  73 164]
  [119 210 100]
  ...
  [183 193 103]
  [  0  45 154]
  [120  39 234]]

 [[134  22  22]
  [103  99 189]
  [202 155 152]
  ...
  [ 97 131 169]
  [ 64  82  73]
  [ 11 101  64]]

 [[238 106  49]
  [178  13 103]
  [227  80 225]
  ...
  [ 24 104  26]
  [ 65  47 130]
  [ 65  25  16]]]
[[[119   8 130]
  [ 47 175   9]
  [112 149  68]
  ...
  [ 76 138 155]
  [ 50 144 161]
  [  4  33  83]]

 [[179 201  42]
  [ 32   2 253]
  [ 45 203   1]
  ...
  [ 32 105   6]
  [ 81  50 208]
  [194 150 189]]

 [[ 96 229  24]
  [ 12 155  93]
  [205 212 151]
  ...
  [203 174  46]
  [ 41 108  83]
  [110 134 104]]

 ...

 [[ 40  42  33]
  [ 75 182  91]
  [136  45 155]
  ...
  [ 72  62 152]
  [255 210 101]
  [135 216  21]]

 [[121 233 233]
  [152 156  66]
  [ 53 100 103]
  ...
  [158 124  86]
  [191 173 182]
  [244 154 191]]

 [[ 17 149 206]
  [ 77 242 152]
  [ 28 175  30]
  ...
  [231 151 229]
  [190 208 125]
  [190 230 239]]]

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ ls
'01- Mind your Ps and Qs.md'     '03- Pixelated.md'   Help-pictures-notes   scrambled1.png   values
'02- No Padding, No Problem.md'   exp.py              nueva.png             scrambled2.png

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ open nueva.png

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$
```

```python
from PIL import Image
import numpy as np

img1=np.asarray(Image.open('scrambled1.png'))
img2=np.asarray(Image.open('scrambled2.png'))

print(img1)
print(img2)

datos=img1.copy() + img2.copy()

nueva = Image.fromarray(datos)

nueva.save('nueva.png','PNG')
```

![[nueva.png]]

picoCTF{d72ea4af}

## Referencias
- []()
