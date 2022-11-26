# Need For Speed
## Objetivo
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/27dd5548b14661f65ce3ac6a8a8f575b/need-for-speed).

## Soluciòn

```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file need-for-speed
need-for-speed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2d0d401d07683664113690a7fb94413a0039d228, not stripped

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ chmod -x need-for-speed

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ./need-for-speed
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ objdump -D need-for-speed -M intel | grep '<main>:' -A20
000000000000091a <main>:
 91a:   55                      push   rbp
 91b:   48 89 e5                mov    rbp,rsp
 91e:   48 83 ec 10             sub    rsp,0x10
 922:   89 7d fc                mov    DWORD PTR [rbp-0x4],edi
 925:   48 89 75 f0             mov    QWORD PTR [rbp-0x10],rsi
 929:   b8 00 00 00 00          mov    eax,0x0
 92e:   e8 a5 ff ff ff          call   8d8 <header>
 933:   b8 00 00 00 00          mov    eax,0x0
 938:   e8 f2 fe ff ff          call   82f <set_timer>
 93d:   b8 00 00 00 00          mov    eax,0x0
 942:   e8 36 ff ff ff          call   87d <get_key>
 947:   b8 00 00 00 00          mov    eax,0x0
 94c:   e8 5b ff ff ff          call   8ac <print_flag>
 951:   b8 00 00 00 00          mov    eax,0x0
 956:   c9                      leave
 957:   c3                      ret
 958:   0f 1f 84 00 00 00 00    nop    DWORD PTR [rax+rax*1+0x0]
 95f:   00 

0000000000000960 <__libc_csu_init>:

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ sudo apt install gdb
[sudo] password for kali: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  liblerc3 libplacebo192 libsvtav1enc0
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libbabeltrace1 libboost-iostreams1.74.0 libboost-regex1.74.0 libboost-thread1.74.0 libc6-dbg libdebuginfod-common libdebuginfod1 libipt2
  libsource-highlight-common libsource-highlight4v5
Suggested packages:
  gdb-doc gdbserver
The following NEW packages will be installed:
  gdb libbabeltrace1 libboost-regex1.74.0 libc6-dbg libdebuginfod-common libdebuginfod1 libipt2 libsource-highlight-common libsource-highlight4v5
The following packages will be upgraded:
  libboost-iostreams1.74.0 libboost-thread1.74.0
2 upgraded, 9 newly installed, 0 to remove and 1110 not upgraded.
Need to get 12.3 MB/12.6 MB of archives.
After this operation, 27.5 MB of additional disk space will be used.
Do you want to continue? [Y/n] Y
Get:1 http://http.kali.org/kali kali-rolling/main amd64 libboost-regex1.74.0 amd64 1.74.0-17+b2 [487 kB]
Get:2 http://http.kali.org/kali kali-rolling/main amd64 libsource-highlight4v5 amd64 3.1.9-4.2+b2 [257 kB]
Get:3 http://kali.download/kali kali-rolling/main amd64 gdb amd64 12.1-4 [3,595 kB]
Get:4 http://http.kali.org/kali kali-rolling/main amd64 libboost-iostreams1.74.0 amd64 1.74.0-17+b2 [240 kB]
Get:5 http://http.kali.org/kali kali-rolling/main amd64 libboost-thread1.74.0 amd64 1.74.0-17+b2 [257 kB]
Get:6 http://kali.download/kali kali-rolling/main amd64 libc6-dbg amd64 2.36-4 [7,448 kB]
Fetched 12.3 MB in 6s (2,105 kB/s)              
Preconfiguring packages ...
Selecting previously unselected package libdebuginfod-common.
(Reading database ... 342407 files and directories currently installed.)
Preparing to unpack .../00-libdebuginfod-common_0.187-4_all.deb ...
Unpacking libdebuginfod-common (0.187-4) ...
Selecting previously unselected package libbabeltrace1:amd64.
Preparing to unpack .../01-libbabeltrace1_1.5.11-1+b1_amd64.deb ...
Unpacking libbabeltrace1:amd64 (1.5.11-1+b1) ...
Selecting previously unselected package libdebuginfod1:amd64.
Preparing to unpack .../02-libdebuginfod1_0.187-4_amd64.deb ...
Unpacking libdebuginfod1:amd64 (0.187-4) ...
Selecting previously unselected package libipt2.
Preparing to unpack .../03-libipt2_2.0.5-1_amd64.deb ...
Unpacking libipt2 (2.0.5-1) ...
Selecting previously unselected package libsource-highlight-common.
Preparing to unpack .../04-libsource-highlight-common_3.1.9-4.2_all.deb ...
Unpacking libsource-highlight-common (3.1.9-4.2) ...
Selecting previously unselected package libboost-regex1.74.0:amd64.
Preparing to unpack .../05-libboost-regex1.74.0_1.74.0-17+b2_amd64.deb ...
Unpacking libboost-regex1.74.0:amd64 (1.74.0-17+b2) ...
Selecting previously unselected package libsource-highlight4v5:amd64.
Preparing to unpack .../06-libsource-highlight4v5_3.1.9-4.2+b2_amd64.deb ...
Unpacking libsource-highlight4v5:amd64 (3.1.9-4.2+b2) ...
Selecting previously unselected package gdb.
Preparing to unpack .../07-gdb_12.1-4_amd64.deb ...
Unpacking gdb (12.1-4) ...
Preparing to unpack .../08-libboost-iostreams1.74.0_1.74.0-17+b2_amd64.deb ...
Unpacking libboost-iostreams1.74.0:amd64 (1.74.0-17+b2) over (1.74.0-16.1) ...
Preparing to unpack .../09-libboost-thread1.74.0_1.74.0-17+b2_amd64.deb ...
Unpacking libboost-thread1.74.0:amd64 (1.74.0-17+b2) over (1.74.0-16.1) ...
Selecting previously unselected package libc6-dbg:amd64.
Preparing to unpack .../10-libc6-dbg_2.36-4_amd64.deb ...
Unpacking libc6-dbg:amd64 (2.36-4) ...
Setting up libdebuginfod-common (0.187-4) ...
Setting up libboost-iostreams1.74.0:amd64 (1.74.0-17+b2) ...
Setting up libdebuginfod1:amd64 (0.187-4) ...
Setting up libsource-highlight-common (3.1.9-4.2) ...
Setting up libc6-dbg:amd64 (2.36-4) ...
Setting up libboost-regex1.74.0:amd64 (1.74.0-17+b2) ...
Setting up libipt2 (2.0.5-1) ...
Setting up libbabeltrace1:amd64 (1.5.11-1+b1) ...
Setting up libsource-highlight4v5:amd64 (3.1.9-4.2+b2) ...
Setting up libboost-thread1.74.0:amd64 (1.74.0-17+b2) ...
Setting up gdb (12.1-4) ...
Processing triggers for libc-bin (2.36-4) ...
Processing triggers for man-db (2.10.2-1) ...
Processing triggers for kali-menu (2022.3.1) ...

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ gdb                          
GNU gdb (Debian 12.1-4) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word".
(gdb) q

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ gdb ./need-for-speed
GNU gdb (Debian 12.1-4) 12.1
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./need-for-speed...
(No debugging symbols found in ./need-for-speed)
(gdb) break set_timer
Breakpoint 1 at 0x833
(gdb) r
Starting program: /home/kali/Desktop/CarpetaCompartida.Windows/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019/need-for-speed 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Keep this thing over 50 mph!
============================


Breakpoint 1, 0x0000555555400833 in set_timer ()
(gdb) return
Make selected stack frame return now? (y or n) y
#0  0x000055555540093d in main ()
(gdb) step
Single stepping until exit from function main,
which has no line number information.
Creating key...
Finished
Printing flag:
PICOCTF{Good job keeping bus #1f2ac4ec speeding along!}
__libc_start_call_main (main=main@entry=0x55555540091a <main>, argc=argc@entry=1, argv=argv@entry=0x7fffffffde98) at ../sysdeps/nptl/libc_start_call_main.h:74
74      ../sysdeps/nptl/libc_start_call_main.h: No such file or directory.
(gdb) q
A debugging session is active.

        Inferior 1 [process 11138] will be killed.

Quit anyway? (y or n) y

┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```
picoCTF{Good job keeping bus #1f2ac4ec speeding along!}

## Referencias
- []()
