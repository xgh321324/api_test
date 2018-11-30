#coding:utf-8


import datetime
import time
import threading
import requests
from common.login_lanting import auto_login_by_UID
from common.Hash import get_digit,get_sign

class test_login002():
    times = []
    error = []
    def login(self):
        mytest=test_login002
        url = "http://api.lesson.sunnycare.cc/v1/lesson"
        headers = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }

        data = {
            "token":auto_login_by_UID(),
            "lesson_code":"K00098",
            "timestamp":str(int(time.time())),
            "nonce":get_digit()
            }
        data['sign'] = get_sign(data)
        r =requests.post(url=url, headers=headers, json=data)
        print(r.json()['code'])
        ResponseTime = float(r.elapsed.microseconds)/1000
        mytest.times.append(ResponseTime)
        if  r.status_code !=200:
            mytest.error.append("0")

if __name__=="__main__":
    mytest = test_login002()
    threads = []
    starttime = datetime.datetime.now()
    print ("request start time %s " %starttime)
    nub = 5
    ThinkTime = 0.1
    for i in range(1, nub+1):
        t = threading.Thread(target=mytest.login, args='')
        threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        t.setDaemon(True)
        t.start()
    t.join()
    endtime = datetime.datetime.now()
    print ("request end time %s" %endtime)
    time.sleep(0.1)
    AverageTime = "{:.3f}".format(float(sum(mytest.times))/float(len(mytest.times)))
    print("Average Response Time %s ms"%AverageTime)
    usertime = str(endtime - starttime)
    hour = usertime.split(':').pop(0)
    minute = usertime.split(':').pop(1)
    second = usertime.split(':').pop(2)
    totaltime = float(hour)*60*60 + float(minute)*60 + float(second)
    print ("Concurrent processing %s"%nub)
    print ("use total time %s s" %(totaltime-float(nub*ThinkTime)))
    print ("fail request %s" %mytest.error.count("0"))