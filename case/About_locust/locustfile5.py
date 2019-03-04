#coding:utf-8
#import Hash
import time,requests
from locust import HttpLocust,TaskSet,task
#import login

#定义用户行为
class User(TaskSet):
    #下面是请求头header
    header = {
            'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Type': 'application/json',
            'requestApp': '3',
            'requestclient': '2',
            'versionForApp': '2.4.0',
            'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
            'Connection': 'keep-alive'
        }
    #登录入参

    denglu = {
            "username":"15651797525",
            "password":"123456",
            "loginDevice":"2",
            "loginCity":"南京市"
        }
    @task
    def test_login(self):
        u'登录'
        r = self.client.post('/API/V1/DoctorLoginForToken/loginByUsername',headers = self.header,json=self.denglu)
        re = r.json()
        assert r.json()['code'] == 200

class Websiteuser(HttpLocust):
    u'WebsiteUser()类用于设置性能测试'
    task_set = User
    #host = 'http://api.rih.sunnycare.cc'
    max_wait = 0
    min_wait = 0

if __name__=='__main__':
    import os
    os.system("locust -f locustfile5.py --host=http://api.rih.sunnycare.cc")