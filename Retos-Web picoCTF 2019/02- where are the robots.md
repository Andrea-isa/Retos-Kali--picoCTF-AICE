# where are the robots
## Objetivo
Can you find the robots? `https://jupiter.challenges.picoctf.org/problem/60915/` ([link](https://jupiter.challenges.picoctf.org/problem/60915/)) or http://jupiter.challe

## Soluciòn

```shell
El nombre del reto nos dice que una parte que el desarrollador no quiere que veamos es el archivo robots.txt, ingresamos a el directamente desde la barra de navegación y podemos ver otra parte de la página que no se desea que observemos, entramos a ella y ahí es donde se encuentra la bandera.

Ademàs, podemos hacer lo siguiente desde consola usando el comando curl para mostrar el contenido.

──(kali㉿kali)-[~/…/CarpetaKali-exam1/Retos-Web picoCTF/pico-2021/Retos-Web picoCTF 2019]
└─$ curl https://jupiter.challenges.picoctf.org/problem/60915/robots.txt
User-agent: *
Disallow: /8028f.html
  
┌──(kali㉿kali)-[~/…/CarpetaKali-exam1/Retos-Web picoCTF/pico-2021/Retos-Web picoCTF 2019]
└─$ curl https://jupiter.challenges.picoctf.org/problem/60915/8028f.html
<!doctype html>
<html>
  <head>
    <title>Where are the robots</title>
    <link href="https://fonts.googleapis.com/css?family=Monoton|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="style.css">
  </head>
  <body>
    <div class="container">
      
      <div class="content">
        <p>Guess you found the robots<br />
          <flag>picoCTF{ca1cu1at1ng_Mach1n3s_8028f}</f</p>
      </div>
      <footer></footer>
  </body>
</html>
   
┌──(kali㉿kali)-[~/…/CarpetaKali-exam1/Retos-Web picoCTF/pico-2021/Retos-Web picoCTF 2019]
└─$ curl https://jupiter.challenges.picoctf.org/problem/60915/8028f.html | grep 'picoCTF'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
  Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--100   453  100   453    0     
  0    836      0 --:--:-- --:--:-- --:--:--   840
   <flag>picoCTF{ca1cu1at1ng_Mach1n3s_8028f}</flag></p>
 
┌──(kali㉿kali)-[~/…/CarpetaKali-exam1/Retos-Web picoCTF/pico-2021/Retos-Web picoCTF 2019]
└─$ 

```
picoCTF{ca1cu1at1ng_Mach1n3s_8028f}

## Referencias
- []()