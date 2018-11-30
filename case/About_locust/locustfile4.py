#coding:utf-8
from common import Hash
import time,requests
from locust import HttpLocust,TaskSet,task
from common import login

#澜渟医生APP直播接口压测

#定义用户行为
class User(TaskSet):
    #下面是请求头header
    header = {
            'User-Agent': 'okhttp/3.8.1',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Content-Type': 'application/json',
            'requestApp': '3',
            'requestclient': '2',
            'versionForApp': '2.5.1',
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
        'live_code': 'L2018112298710'
        }
    #入参加密
    t['sign'] = Hash.get_sign(t)

    #进入直播课详情的入参
    de = {
        'token': L.login(),
        'nonce': Hash.get_digit(),
        'timestamp': str(int(time.time())),
        'live_code': 'L2018112298710'

    }
    #入参加密
    de['sign'] = Hash.get_sign(de)

    #获取嘉宾主持人入参
    member = {
        'token': L.login(),
        'nonce': Hash.get_digit(),
        'timestamp': str(time.time()),
        'live_code': 'L2018112298710'
    }
    #入参加密
    member['sign'] = Hash.get_sign(member)

    #获取图片
    image = {
        'token': L.login(),
        'nonce': Hash.get_digit(),
        'timestamp': str(time.time()),
        'live_code': 'L2018112298710'
    }
    #加密
    image = Hash.get_sign(image)


    #task()括号中代表执行压测时的比重
    @task(1)
    def checkin(self):
        u'进入直播课堂'
        with self.client.post('/v1/live/checkIn',headers = self.header,json=self.t,catch_response=True) as response:
            #请求参数中通过catch_response=True来捕获响应数据，然后对响应数据进行校验
            #使用success()/failure()两个方法来标识请求结果的状态
            if response.status_code == 200:
                response.success()
            else:
                response.failure()

    @task(1)
    def detail(self):
        u'进入直播课详情'
        with self.client.post('/v1/live/detail',headers = self.header,json=self.de,catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure()

    @task(1)
    def member_teach(self):
        u'获取嘉宾主持人'
        with self.client.post('/v1/member/teach',headers = self.header,json= self.member,catch_response=True) as response:

            if response.status_code == 200:
                response.success()
            else:
                response.failure()

    @task(1)
    def get_iamge(self):
        with self.client.post('/v1/matter/imageList',headers = self.header,json = self.image,catch_response=True) as response:
             if response.status_code == 200:
                 response.success()
             else:
                 response.failure()

class Websiteuser(HttpLocust):
    task_set = User
    #host = 'http://api-live.sunnycare.cc'
    max_wait = 6000
    min_wait = 3000

if __name__=='__main__':
    #导入os模块，os.system方法可以直接在pycharm中该文件中直接运行该py文件
    import os
    os.system('locust -f locustfile4.py --host=http://api-live.sunnycare.cc')

