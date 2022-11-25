# Need For Speed
## Objetivo
The name of the game is [speed](https://www.youtube.com/watch?v=8piqd2BWeGI). Are you quick enough to solve this problem and keep it above 50 mph? [need-for-speed](https://jupiter.challenges.picoctf.org/static/27dd5548b14661f65ce3ac6a8a8f575b/need-for-speed).

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file need-for-speed
need-for-speed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2d0d401d07683664113690a7fb94413a0039d228, not stripped
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ./need-for-speed
Keep this thing over 50 mph!
============================

Creating key...
Not fast enough. BOOM!
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cp need-for-speed patched
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ r2 patched
Warning: run r2 with -e bin.cache=true to fix relocations in disassembly
[0x00000660]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x00000660]> af1
[0x00000660]> afl
0x00000660    1 43           entry0
0x00000690    4 50   -> 40   sym.deregister_tm_clones
0x000006d0    4 66   -> 57   sym.register_tm_clones
0x00000720    5 58   -> 51   sym.__do_global_dtors_aux
0x00000650    1 6            sym.imp.__cxa_finalize
0x00000760    1 10           entry.init0
0x000009d0    1 2            sym.__libc_csu_fini
0x0000076a    6 135          sym.decrypt_flag
0x0000080e    1 33           sym.alarm_handler
0x00000610    1 6            sym.imp.puts
0x00000640    1 6            sym.imp.exit
0x00000630    1 6            sym.imp.__sysv_signal
0x00000620    1 6            sym.imp.alarm
0x000008d8    4 66           sym.header
0x000009d4    1 9            sym._fini
0x0000087d    1 47           sym.get_key
0x000007f1    3 29           sym.calculate_key
0x00000960    4 101          sym.__libc_csu_init
0x0000091a    1 62           main
0x0000082f    3 78           sym.set_timer
0x000008ac    1 44           sym.print_flag
0x000005d8    3 23           sym._init
0x00000600    1 6            sym.imp.putchar
0x00000000   12 459  -> 485  loc.imp._ITM_deregisterTMCloneTable
[0x00000660]> s sym.get_key
[0x0000087d]> pdf
            ; CALL XREF from main @ 0x942
┌ 47: sym.get_key ();
│           0x0000087d      55             push rbp
│           0x0000087e      4889e5         mov rbp, rsp
│           0x00000881      488d3da00100.  lea rdi, str.Creating_key... ; 0xa28 ; "Creating key..." ; const char *s                   
│           0x00000888      e883fdffff     call sym.imp.puts           ; int puts(const char *s)                                      
│           0x0000088d      b800000000     mov eax, 0
│           0x00000892      e85affffff     call sym.calculate_key
│           0x00000897      8905bf072000   mov dword [obj.key], eax    ; [0x20105c:4]=0                                               
│           0x0000089d      488d3d940100.  lea rdi, str.Finished       ; 0xa38 ; "Finished" ; const char *s                           
│           0x000008a4      e867fdffff     call sym.imp.puts           ; int puts(const char *s)                                      
│           0x000008a9      90             nop
│           0x000008aa      5d             pop rbp
└           0x000008ab      c3             ret
[0x0000087d]> s sym.calculate_key
[0x000007f1]> s sym.calculate_key
[0x000007f1]> pdf
            ; CALL XREF from sym.get_key @ 0x892
┌ 29: sym.calculate_key ();
│           ; var uint32_t var_4h @ rbp-0x4
│           0x000007f1      55             push rbp
│           0x000007f2      4889e5         mov rbp, rsp
│           0x000007f5      c745fc401a80.  mov dword [var_4h], 0xd4801a40                                                             
│           ; CODE XREF from sym.calculate_key @ 0x807
│       ┌─> 0x000007fc      836dfc01       sub dword [var_4h], 1
│       ╎   0x00000800      817dfc200d40.  cmp dword [var_4h], 0xea400d20                                                             
│       └─< 0x00000807      75f3           jne 0x7fc
│           0x00000809      8b45fc         mov eax, dword [var_4h]
│           0x0000080c      5d             pop rbp
└           0x0000080d      c3             ret
[0x000007f1]> oo+
[0x000007f1]> s s 0x00000845
Cannot seek to unknown address 's 0x00000845'
[0x000007f1]> s 0x00000845
[0x00000845]> pd 1
│           0x00000845      bf0e000000     mov edi, 0xe
[0x00000845]> wa mov edi, 0xe
Written 5 byte(s) (mov edi, 0xe) = wx bf0e000000
[0x00000845]> wa mov dword [rbp-0x4], 0xec61038f
Written 7 byte(s) (mov dword [rbp-0x4], 0xec61038f) = wx c745fc8f0361ec                                                               
[0x00000845]> q
                                                                   
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ./patched
Keep this thing over 50 mph!
============================

zsh: illegal hardware instruction  ./patched
                                                                   
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ r2 patched
Warning: run r2 with -e bin.cache=true to fix relocations in disassembly
[0x00000660]> aaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Use -AA or aaaa to perform additional experimental analysis.
[0x00000660]> afl
0x00000660    1 43           entry0
0x00000690    4 50   -> 40   sym.deregister_tm_clones
0x000006d0    4 66   -> 57   sym.register_tm_clones
0x00000720    5 58   -> 51   sym.__do_global_dtors_aux
0x00000650    1 6            sym.imp.__cxa_finalize
0x00000760    1 10           entry.init0
0x000009d0    1 2            sym.__libc_csu_fini
0x0000076a    6 135          sym.decrypt_flag
0x0000080e    1 33           sym.alarm_handler
0x00000610    1 6            sym.imp.puts
0x00000640    1 6            sym.imp.exit
0x000008d8    4 66           sym.header
0x000009d4    1 9            sym._fini
0x0000087d    1 47           sym.get_key
0x000007f1    3 29           sym.calculate_key
0x00000960    4 101          sym.__libc_csu_init
0x0000091a    1 62           main
0x0000082f    1 30           sym.set_timer
0x000008ac    1 44           sym.print_flag
0x000005d8    3 23           sym._init
0x00000600    1 6            sym.imp.putchar
0x00000620    1 6            sym.imp.alarm
0x00000000   12 459  -> 485  loc.imp._ITM_deregisterTMCloneTable
0x00000630    1 6            sym.imp.__sysv_signal
[0x00000660]> s sym.get_key
[0x0000087d]> pdf
            ; CALL XREF from main @ 0x942
┌ 47: sym.get_key ();
│           0x0000087d      55             push rbp
│           0x0000087e      4889e5         mov rbp, rsp
│           0x00000881      488d3da00100.  lea rdi, str.Creating_key... ; 0xa28 ; "Creating key..." ; const char *s                   
│           0x00000888      e883fdffff     call sym.imp.puts           ; int puts(const char *s)                                      
│           0x0000088d      b800000000     mov eax, 0
│           0x00000892      e85affffff     call sym.calculate_key
│           0x00000897      8905bf072000   mov dword [obj.key], eax    ; [0x20105c:4]=0                                               
│           0x0000089d      488d3d940100.  lea rdi, str.Finished       ; 0xa38 ; "Finished" ; const char *s                           
│           0x000008a4      e867fdffff     call sym.imp.puts           ; int puts(const char *s)                                      
│           0x000008a9      90             nop
│           0x000008aa      5d             pop rbp
└           0x000008ab      c3             ret
[0x0000087d]> s sym.calculate_key
[0x000007f1]> s sym.calculate_key
[0x000007f1]> pdf
            ; CALL XREF from sym.get_key @ 0x892
┌ 29: sym.calculate_key ();
│           ; var uint32_t var_4h @ rbp-0x4
│           0x000007f1      55             push rbp
│           0x000007f2      4889e5         mov rbp, rsp
│           0x000007f5      c745fc401a80.  mov dword [var_4h], 0xd4801a40                                                             
│           ; CODE XREF from sym.calculate_key @ 0x807
│       ┌─> 0x000007fc      836dfc01       sub dword [var_4h], 1
│       ╎   0x00000800      817dfc200d40.  cmp dword [var_4h], 0xea400d20                                                             
│       └─< 0x00000807      75f3           jne 0x7fc
│           0x00000809      8b45fc         mov eax, dword [var_4h]
│           0x0000080c      5d             pop rbp
└           0x0000080d      c3             ret
[0x000007f1]> oo+
[0x000007f1]> s 0x000007f5
[0x000007f5]> pd 1
│           0x000007f5      c745fc401a80.  mov dword [var_4h], 0xd4801a40
[0x000007f5]> wa mov dword [rbp-0x4], 0xea400d21
Written 7 byte(s) (mov dword [rbp-0x4], 0xea400d21) = wx c745fc210d40ea
[0x000007f5]> q
                                                                            
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ ./patched 
Keep this thing over 50 mph!
============================

zsh: illegal hardware instruction  ./patched
                                                                            
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```
picoCTF{}

## Referencias
- []()