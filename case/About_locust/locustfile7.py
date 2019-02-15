#coding:utf-8
from common import Hash
import time,requests
from locust import HttpLocust,TaskSet,task
from locust.contrib.fasthttp import FastHttpLocust
from common import login_lanting


#澜渟APP直播接口压测

#定义用户行为
class User(TaskSet):
    #下面是请求头header
    header = {
        'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Content-Type': 'application/json',
        'requestApp': '3',
        'requestclient': '2',
        'versionForApp': '2.0',
        'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
        'Connection': 'keep-alive'
    }
    s = requests.session()
    t = login_lanting.auto_login_by_UID()

    #进入直播入参
    into = {
        'token': t,
        'nonce': Hash.get_digit(),
        'timestamp':str(int(time.time())),
        'live_code': 'L2018112248566'
    }
    #加密
    into['sign'] = Hash.get_sign(into)

    #
    de = {
        'token': t,
        'nonce': Hash.get_digit(),
        'timestamp': str(int(time.time())),
        'live_code': 'L2018121173179'
    }
    #入参加密
    de['sign'] = Hash.get_sign(de)

    @task(1)
    def chekin(self):
        with self.client.post('/v1/live/checkIn',headers = self.header,json=self.into,catch_response=True) as response:
            #请求参数中通过catch_response=True来捕获响应数据，然后对响应数据进行校验
            #使用success()/failure()两个方法来标识请求结果的状态
            if response.status_code == 200:
                response.success()
            else:
                response.failure('not 200!')

    @task(1)
    def detail(self):
        with self.client.post('/v1/live/detail',headers = self.header,json=self.de,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('not 200!')

class Websiteuser(HttpLocust):   # or HttpLocust
    task_set = User
    #host = 'http://api-live.sunnycare.cc'
    max_wait = 6000
    min_wait = 3000


if __name__=='__main__':
    #导入os模块，os.system方法可以直接在pycharm中该文件中直接运行该py文件
    import os
    os.system('locust -f locustfile7.py --host=http://api-live.sunnycare.cc')
