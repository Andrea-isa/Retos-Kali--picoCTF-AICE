# Mind your Ps and Qs
## Objetivo
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/2604f8b51a5cc62d38a3736938f19cef/values)

## Soluciòn

Antes de dar la soluciòn,  debemos tener encuenta estos puntos para poder dar respuesta:
```text
c - texto cifrado
m - mensajo en texto plano (lo que se va encriptar)
p - primo 1
q - primo 2
n - modulo
tn - totient n (euler)
e - exponente (llave publica, suele ser 216 + 1=65537 )
d - llave privada
```
Y estas operaciones base son las que necesitaremos:
```text
n = p * q
tn = (p-1)*(q-1)
d = e mod inv tn / python -> inverse(e,tn)

Encriptar
c = m^e mod n / python -> pow(m,e,n)

Desencriptar
m = c^d mod n / python -> pow(c,d,n)

```

Para poder obtener el mensaje desencriptado, como vemos en los puntos anteriores, debemos tener ciertos dato para poder realizar el reto. Este reto solamente nos da `c`, `n` y `e`, y como vemos, tambièn necesitamos `p` y `q`, pero no tenemos esos datos, tenemos `n`, podemos usar este dato para obtener `p` y `q`, para esto necesitamos una herramienta que nos permitirà factorizar `n` y obtener los multiplos `p` y `q`.

![[Screenshot_2022-11-10_09_42_14.png]]

La herramienta nos da 2 datos, los cuales tomaremos como `p` y `q`. 
http://factordb.com/index.php?query=1311097532562595991877980619849724606784164430105441327897358800116889057763413423

![[Screenshot_2022-11-11_18_52_13.png]]


Para este reto usaremos python, asì como en retos pasados en categorìas diferentes.

```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ ls
'01- Mind your Ps and Qs.md'   values

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ cat values
Decrypt my super sick RSA:
c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
e: 65537                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ 
```

```python
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Crypto picoCTF 2021]
└─$ python
Python 3.10.5 (main, Jun  8 2022, 09:26:22) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> c=861270243527190895777142537838333832920579264010533029282104230006461420086153423
>>> e=65537
>>> p=1955175890537890492055221842734816092141
>>> q=670577792467509699665091201633524389157003
>>> n = p * q
>>> n
1311097532562595991877980619849724606784164430105441327897358800116889057763413423
>>> tn = (p-1)*(q-1)
>>> from Crypto.Util.number import inverse
>>> d=inverse(e,tn)
>>> from Crypto.Util.number import long_to_bytes
>>> m=pow(c,d,n)
>>> long_to_bytes(m)
b'picoCTF{sma11_N_n0_g0od_13686679}'
>>>
```

## Referencias
- []()