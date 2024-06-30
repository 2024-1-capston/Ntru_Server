import numpy as np #line:1
from math import log ,gcd #line:2
import sys #line:3
from sympy import Poly ,symbols #line:4
from NTRU .NTRUutil import *#line:5
class NTRUdecrypt :#line:7
    def __init__ (OOO00O00OO0OOOO0O ,N =503 ,p =3 ,q =256 ,df =61 ,dg =20 ,d =18 ):#line:9
        OOO00O00OO0OOOO0O .N =N #line:10
        OOO00O00OO0OOOO0O .p =p #line:11
        OOO00O00OO0OOOO0O .q =q #line:12
        OOO00O00OO0OOOO0O .df =df #line:14
        OOO00O00OO0OOOO0O .dg =dg #line:15
        OOO00O00OO0OOOO0O .dr =d #line:16
        OOO00O00OO0OOOO0O .f =np .zeros ((OOO00O00OO0OOOO0O .N ,),dtype =int )#line:18
        OOO00O00OO0OOOO0O .fp =np .zeros ((OOO00O00OO0OOOO0O .N ,),dtype =int )#line:19
        OOO00O00OO0OOOO0O .fq =np .zeros ((OOO00O00OO0OOOO0O .N ,),dtype =int )#line:20
        OOO00O00OO0OOOO0O .g =np .zeros ((OOO00O00OO0OOOO0O .N ,),dtype =int )#line:21
        OOO00O00OO0OOOO0O .h =np .zeros ((OOO00O00OO0OOOO0O .N ,),dtype =int )#line:22
        OOO00O00OO0OOOO0O .I =np .zeros ((OOO00O00OO0OOOO0O .N +1 ,),dtype =int )#line:24
        OOO00O00OO0OOOO0O .I [OOO00O00OO0OOOO0O .N ]=-1 #line:25
        OOO00O00OO0OOOO0O .I [0 ]=1 #line:26
        OOO00O00OO0OOOO0O .M =None #line:28
    def setNpq (O0OO0OOO0O0O00O00 ,N =None ,p =None ,q =None ,df =None ,dg =None ,d =None ):#line:31
        if N is not None :#line:34
            if (not checkPrime (N )):#line:35
                sys .exit ("\n\nERROR: Input value of N not prime\n\n")#line:36
            else :#line:37
                if df is None :#line:38
                    if 2 *O0OO0OOO0O0O00O00 .df >N :#line:39
                        sys .exit ("\n\nERROR: Input N too small compared to default df "+str (O0OO0OOO0O0O00O00 .df )+"\n\n")#line:40
                if dg is None :#line:41
                    if 2 *O0OO0OOO0O0O00O00 .dg >N :#line:42
                        sys .exit ("\n\nERROR: Input N too small compared to default dg "+str (O0OO0OOO0O0O00O00 .dg )+"\n\n")#line:43
                if d is None :#line:44
                    if 2 *O0OO0OOO0O0O00O00 .dr >N :#line:45
                        sys .exit ("\n\nERROR: Input N too small compared to default dr "+str (O0OO0OOO0O0O00O00 .dr )+"\n\n")#line:46
                O0OO0OOO0O0O00O00 .N =N #line:47
                O0OO0OOO0O0O00O00 .f =np .zeros ((O0OO0OOO0O0O00O00 .N ,),dtype =int )#line:48
                O0OO0OOO0O0O00O00 .fp =np .zeros ((O0OO0OOO0O0O00O00 .N ,),dtype =int )#line:49
                O0OO0OOO0O0O00O00 .fq =np .zeros ((O0OO0OOO0O0O00O00 .N ,),dtype =int )#line:50
                O0OO0OOO0O0O00O00 .g =np .zeros ((O0OO0OOO0O0O00O00 .N ,),dtype =int )#line:51
                O0OO0OOO0O0O00O00 .h =np .zeros ((O0OO0OOO0O0O00O00 .N ,),dtype =int )#line:52
                O0OO0OOO0O0O00O00 .I =np .zeros ((O0OO0OOO0O0O00O00 .N +1 ,),dtype =int )#line:53
                O0OO0OOO0O0O00O00 .I [O0OO0OOO0O0O00O00 .N ]=-1 #line:54
                O0OO0OOO0O0O00O00 .I [0 ]=1 #line:55
        if (p is None and q is not None )or (p is not None and q is None ):#line:57
            sys .exit ("\n\nError: Can only set p and q together, not individually")#line:58
        elif (p is not None )and (q is not None ):#line:59
            if ((8 *p )>q ):#line:60
                sys .exit ("\n\nERROR: We require 8p <= q\n\n")#line:61
            else :#line:62
                if (gcd (p ,q )!=1 ):#line:63
                    sys .exit ("\n\nERROR: Input p and q are not coprime\n\n")#line:64
                else :#line:65
                    O0OO0OOO0O0O00O00 .p =p #line:66
                    O0OO0OOO0O0O00O00 .q =q #line:67
        if df is not None :#line:69
            if 2 *df >O0OO0OOO0O0O00O00 .N :#line:70
                sys .exit ("\n\nERROR: Input df such that 2*df>N\n\n")#line:71
            else :#line:72
                O0OO0OOO0O0O00O00 .df =df #line:73
        if dg is not None :#line:75
            if 2 *dg >O0OO0OOO0O0O00O00 .N :#line:76
                sys .exit ("\n\nERROR: Input dg such that 2*dg>N\n\n")#line:77
            else :#line:78
                O0OO0OOO0O0O00O00 .dg =dg #line:79
        if d is not None :#line:81
            if 2 *d >O0OO0OOO0O0O00O00 .N :#line:82
                sys .exit ("\n\nERROR: Input dr such that 2*dr>N\n\n")#line:83
            else :#line:84
                O0OO0OOO0O0O00O00 .dr =d #line:85
    def invf (OO0OOOO0OO000O0OO ):#line:88
        OOOO00OOOOO000OO0 =poly_inv (OO0OOOO0OO000O0OO .f ,OO0OOOO0OO000O0OO .I ,OO0OOOO0OO000O0OO .p )#line:89
        OO00000OOO0000000 =poly_inv (OO0OOOO0OO000O0OO .f ,OO0OOOO0OO000O0OO .I ,OO0OOOO0OO000O0OO .q )#line:90
        if len (OOOO00OOOOO000OO0 )>0 and len (OO00000OOO0000000 )>0 :#line:91
            OO0OOOO0OO000O0OO .fp =np .array (OOOO00OOOOO000OO0 )#line:92
            OO0OOOO0OO000O0OO .fq =np .array (OO00000OOO0000000 )#line:93
            if len (OO0OOOO0OO000O0OO .fp )<OO0OOOO0OO000O0OO .N :#line:94
                OO0OOOO0OO000O0OO .fp =np .concatenate ([np .zeros (OO0OOOO0OO000O0OO .N -len (OO0OOOO0OO000O0OO .fp ),dtype =int ),OO0OOOO0OO000O0OO .fp ])#line:95
            if len (OO0OOOO0OO000O0OO .fq )<OO0OOOO0OO000O0OO .N :#line:96
                OO0OOOO0OO000O0OO .fq =np .concatenate ([np .zeros (OO0OOOO0OO000O0OO .N -len (OO0OOOO0OO000O0OO .fq ),dtype =int ),OO0OOOO0OO000O0OO .fq ])#line:97
            return True #line:98
        else :#line:99
            return False #line:100
    def genfg (OO000O00O0OO0OO00 ):#line:103
        OO0O000OOO0OOO000 =100 #line:104
        OO000O00O0OO0OO00 .g =genRand10 (OO000O00O0OO0OO00 .N ,OO000O00O0OO0OO00 .dg ,OO000O00O0OO0OO00 .dg )#line:105
        for O0OO0O0OO0O0OOOOO in range (OO0O000OOO0OOO000 ):#line:106
            OO000O00O0OO0OO00 .f =genRand10 (OO000O00O0OO0OO00 .N ,OO000O00O0OO0OO00 .df ,OO000O00O0OO0OO00 .df -1 )#line:107
            OOOOO00OOOO0O0OO0 =OO000O00O0OO0OO00 .invf ()#line:108
            if OOOOO00OOOO0O0OO0 ==True :#line:109
                break #line:110
            elif O0OO0O0OO0O0OOOOO ==OO0O000OOO0OOO000 -1 :#line:111
                sys .exit ("Cannot generate required inverses of f")#line:112
    def genh (OOOO000OOOO0O0OOO ):#line:115
        O0000O0O00O0OO00O =symbols ('x')#line:116
        OOOO000OOOO0O0OOO .h =Poly ((Poly (OOOO000OOOO0O0OOO .p *OOOO000OOOO0O0OOO .fq ,O0000O0O00O0OO00O ).trunc (OOOO000OOOO0O0OOO .q )*Poly (OOOO000OOOO0O0OOO .g ,O0000O0O00O0OO00O )).trunc (OOOO000OOOO0O0OOO .q )%Poly (OOOO000OOOO0O0OOO .I ,O0000O0O00O0OO00O )).all_coeffs ()#line:118
    def writePub (O00OO000000000OOO ,filename ="key"):#line:121
        OOO0O000OOOO00O0O ="p ::: "+str (O00OO000000000OOO .p )+"\nq ::: "+str (O00OO000000000OOO .q )+"\nN ::: "+str (O00OO000000000OOO .N )+"\nd ::: "+str (O00OO000000000OOO .dr )+"\nh :::"#line:123
        np .savetxt (filename +".pub",O00OO000000000OOO .h ,newline =" ",header =OOO0O000OOOO00O0O ,fmt ="%s")#line:124
    def readPub (OOO000000OO00OO0O ,filename ="key.pub"):#line:127
        with open (filename ,"r")as OOO0000O00O000OOO :#line:128
            OOO000000OO00OO0O .p =int (OOO0000O00O000OOO .readline ().split (" ")[-1 ])#line:129
            OOO000000OO00OO0O .q =int (OOO0000O00O000OOO .readline ().split (" ")[-1 ])#line:130
            OOO000000OO00OO0O .N =int (OOO0000O00O000OOO .readline ().split (" ")[-1 ])#line:131
            OOO000000OO00OO0O .dr =int (OOO0000O00O000OOO .readline ().split (" ")[-1 ])#line:132
            OOO000000OO00OO0O .h =np .array (OOO0000O00O000OOO .readline ().split (" ")[3 :-1 ],dtype =int )#line:133
        OOO000000OO00OO0O .I =np .zeros ((OOO000000OO00OO0O .N +1 ,),dtype =int )#line:134
        OOO000000OO00OO0O .I [OOO000000OO00OO0O .N ]=-1 #line:135
        OOO000000OO00OO0O .I [0 ]=1 #line:136
    def writePriv (O0OO0OO000OOO0O0O ,filename ="key"):#line:138
        O0OO00O0O0000000O ="p ::: "+str (O0OO0OO000OOO0O0O .p )+"\nq ::: "+str (O0OO0OO000OOO0O0O .q )+"\nN ::: "+str (O0OO0OO000OOO0O0O .N )+"\ndf ::: "+str (O0OO0OO000OOO0O0O .df )+"\ndg ::: "+str (O0OO0OO000OOO0O0O .dg )+"\nd ::: "+str (O0OO0OO000OOO0O0O .dr )+"\nf/fp/fq/g :::"#line:141
        np .savetxt (filename +".priv",(O0OO0OO000OOO0O0O .f ,O0OO0OO000OOO0O0O .fp ,O0OO0OO000OOO0O0O .fq ,O0OO0OO000OOO0O0O .g ),header =O0OO00O0O0000000O ,newline ="\n",fmt ="%s")#line:142
    def readPriv (O0OO0O0OOO0O00OO0 ,filename ="key.priv"):#line:144
        with open (filename ,"r")as O0OO0OOO0O00OOOO0 :#line:145
            O0OO0O0OOO0O00OO0 .p =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:146
            O0OO0O0OOO0O00OO0 .q =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:147
            O0OO0O0OOO0O00OO0 .N =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:148
            O0OO0O0OOO0O00OO0 .df =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:149
            O0OO0O0OOO0O00OO0 .dg =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:150
            O0OO0O0OOO0O00OO0 .dr =int (O0OO0OOO0O00OOOO0 .readline ().split (" ")[-1 ])#line:151
            OO00O000OO00O000O =O0OO0OOO0O00OOOO0 .readline ()#line:152
            O0OO0O0OOO0O00OO0 .f =np .array (O0OO0OOO0O00OOOO0 .readline ().split (" "),dtype =int )#line:153
            O0OO0O0OOO0O00OO0 .fp =np .array (O0OO0OOO0O00OOOO0 .readline ().split (" "),dtype =int )#line:154
            O0OO0O0OOO0O00OO0 .fq =np .array (O0OO0OOO0O00OOOO0 .readline ().split (" "),dtype =int )#line:155
            O0OO0O0OOO0O00OO0 .g =np .array (O0OO0OOO0O00OOOO0 .readline ().split (" "),dtype =int )#line:156
        O0OO0O0OOO0O00OO0 .I =np .zeros ((O0OO0O0OOO0O00OO0 .N +1 ,),dtype =int )#line:157
        O0OO0O0OOO0O00OO0 .I [O0OO0O0OOO0O00OO0 .N ]=-1 #line:158
        O0OO0O0OOO0O00OO0 .I [0 ]=1 #line:159
    def genPubPriv (O0O000O0OOOOOOOO0 ,keyfileName ="key"):#line:162
        O0O000O0OOOOOOOO0 .genfg ()#line:163
        O0O000O0OOOOOOOO0 .genh ()#line:164
        O0O000O0OOOOOOOO0 .writePub (keyfileName )#line:165
        O0O000O0OOOOOOOO0 .writePriv (keyfileName )#line:166
    def decrypt (OO000OO00O00OOOOO ,OOOOO00000OO00O00 ):#line:169
        if len (OOOOO00000OO00O00 )>OO000OO00O00OOOOO .N :#line:170
            sys .exit ("Encrypted message has degree > N")#line:171
        O0O00OO00O0OO0O00 =symbols ('x')#line:172
        O0000OOO00O0OO0O0 =((Poly (OO000OO00O00OOOOO .f ,O0O00OO00O0OO0O00 )*Poly (OOOOO00000OO00O00 ,O0O00OO00O0OO0O00 ))%Poly (OO000OO00O00OOOOO .I ,O0O00OO00O0OO0O00 )).trunc (OO000OO00O00OOOOO .q )#line:173
        OO0O0O000OO0O0000 =O0000OOO00O0OO0O0 .trunc (OO000OO00O00OOOOO .p )#line:174
        OOOO0O00OO00O0000 =((Poly (OO000OO00O00OOOOO .fp ,O0O00OO00O0OO0O00 )*OO0O0O000OO0O0000 )%Poly (OO000OO00O00OOOOO .I ,O0O00OO00O0OO0O00 )).trunc (OO000OO00O00OOOOO .p )#line:175
        return np .array (OOOO0O00OO00O0000 .all_coeffs (),dtype =int )#line:177
    def decryptString (O00O00OO00OOO0000 ,O0OO0O0000000O0OO ):#line:180
        OO0000000OO0OOO00 =np .fromstring (O0OO0O0000000O0OO ,dtype =int ,sep =' ')#line:181
        if np .mod (len (OO0000000OO0OOO00 ),O00O00OO00OOO0000 .N )!=0 :#line:182
            sys .exit ("\n\nERROR : Input decrypt string is not integer multiple of N\n\n")#line:183
        OOO0O00O0000OO00O =np .array ([],dtype =int )#line:185
        for O00OO000O00OOOO00 in range (len (OO0000000OO0OOO00 )//O00O00OO00OOO0000 .N ):#line:186
            OOO0O00O0000OO00O =np .concatenate ((OOO0O00O0000OO00O ,padArr (O00O00OO00OOO0000 .decrypt (OO0000000OO0OOO00 [O00OO000O00OOOO00 *O00O00OO00OOO0000 .N :(O00OO000O00OOOO00 +1 )*O00O00OO00OOO0000 .N ]),O00O00OO00OOO0000 .N )))#line:187
        O00O00OO00OOO0000 .M =bit2str (OOO0O00O0000OO00O )
