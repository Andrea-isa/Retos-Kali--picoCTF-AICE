# m00nwalk
## Objetivo
Decode this [message](https://jupiter.challenges.picoctf.org/static/14393e18d98fedbaedbc28896d7ef31a/message.wav) from the moon.

## Soluciòn

Primero tenemos que hacer lo siguiente, eswto par poder usar un comando.
```shell
┌──(kali㉿kali)-[~]
└─$ cd /opt                               

┌──(kali㉿kali)-[/opt]
└─$ sudo git clone https://github.com/colaclanth/sstv.git
[sudo] password for kali: 
Cloning into 'sstv'...
remote: Enumerating objects: 221, done.
remote: Total 221 (delta 0), reused 0 (delta 0), pack-reused 221
Receiving objects: 100% (221/221), 1.01 MiB | 856.00 KiB/s, done.
Resolving deltas: 100% (140/140), done.

┌──(kali㉿kali)-[/opt]
└─$ ls
microsoft  sstv

┌──(kali㉿kali)-[/opt]
└─$ cd sstv         

┌──(kali㉿kali)-[/opt/sstv]
└─$ ls
examples  LICENSE  README.md  setup.py  sstv  test
    
┌──(kali㉿kali)-[/opt/sstv]
└─$ sudo python setup.py install
running install
/usr/lib/python3/dist-packages/setuptools/command/install.py:34: SetuptoolsDeprecationWarning: setup.py install is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
/usr/lib/python3/dist-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.
  warnings.warn(
^[[B^[[B^[[Brunning bdist_egg
running egg_info
creating sstv.egg-info
writing sstv.egg-info/PKG-INFO
writing dependency_links to sstv.egg-info/dependency_links.txt
writing entry points to sstv.egg-info/entry_points.txt
writing requirements to sstv.egg-info/requires.txt
writing top-level names to sstv.egg-info/top_level.txt
writing manifest file 'sstv.egg-info/SOURCES.txt'
reading manifest file 'sstv.egg-info/SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'sstv.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
creating build/lib/sstv
copying sstv/common.py -> build/lib/sstv
copying sstv/command.py -> build/lib/sstv
copying sstv/__main__.py -> build/lib/sstv
copying sstv/decode.py -> build/lib/sstv
copying sstv/__init__.py -> build/lib/sstv
copying sstv/spec.py -> build/lib/sstv
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/common.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/command.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__main__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/decode.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/__init__.py -> build/bdist.linux-x86_64/egg/sstv
copying build/lib/sstv/spec.py -> build/bdist.linux-x86_64/egg/sstv
byte-compiling build/bdist.linux-x86_64/egg/sstv/common.py to common.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/command.py to command.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/__main__.py to __main__.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/decode.py to decode.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/__init__.py to __init__.cpython-310.pyc
byte-compiling build/bdist.linux-x86_64/egg/sstv/spec.py to spec.cpython-310.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying sstv.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating dist
creating 'dist/sstv-0.1-py3.10.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing sstv-0.1-py3.10.egg
Removing /usr/local/lib/python3.10/dist-packages/sstv-0.1-py3.10.egg
Copying sstv-0.1-py3.10.egg to /usr/local/lib/python3.10/dist-packages
sstv 0.1 is already the active version in easy-install.pth
Installing sstv script to /usr/local/bin

Installed /usr/local/lib/python3.10/dist-packages/sstv-0.1-py3.10.egg
Processing dependencies for sstv==0.1
Searching for scipy==1.7.3
Best match: scipy 1.7.3
Adding scipy 1.7.3 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for numpy==1.21.5
Best match: numpy 1.21.5
Adding numpy 1.21.5 to easy-install.pth file
Installing f2py script to /usr/local/bin
Installing f2py3 script to /usr/local/bin
Installing f2py3.10 script to /usr/local/bin

Using /usr/lib/python3/dist-packages
Searching for PySoundFile==0.9.0.post1
Best match: PySoundFile 0.9.0.post1
Processing PySoundFile-0.9.0.post1-py3.10.egg
PySoundFile 0.9.0.post1 is already the active version in easy-install.pth

Using /usr/local/lib/python3.10/dist-packages/PySoundFile-0.9.0.post1-py3.10.egg
Searching for Pillow==9.2.0
Best match: Pillow 9.2.0
Adding Pillow 9.2.0 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Searching for cffi==1.15.1
Best match: cffi 1.15.1
Adding cffi 1.15.1 to easy-install.pth file

Using /usr/lib/python3/dist-packages
Finished processing dependencies for sstv==0.1
   
┌──(kali㉿kali)-[/opt/sstv]
└─$ 
```
Si no instalaos lo anterior no podreos usar el comando que necesitamos.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ sstv -d message.wav -o message-resultado.png
Command 'sstv' not found, did you mean:
  command 'qsstv' from deb qsstv
Try: sudo apt install <deb name>
```
Ahora hacemos lo siguiente, el archivo de audio que nos dan es en realidad una imagen codificada en SSTV con su variante scottie, si buscamos un decodificador podremos resolverlo, segùn lo especificado en las pistas. Usando la herramienta sstv que encontramos en git decodificamos el audio.
```shell
┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ sstv -d message.wav -o message-resultado.png
[sstv] Searching for calibration header... Found!    
[sstv] Detected SSTV mode Scottie 1
[sstv] Decoding image...                                    [####################################################################################################] 100%
[sstv] Drawing image data...
[sstv] ...Done!

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$ open message-resultado.png

┌──(kali㉿kali)-[~/…/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Forensic picoCTF 2019]
└─$

```

![[message-resultado.png]]
Como podemos ver, la imagen contiene la flag.
picoCTF{beep_boop_im_in_space}

## Referencias
- []()