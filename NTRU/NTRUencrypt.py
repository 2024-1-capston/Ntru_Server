import numpy as np #line:1
import sys #line:2
from sympy import Poly ,symbols #line:3
from NTRU .NTRUutil import *#line:4
class NTRUencrypt :#line:6
    ""#line:9
    def __init__ (OO0O00O0OOO00O0O0 ,N =503 ,p =3 ,q =256 ,d =18 ):#line:11
        ""#line:14
        OO0O00O0OOO00O0O0 .N =N #line:15
        OO0O00O0OOO00O0O0 .p =p #line:16
        OO0O00O0OOO00O0O0 .q =q #line:17
        OO0O00O0OOO00O0O0 .dr =d #line:19
        OO0O00O0OOO00O0O0 .g =np .zeros ((OO0O00O0OOO00O0O0 .N ,),dtype =int )#line:21
        OO0O00O0OOO00O0O0 .h =np .zeros ((OO0O00O0OOO00O0O0 .N ,),dtype =int )#line:22
        OO0O00O0OOO00O0O0 .r =np .zeros ((OO0O00O0OOO00O0O0 .N ,),dtype =int )#line:23
        OO0O00O0OOO00O0O0 .genr ()#line:24
        OO0O00O0OOO00O0O0 .m =np .zeros ((OO0O00O0OOO00O0O0 .N ,),dtype =int )#line:25
        OO0O00O0OOO00O0O0 .e =np .zeros ((OO0O00O0OOO00O0O0 .N ,),dtype =int )#line:26
        OO0O00O0OOO00O0O0 .I =np .zeros ((OO0O00O0OOO00O0O0 .N +1 ,),dtype =int )#line:28
        OO0O00O0OOO00O0O0 .I [OO0O00O0OOO00O0O0 .N ]=-1 #line:29
        OO0O00O0OOO00O0O0 .I [0 ]=1 #line:30
        OO0O00O0OOO00O0O0 .readKey =False #line:32
        OO0O00O0OOO00O0O0 .Me =None #line:34
    def readPub (O0O00000O00OO00O0 ,filename ="key.pub"):#line:37
        with open (filename ,"r")as OO0OO0O0O0O0000O0 :#line:38
            O0O00000O00OO00O0 .p =int (OO0OO0O0O0O0000O0 .readline ().split (" ")[-1 ])#line:39
            O0O00000O00OO00O0 .q =int (OO0OO0O0O0O0000O0 .readline ().split (" ")[-1 ])#line:40
            O0O00000O00OO00O0 .N =int (OO0OO0O0O0O0000O0 .readline ().split (" ")[-1 ])#line:41
            O0O00000O00OO00O0 .dr =int (OO0OO0O0O0O0000O0 .readline ().split (" ")[-1 ])#line:42
            O0O00000O00OO00O0 .h =np .array (OO0OO0O0O0O0000O0 .readline ().split (" ")[3 :-1 ],dtype =int )#line:43
        O0O00000O00OO00O0 .I =np .zeros ((O0O00000O00OO00O0 .N +1 ,),dtype =int )#line:44
        O0O00000O00OO00O0 .I [O0O00000O00OO00O0 .N ]=-1 #line:45
        O0O00000O00OO00O0 .I [0 ]=1 #line:46
        O0O00000O00OO00O0 .genr ()#line:47
        O0O00000O00OO00O0 .readKey =True #line:48
    def genr (O0OO000O0O0000OO0 ):#line:51
        O0OO000O0O0000OO0 .r =genRand10 (O0OO000O0O0000OO0 .N ,O0OO000O0O0000OO0 .dr ,O0OO000O0O0000OO0 .dr )#line:52
    def setM (O0OO0OO00O00000OO ,O0OO0O000000000OO ):#line:55
        if O0OO0OO00O00000OO .readKey ==False :#line:56
            sys .exit ("ERROR : Public key not read before setting message")#line:57
        if len (O0OO0O000000000OO )>O0OO0OO00O00000OO .N :#line:58
            sys .exit ("ERROR : Message length longer than degree of polynomial ring ideal")#line:59
        for O0OOO0O00O00OO0OO in range (len (O0OO0O000000000OO )):#line:60
            if O0OO0O000000000OO [O0OOO0O00O00OO0OO ]<-O0OO0OO00O00000OO .p /2 or O0OO0O000000000OO [O0OOO0O00O00OO0OO ]>O0OO0OO00O00000OO .p /2 :#line:61
                sys .exit ("ERROR : Elements of message must be in [-p/2,p/2]")#line:62
        O0OO0OO00O00000OO .m =padArr (O0OO0O000000000OO ,O0OO0OO00O00000OO .N )#line:63
    def encrypt (O0O00OOO0O00OO0OO ,m =None ):#line:66
        if O0O00OOO0O00OO0OO .readKey ==False :#line:67
            sys .exit ("Error : Not read the public key file, so cannot encrypt")#line:68
        if m is not None :#line:69
            if len (m )>O0O00OOO0O00OO0OO .N :#line:70
                sys .exit ("\n\nERROR: Polynomial message of degree >= N")#line:71
            O0O00OOO0O00OO0OO .m =m #line:72
        OOOO0OOO0O00O0O0O =symbols ('x')#line:73
        O0O00OOO0O00OO0OO .e =np .array (((((Poly (O0O00OOO0O00OO0OO .r ,OOOO0OOO0O00O0O0O )*Poly (O0O00OOO0O00OO0OO .h ,OOOO0OOO0O00O0O0O )).trunc (O0O00OOO0O00OO0OO .q ))+Poly (O0O00OOO0O00OO0OO .m ,OOOO0OOO0O00O0O0O ))%Poly (O0O00OOO0O00OO0OO .I ,OOOO0OOO0O00O0O0O )).trunc (O0O00OOO0O00OO0OO .q ).all_coeffs (),dtype =int )#line:75
        O0O00OOO0O00OO0OO .e =padArr (O0O00OOO0O00OO0OO .e ,O0O00OOO0O00OO0OO .N )#line:76
    def encryptString (O000000O0OO0OO000 ,O0O0O0O0O0OO00OOO ):#line:79
        if O000000O0OO0OO000 .readKey ==False :#line:80
            sys .exit ("Error : Not read the public key file, so cannot encrypt")#line:81
        OOOO0OO0OO0OOOOOO =str2bit (O0O0O0O0O0OO00OOO )#line:83
        OOOO0OO0OO0OOOOOO =padArr (OOOO0OO0OO0OOOOOO ,len (OOOO0OO0OO0OOOOOO )-np .mod (len (OOOO0OO0OO0OOOOOO ),O000000O0OO0OO000 .N )+O000000O0OO0OO000 .N )#line:84
        O000000O0OO0OO000 .Me =""#line:86
        for O0OOOO0O0O0OO00O0 in range (len (OOOO0OO0OO0OOOOOO )//O000000O0OO0OO000 .N ):#line:88
            O000000O0OO0OO000 .genr ()#line:89
            O000000O0OO0OO000 .setM (OOOO0OO0OO0OOOOOO [O0OOOO0O0O0OO00O0 *O000000O0OO0OO000 .N :(O0OOOO0O0O0OO00O0 +1 )*O000000O0OO0OO000 .N ])#line:90
            O000000O0OO0OO000 .encrypt ()#line:91
            O000000O0OO0OO000 .Me =O000000O0OO0OO000 .Me +arr2str (O000000O0OO0OO000 .e )+" "#line:92
