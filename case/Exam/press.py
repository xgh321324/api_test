#coding:utf-8
import threading
import requests
import time
from datetime import datetime
from common.login_lanting import auto_login_by_UID
from common.Hash import get_digit,get_sign
#这是自己写的一个进入课程主页的接口的压力测试
#利用多线程
#
class Stress():
    def __init__(self):
        self.url = 'http://api.lesson.sunnycare.cc/v1/lesson'
        self.t = auto_login_by_UID()
        self.s = requests.session()
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }

    def post(self):
        self.json_data = {
            "token":self.t,
            "lesson_code":"K00098",
            "timestamp":str(int(time.time())),
            "nonce":get_digit()
            }
        self.json_data['sign'] = get_sign(self.json_data)
        try:
            r = self.s.post(url=self.url ,headers = self.header,json=self.json_data)
            print(r.json())
        except Exception as e:
            print(e)
#实例化
def Login():
    login = Stress()
    return login.post()


if __name__ == '__main__':
    try:
        i = 0
        #创建线程组
        tasks = []
        #开启线程数目
        task_number = 300
        print('测试启动')
        time1 = datetime.now()
        print('开始时间为：%s' % time1)
        while i < task_number:
            t = threading.Thread(target=Login())
            tasks.append(t)
            t.start()
            i += 1
        time2 = datetime.now()
        print('结束时间为：%s' % time1)
        times = time2 - time1
        print('平均响应时间：%s' % (times/task_number))
    except Exception as e:
        print(e)



