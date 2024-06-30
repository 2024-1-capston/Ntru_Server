import numpy as np #line:1
from math import log ,gcd #line:2
import random #line:3
import sys #line:4
from sympy import Poly ,symbols ,GF ,invert #line:5
np .set_printoptions (threshold =sys .maxsize )#line:7
def checkPrime (OO000OOO0OO000OOO ):#line:9
    if (OO000OOO0OO000OOO <=1 ):#line:10
        return False #line:11
    elif (OO000OOO0OO000OOO ==2 or OO000OOO0OO000OOO ==3 ):#line:12
        return True #line:13
    else :#line:14
        for OO0OO0OO0O0OOOO00 in range (4 ,OO000OOO0OO000OOO //2 ):#line:15
            if (OO000OOO0OO000OOO %OO0OO0OO0O0OOOO00 ==0 ):#line:16
                return False #line:17
    return True #line:19
def poly_inv (OO000OO00OO0O000O ,OO0OO0000OOO0OOO0 ,O00O0000OO00OOO0O ):#line:23
    OO000O0OOO0OOOO0O =symbols ('x')#line:24
    O00O0OOOOOOOOO00O =Poly (OO0OO0000OOO0OOO0 ,OO000O0OOO0OOOO0O )#line:25
    OO00000OO0O0O0OO0 =len (O00O0OOOOOOOOO00O .all_coeffs ())#line:26
    if checkPrime (O00O0000OO00OOO0O ):#line:27
        try :#line:28
            OO0O0000O0O00OOOO =invert (Poly (OO000OO00OO0O000O ,OO000O0OOO0OOOO0O ).as_expr (),O00O0OOOOOOOOO00O .as_expr (),domain =GF (O00O0000OO00OOO0O ,symmetric =False ))#line:29
        except :#line:30
            return np .array ([])#line:31
    elif log (O00O0000OO00OOO0O ,2 ).is_integer ():#line:32
        try :#line:33
            OO0O0000O0O00OOOO =invert (Poly (OO000OO00OO0O000O ,OO000O0OOO0OOOO0O ).as_expr (),O00O0OOOOOOOOO00O .as_expr (),domain =GF (2 ,symmetric =False ))#line:34
            OOOO0OOOOOO0O0OO0 =int (log (O00O0000OO00OOO0O ,2 ))#line:35
            for O0OO000O000OOO00O in range (1 ,OOOO0OOOOOO0O0OO0 ):#line:36
                OO0O0000O0O00OOOO =((2 *Poly (OO0O0000O0O00OOOO ,OO000O0OOO0OOOO0O )-Poly (OO000OO00OO0O000O ,OO000O0OOO0OOOO0O )*Poly (OO0O0000O0O00OOOO ,OO000O0OOO0OOOO0O )**2 )%O00O0OOOOOOOOO00O ).trunc (O00O0000OO00OOO0O )#line:37
            OO0O0000O0O00OOOO =Poly (OO0O0000O0O00OOOO ,domain =GF (O00O0000OO00OOO0O ,symmetric =False ))#line:38
        except :#line:39
            return np .array ([])#line:40
    else :#line:41
        return np .array ([])#line:42
    OOO0OOOOOO0000OO0 =np .array (Poly ((Poly (OO0O0000O0O00OOOO ,OO000O0OOO0OOOO0O )*Poly (OO000OO00OO0O000O ,OO000O0OOO0OOOO0O ))%O00O0OOOOOOOOO00O ,domain =GF (O00O0000OO00OOO0O ,symmetric =False )).all_coeffs (),dtype =int )#line:45
    if len (OOO0OOOOOO0000OO0 )>1 or OOO0OOOOOO0000OO0 [0 ]!=1 :#line:46
        sys .exit ("ERROR : Error in caclualtion of polynomial inverse")#line:47
    return padArr (np .array (Poly (OO0O0000O0O00OOOO ,OO000O0OOO0OOOO0O ).all_coeffs (),dtype =int ),OO00000OO0O0O0OO0 -1 )#line:49
def padArr (O0O00O0OOOOO0O000 ,O00O0O0O000O0O0O0 ):#line:53
    return np .pad (O0O00O0OOOOO0O000 ,(O00O0O0O000O0O0O0 -len (O0O00O0OOOOO0O000 ),0 ),constant_values =(0 ))#line:54
def genRand10 (O00O0OOO000OO0000 ,OO00O00000OO00O0O ,OO00O000OO0000O0O ):#line:58
    if OO00O00000OO00O0O +OO00O000OO0000O0O >O00O0OOO000OO0000 :#line:59
        sys .exit ("ERROR: Asking for P+M>L.")#line:60
    O0OOOO0O0O00O0OO0 =np .zeros ((O00O0OOO000OO0000 ,),dtype =int )#line:61
    for O000000OO0000OOO0 in range (O00O0OOO000OO0000 ):#line:63
        if O000000OO0000OOO0 <OO00O00000OO00O0O :#line:64
            O0OOOO0O0O00O0OO0 [O000000OO0000OOO0 ]=1 #line:65
        elif O000000OO0000OOO0 <OO00O00000OO00O0O +OO00O000OO0000O0O :#line:66
            O0OOOO0O0O00O0OO0 [O000000OO0000OOO0 ]=-1 #line:67
        else :#line:68
            break #line:69
    np .random .shuffle (O0OOOO0O0O00O0OO0 )#line:71
    return O0OOOO0O0O00O0OO0 #line:72
def arr2str (OOOOO0OOO00O00O00 ):#line:75
    OO0OO00O0000OOOO0 =np .array_str (OOOOO0OOO00O00O00 )#line:76
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("[","",1 )#line:77
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("]","",1 )#line:78
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("\n","")#line:79
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("     "," ")#line:80
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("    "," ")#line:81
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("   "," ")#line:82
    OO0OO00O0000OOOO0 =OO0OO00O0000OOOO0 .replace ("  "," ")#line:83
    return OO0OO00O0000OOOO0 #line:84
def str2bit (OO0O0O0O0O00O00O0 ):#line:87
    return np .array (list (bin (int .from_bytes (str (OO0O0O0O0O00O00O0 ).encode (),"big")))[2 :],dtype =int )#line:88
def bit2str (OOOO0O00O00O0OO00 ):#line:92
    OOOO0OO0O0OO00O00 =padArr (OOOO0O00O00O0OO00 ,len (OOOO0O00O00O0OO00 )+np .mod (len (OOOO0O00O00O0OO00 ),8 ))#line:93
    OOOO0OO0O0OO00O00 =arr2str (OOOO0O00O00O0OO00 )#line:95
    OOOO0OO0O0OO00O00 =OOOO0OO0O0OO00O00 .replace (" ","")#line:96
    OO0O000OOOO0O000O =""#line:98
    for OO0O00O000OO0O0OO in range (len (OOOO0OO0O0OO00O00 )//8 ):#line:99
        if OO0O00O000OO0O0OO ==0 :#line:100
            OOOO0O0OOO00000O0 =OOOO0OO0O0OO00O00 [len (OOOO0OO0O0OO00O00 )-8 :]#line:101
        else :#line:102
            OOOO0O0OOO00000O0 =OOOO0OO0O0OO00O00 [-(OO0O00O000OO0O0OO +1 )*8 :-OO0O00O000OO0O0OO *8 ]#line:103
        OOOO0O0OOO00000O0 =int (OOOO0O0OOO00000O0 ,2 )#line:104
        OO0O000OOOO0O000O =OOOO0O0OOO00000O0 .to_bytes ((OOOO0O0OOO00000O0 .bit_length ()+7 )//8 ,"big").decode ("utf-8",errors ="ignore")+OO0O000OOOO0O000O #line:105
    return OO0O000OOOO0O000O #line:106
