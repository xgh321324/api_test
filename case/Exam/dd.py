#coding:utf-8
from datetime import datetime
import time
import requests

header = {"Date": "Tue, 19 Jun 2018 08:29:51 GMT",
    'User-Agent': 'aliyun-sdk-android/2.3.0/Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G935F Build/MMB29K)',
        "x-oss-security-token":"CAISgQN1q6Ft5B2yfSjIr4j3GO72h+5K+7WuaE7VkmFhOOoY3qLmkDz2IH1OfHlgBeEbvvgwlGtV5vYTlqJ4T55IQ1Dza8J148y6K65xys6T1fau5Jko1bcGcAr6UmxWta2/SuH9S8ynkJ7PD3nPii50x5bjaDymRCbLGJaViJlhHNZ1Ow6jdmhpCctxLAlvo9N4UHzKLqSVLwLNiGjdB1YKwg1nkjFT5KCy3sC74BjTh0GYr+gOvNbVI4O4V8B2IIwdI9Cux75ffK3bzAtN7wRL7K5skJFc/TDOsrP6BEJKsTGHKPbz+N9iJxNiHPdYfZRJt//hj/Z1l/XOnoDssXZ3MPpSTj7USfLTorrNE/j7Mc0iJ/SpeSbX09+PKpjzswQhbDVZFnsTI4F/dy4tUU10EWyEcvP5wj2QPFf/EZri+botzJ94w2/v+de3PFWVS92bq31FYMdsPx95ak5Kgjy6L/9WIhYxaVJoB6qUS4V0aR1Dsq7ytAbZWzZ73tfRXERn13C/GoABP/MVbCx59MoGTKz4rZy+3KEtAYhS3C1s3rDU1peiIFdIpopHjBxR8sZU+6rCIhij6CmzZcOv8/nhe2DOVXJbbRHeREflpj4HNKFisFsZN479hfUlrGO8Ow6TEcTRpRGZApjAPApBmN024k23TMAG/qgHNKbk/uSyVjGQ3khYcAw=",
    "Authorization": "OSS STS.NKBSTBj1kLwEjhdva44e41gMr:LYQ7tXY9FBrTiVgEaYX3lFFxlgo=",
    "Content-Type": "image/jpeg",
    "Content-Length": "128325",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"}
t = str(time.time()).split('.')
t1 = t[0]+t[1]
#print(t1)
sever_url = r'http://rightinhome.oss-cn-hangzhou.aliyuncs.com/TestObjectFiles/TestObjectFiles/'
#print(sever_url)
with open(r'C:\Users\Administrator\Desktop\77.jpg','rb') as f:
    p = requests.put(sever_url+str(t1)+'.jpg',data=f,headers = header)
g = requests.get(sever_url+str(t1)+'.jpg',headers = header)
print(g.text)
