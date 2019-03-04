#coding:utf-8
import time,requests
from locust import HttpLocust, TaskSet, task
from locust.clients import HttpSession
from locust.contrib.fasthttp import FastHttpLocust
"""
使用FastHttpLocust的话rps会更高，有更高的并发
"""

class User(TaskSet):

    @task(1)
    def lo(self):
        global h
        h = {'token': 'asz120190213chau5c63a9bcfffd7cfcdf5aa03c0000000'}
        with self.client.get('/login/ali-login?os=android&device_token=Aq02lzYuCToe8oK7BXw0R_dBWMqD4iZ5fSL9ssqtR7uH&uuid=358543080625699&channel=应用宝', headers=h, catch_response=True) as response:
            #请求参数中通过catch_response=True来捕获响应数据，然后对响应数据进行校验
            #使用success()/failure()两个方法来标识请求结果的状态
            if response.status_code == 200:
                response.success()
            else:
                response.failure('not 200!')
    @task(1)
    def my(self):
        with self.client.get('/my/my-info', headers=h, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('not 200!')

class Websiteuser(FastHttpLocust):   # or HttpLocust
    task_set = User
    #host = 'http://api-live.sunnycare.cc'
    max_wait = 0
    min_wait = 0


if __name__=='__main__':
    #导入os模块，os.system方法可以直接在pycharm中该文件中直接运行该py文件
    import os
    os.system('locust -f locustfile9.py --host=http://39.105.73.153')

