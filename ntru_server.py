from flask import Flask ,request ,jsonify #line:1
import subprocess #line:2
import base64 #line:3
app =Flask (__name__ )#line:5
@app .route ('/enc',methods =['POST'])#line:7
def encrypt ():#line:8
    OOOOOO0O0OO0O0OOO =request .json #line:9
    OOOO0O0OOO00OOO00 =OOOOOO0O0OO0O0OOO .get ('text','')#line:10
    OOO0OOO0OOOOOO0OO =base64 .b64encode (OOOO0O0OOO00OOO00 .encode ()).decode ()#line:12
    O00O00OOOO00OOOOO =['python3','NTRU.py','-k','NTRU_key','-eS',OOO0OOO0OOOOOO0OO ,'-T']#line:14
    try :#line:16
        O000OO00OOO00OOOO =subprocess .run (O00O00OOOO00OOOOO ,check =True ,stdout =subprocess .PIPE )#line:17
        OO00O0O0OOOOO00O0 =O000OO00OOO00OOOO .stdout .decode ('utf-8')#line:18
        return jsonify ({'result':OO00O0O0OOOOO00O0 [:-1 ]})#line:19
    except subprocess .CalledProcessError as OO0OO00OOO0OOO0OO :#line:20
        return jsonify ({'error':f'ntru.py 실행 중 오류 발생: {OO0OO00OOO0OOO0OO}'})#line:21
@app .route ('/dec',methods =['POST'])#line:23
def decrypt ():#line:24
    O000O000OOOO0000O =request .json #line:25
    OOOO0OO0O00O0O0OO =O000O000OOOO0000O .get ('text','')#line:26
    OOOO0O0000O00000O =['python3','NTRU.py','-k','NTRU_key','-T','-dS',OOOO0OO0O00O0O0OO ,]#line:28
    try :#line:30
        OO00O00000000OOOO =subprocess .run (OOOO0O0000O00000O ,check =True ,stdout =subprocess .PIPE )#line:31
        O0O000000OO0O0OO0 =OO00O00000000OOOO .stdout .decode ('utf-8')#line:32
        OO0OOOOOO000OOOOO =base64 .b64decode (O0O000000OO0O0OO0 .encode ()).decode ()#line:34
        return jsonify ({'result':OO0OOOOOO000OOOOO })#line:36
    except subprocess .CalledProcessError as O0O00O00OO0O00O00 :#line:37
        return jsonify ({'error':f'ntru.py 실행 중 오류 발생: {O0O00O00OO0O00O00}'})#line:38
if __name__ =='__main__':#line:40
    app .run (host ='0.0.0.0')
