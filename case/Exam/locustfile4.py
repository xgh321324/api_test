#coding:utf-8
import Hash
import time,requests
from locust import HttpLocust,TaskSet,task
import login

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
    #调用登录，获取token
    s = requests.session()
    L = login.LG(s)

    #进入直播课的入参
    t = {
        "token": L.login(),
        "nonce": Hash.get_digit(),
        "timestamp":str(int(time.time())),
        'live_code': 'L2018091268052'
        }
    #入参加密
    t['sign'] = Hash.get_sign(t)

    #进入直播课详情的入参
    de = {
        'token': L.login(),
        'nonce': Hash.get_digit(),
        'timestamp': str(int(time.time())),
        'live_code': 'L2018091268052'

    }
    #入参加密
    de['sign'] = Hash.get_sign(de)

    #task()括号中代表执行压测时的比重
    @task(1)
    def checkin(self):
        u'进入直播课堂'
        r = self.client.post('/v1/live/checkIn',headers = self.header,json=self.t)
        result = r.json()
        assert r.json()['code'] == 200

    @task(1)
    def detail(self):
        u'进入直播课详情'
        r2 = self.client.post('/v1/live/detail',headers = self.header,json=self.de)
        result2 = r2.json()
        assert r2.json()['code'] == 200



class Websiteuser(HttpLocust):
    task_set = User
    #host = 'http://api-live.sunnycare.cc'
    max_wait = 6000
    min_wait = 3000