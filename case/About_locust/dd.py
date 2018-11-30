#coding:utf-8
from datetime import datetime
import time
import requests


t = {'name':'南京',"page":'2',"timestamp":"1520222159","nonce":"kspI4VjGTmtaRiYNLyefCruCHOx0da97","token":"jLzS3QryBMObp69UHVYKhoXNqev8gcGW"}
result = sorted(t.items(),key = lambda x:x[0])
print(result)
target2 = ''
for i in result:
    target1 = i[0]+'='+i[1]+'&'
    target2 += target1
print(target2)
print(type(target2))
target3 = target2+'&secret=PSudep6nfrJ9BkEn'
print(target3)