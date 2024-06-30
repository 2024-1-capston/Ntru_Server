import numpy as np #line:1
from NTRU .NTRUencrypt import NTRUencrypt #line:2
from NTRU .NTRUdecrypt import NTRUdecrypt #line:3
from NTRU .NTRUutil import *#line:4
import argparse #line:6
from argparse import RawTextHelpFormatter #line:7
import sys #line:9
from os .path import exists #line:10
prog_description ="""

Based on the original NTRU paper by Hoffstein.

"""#line:17
prog_epilog ="""

References
"""#line:22
parser =argparse .ArgumentParser (prog ="NTRU Encrypt/Decrypt",description =prog_description ,epilog =prog_epilog ,formatter_class =RawTextHelpFormatter )#line:28
parser .add_argument ("-k","--key-name",default ="key",type =str ,help ="The filename of the public and private keys (key_name.pub and (key_name.priv).")#line:30
parser .add_argument ("-G","--Gen",action ="store_true",help ="Generate the public and private key files.\n"+"Default key parameters are the high security parameters from [1].")#line:33
parser .add_argument ("-M","--moderate_sec",action ="store_true",help ="If given with -G flag generate moderate security keys from [1] with N=107, p=3, q=64.")#line:35
parser .add_argument ("-H","--high-sec",action ="store_true",help ="If given with -G flag generate high security keys from [1] with N=167, p=3, q=128.")#line:37
parser .add_argument ("-HH","--highest-sec",action ="store_true",help ="If given with -G flag generate highest security keys from [1] with N=503, p=3, q=256.")#line:39
parser .add_argument ("-N","--N",default =167 ,type =int ,help ="The order of the polynomial ring, default 503.")#line:41
parser .add_argument ("-p","--p",default =3 ,type =int ,help ="The smallest inverse polynomial modulus, default 3.")#line:43
parser .add_argument ("-q","--q",default =128 ,type =int ,help ="The largest inverse polynomial modulus, default 256.")#line:45
parser .add_argument ("-df","--df",default =61 ,type =int ,help ="Polynomial f has df 1's and df -1's, default 61.")#line:47
parser .add_argument ("-dg","--dg",default =20 ,type =int ,help ="Polynomial g has dg 1's and -1's, default 20.")#line:49
parser .add_argument ("-d","--d",default =18 ,type =int ,help ="Random obfuscating polynomial has d 1's and -1's, default 18.")#line:51
parser .add_argument ("-O","--out_file",type =str ,help ="Output file for encrypted/decrypted data/string.")#line:53
parser .add_argument ("-T","--out_in_term",action ="store_true",help ="Output encrypted/decrypted data/string to terminal.")#line:55
parser .add_argument ("-eS","--Enc_string",type =str ,help ="Encrypt the string given as an input.\n"+"Note: String must be given in quotation marks, e.g. \"a string\".\n"+"Note: This always requires a known public key.")#line:59
parser .add_argument ("-eF","--Enc_file",type =str ,help ="Encrypt the string given in this input file.\n"+"Note: This always requires a known public key.")#line:62
parser .add_argument ("-dS","--Dec_string",type =str ,help ="Decrypt the string given as an input.\n"+"Note: String must be given in quotation marks, e.g. \"a string\".\n"+"Note: This always requires a known private key.")#line:66
parser .add_argument ("-dF","--Dec_file",type =str ,help ="Decrypt the string given in this input file.\n"+"Note: This always requires a known private key.")#line:69
args =parser .parse_args ()#line:70
if __name__ =="__main__":#line:74
    if (args .Gen ):#line:78
        N1 =NTRUdecrypt ()#line:80
        if (args .moderate_sec ):#line:82
            N1 .setNpq (N =107 ,p =3 ,q =64 ,df =15 ,dg =12 ,d =5 )#line:83
        elif (args .highest_sec ):#line:84
            N1 .setNpq (N =503 ,p =3 ,q =256 ,df =216 ,dg =72 ,d =55 )#line:85
        else :#line:86
            N1 .setNpq (N =167 ,p =3 ,q =128 ,df =61 ,dg =20 ,d =18 )#line:87
        N1 .genPubPriv (args .key_name )#line:89
    elif (args .Enc_string or args .Enc_file ):#line:93
        if not exists (args .key_name +".pub"):#line:95
            sys .exit ("ERROR : Public key '"+args .key_name +".pub' not found.")#line:96
        if args .Enc_string and args .Enc_file :#line:98
            sys .exit ("ERROR : More than one input to encrypt given.")#line:99
        if not args .out_file and not args .out_in_term :#line:101
            sys .exit ("ERROR : At least one output method must be specified.")#line:102
        E =NTRUencrypt ()#line:104
        E .readPub (args .key_name +".pub")#line:106
        if args .Enc_string :#line:108
            to_encrypt =args .Enc_string #line:109
        elif args .Enc_file :#line:110
            if not exists (args .Enc_file ):#line:112
                sys .exit ("ERROR : Input file '"+args .Enc_file +"' not found.")#line:113
            with open (args .Enc_file ,"r")as f :#line:115
                to_encrypt ="".join (f .readlines ())#line:116
        E .encryptString (to_encrypt )#line:118
        if args .out_in_term :#line:120
            print (E .Me )#line:121
        elif args .out_file :#line:122
            with open (args .out_file ,"w")as f :#line:123
                f .write (E .Me )#line:124
    elif (args .Dec_string or args .Dec_file ):#line:128
        if not exists (args .key_name +".priv"):#line:130
            sys .exit ("ERROR : Public key '"+args .key_name +".priv' not found.")#line:131
        if args .Dec_string and args .Dec_file :#line:133
            sys .exit ("ERROR : More than one input to decrypt given.")#line:134
        if not args .out_file and not args .out_in_term :#line:136
            sys .exit ("ERROR : At least one output method must be specified.")#line:137
        D =NTRUdecrypt ()#line:139
        D .readPriv (args .key_name +".priv")#line:141
        if args .Dec_string :#line:143
            to_decrypt =args .Dec_string #line:144
        elif args .Dec_file :#line:145
            if not exists (args .Dec_file ):#line:146
                sys .exit ("ERROR : Input file '"+args .Dec_file +"' not found.")#line:147
            with open (args .Dec_file ,"r")as f :#line:149
                to_decrypt ="".join (f .readlines ())#line:150
        D .decryptString (to_decrypt )#line:152
        if args .out_in_term :#line:154
            print (D .M )#line:155
        elif args .out_file :#line:156
            with open (args .out_file ,"w")as f :#line:157
                f .write (D .M )
