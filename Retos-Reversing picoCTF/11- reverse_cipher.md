# reverse_cipher
## Objetivo
We have recovered a [binary](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev) and a [text file](https://jupiter.challenges.picoctf.org/static/7aa5f383ec616fe9d72c2ffe1fabd0d9/rev_this). Can you reverse the flag.

## Soluciòn
```shell
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file rev   
rev: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=523d51973c11197605c76f84d4afb0fe9e59338c, not stripped
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ file rev_this
rev_this: ASCII text, with no line terminators
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat rev_this
picoCTF{w1{1wq84fb<1>49}                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat rev     
ELF>�@X:@8
          @@@@h���xx==   ���-�=�=px�-�=�=����DDP�tdx x x <<Q�tdR�td�-�=�=▒▒/lib64/ld-linux-x86-64.so.2GNUGNUR=Q�<v�o�ԯ���Y3�
                                                                                                                            �
                                                                                                                             �e�m[ (!w 
                                                                                                                                       � ."libc.so.6exitfopenputsfputcfclosefread__cxa_finalize__libc_start_mainGLIBC_2.2.5_ITM_deregisterTMCloneTable__gmon_start___ITM_registerTMCloneTableu▒i       O���@PP@�?�?�?�?
�?
H�=��/�DH�=�/H�z/H9�tH��.H��t��������H�=Q/H�5J/H)�H��H��H��?H�H��tH��.H����fD���=/u/UH�=�.H��th������%b/f�1�I��^H��H���PTL�zH�
                                                                                              H�=�.�-����h�����.]�����{���UH��H��PH�5tH�=o�����H�E�H�5hH�=c�����H�E�H�}�u
  H�=W�b���H�}�u
                H�=~�O���H�U�H�E�H�Ѻ�▒H���B����E܃}�
��o����E��#�E�H��D��E��E�H�U�H�։��'����E��}�~��E�C�E�H��D��E��E�����u
                                                                     �E����E��
�E����E��E�H�U�H�։�������E��}�~��EǈE��E�H�U�H�։������H�E�H�������H�E�H�����������AWI��AVI��AUA��ATL�%+UH�-+SL)�H�����H��t�L��L��D��A��H��H9�u�H�[]A\A]A^A_��H�H��rflag.����X��������0zRxag found, please make sure this is run on the serverplease run this on the server<�����▒����(���X
                ����+zRx
                       $▒���pF▒J
?                               �?▒;*3$"D`��\=���DA�C
D|h���]B�E▒�E �E(�H0�H8�G@j8A0A(B B▒B������@
4�▒����P0
�
 ▒@���  ▒���������o���o����o�=6FVfv�P@GCC: (Debian 8.2.0-14) 8.2.0��0P� (
�

��4 x � �=�=�=�?@▒H@X@▒��
                         �!@7X@F�=m�y�=�������!����=��=��=�x �@�
                                                                0 � ▒H@.@S▒X@Z
                                                                              4n��▒H@� �▒P@� ��]�`@��+�X@��D�
                                                                                                             ▒X@* D"crtstuff.cderegister_tm_clones__do_global_dtors_auxcompleted.7325__do_global_dtors_aux_fini_array_entryframe_dummy__frame_dummy_init_array_entryrev.c__FRAME_END____init_array_end_DYNAMIC__init_array_start__GNU_EH_FRAME_HDR_GLOBAL_OFFSET_TABLE___libc_csu_fini_ITM_deregisterTMCloneTableputs@@GLIBC_2.2.5fread@@GLIBC_2.2.5_edatafclose@@GLIBC_2.2.5fputc@@GLIBC_2.2.5__libc_start_main@@GLIBC_2.2.5__data_start__gmon_start____dso_handle_IO_stdin_used__libc_csu_init__bss_startmainfopen@@GLIBC_2.2.5exit@@GLIBC_2.2.5__TMC_END___ITM_registerTMCloneTable__cxa_finalize@@GLIBC_2.2.5.symtab.strtab.shstrtab.interp.note.ABI-tag.note.gnu.build-id.gnu.hash.dynsym.dynstr.gnu.version.gnu.version_r.rela.dyn.rela.plt.init.plt.got.text.fini.rodata.eh_frame_hdr.eh_frame.init_array.fini_array.dynamic.got.plt.data.bss.comment�#�� 1��$D��No
                                                                                                      00▒VPP�^���o��▒k��z((▒�B��▒��  p�����44   �  �x x <�� ������=�-��?��@�H@HX@X�0X0x0x▒     �6`P9                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat rev | wc
      5      75   16856
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ nano solve.py
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ python solve.py 
picoCTF{r3v3rs36ad73964}
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ cat solve.py
import os
import mmap

def memory_map(filename, access=mmap.ACCESS_READ):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDONLY)
    return mmap.mmap(fd, size, access=access)

with memory_map("rev_this") as bin_file:
    for i in range(8):
        print(chr(bin_file[i]), end = '')
    for i in range(8, 23):
        if (i & 1) == 0:
            print(chr(bin_file[i] - 5), end = '')
        else:
            print(chr(bin_file[i] + 2), end = '')
    print (chr(bin_file[23]))
                                                                                                                                                                       
┌──(kali㉿kali)-[~/…/RetosKali-exam--editar/CarpetaKali-exam1/Retos-Reversing/2019]
└─$ 
```
picoCTF{r3v3rs36ad73964}

## Referencias
- []()