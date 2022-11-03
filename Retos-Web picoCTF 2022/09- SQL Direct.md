# SQL Direct
## Objetivo
Connect to this PostgreSQL server and find the flag!
**This challenge launches an instance on demand.**

## Soluciòn
Lo primero que debemos hacer es iniciar la instancia con el botòn que dice *Launch Instance*.
Luego en la descripciòn de este reto nos darà un comando para poder acceder a la base de datos, luego nos pediràn la contraseña, la cual se encuentra abajo del comando que nos da la descpciòn. 
Usamos `\d` para enlistar las tablas que hay en la base de datos, luego usamos `select * from flags;` para listar el contenido de la tabla con nombre flags, y asì obtenemos la flag de este reto.
```shell
┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ psql -h saturn.picoctf.net -p 65078 -U postgres pico
Password for user postgres: 
psql (14.4 (Debian 14.4-1+b1), server 14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

pico=# \d
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags | table | postgres
(1 row)

pico=# select * from flags;
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)

pico=# exit

┌──(kali㉿kali)-[~/Desktop/CarpetaCompartida.Windows]
└─$ 

```
picoCTF{L3arN_S0m3_5qL_t0d4Y_21c94904}

## Referencias
- []()