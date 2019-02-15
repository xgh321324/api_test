#coding:utf-8
from common import Hash
import time,requests
from locust import HttpLocust,TaskSet,task
from locust.contrib.fasthttp import FastHttpLocust


#定义用户行为
class Userbehavior(TaskSet):


    @task(1)
    def get_rec(self):
        #y = {'ci_session':'b66kucj24fr0q35rgqsr6c1afd51dhip'}
        self.client.get('/')


class Websiteuser(FastHttpLocust):
    task_set = Userbehavior
    max_wait = 6000
    min_wait = 3000

if __name__=='__main__':
#导入os模块，os.system方法可以直接在pycharm中该文件中直接运行该py文件
    import os
    os.system('locust -f locust8.py --host=http://www.baidu.com')
