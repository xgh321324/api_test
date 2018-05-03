#coding:utf-8
import json
import time
import datetime
s = {
      "action": "44803",
      "account": "1865998xxxx",
      "uniqueid": "00D7C889-06A0-426E-BAB1-5741A1192038",
      "title": "测试测试",
      "summary": "豆豆豆",
      "message": "12345",
      "msgtype": "25",
      "menuid": "203"
    }
for x in s.items():
    print(x)

t = time.ctime()
print(t)
today = datetime.date.today()
print(today)

