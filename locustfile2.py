#coding:utf-8
from locust import HttpLocust,TaskSet,task
import time
import common.Hash
import common.login_lanting
'''测试课程详情接口的性能'''
#定义用户行为
class Get_lesson(TaskSet):
    #下面是请求接口所要用到的东西，包括请求参数t，请求头header
    t = {"lesson_code":"K00101",
             "timestamp":str(int(time.time())),
             "token":login_lanting.auto_login_by_UID(),
             "nonce": Hash.get_digit()
             }
    t['sign'] = Hash.get_sign(t)

    header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-Hans-CN;q=1',
                   'Content-Type': 'application/json',
                   'requestApp': '3',
                   'requestclient': '2',
                   'versionForApp': '2.0',
                   'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                   'Connection': 'keep-alive'
                   }
    #task()括号中代表执行压测时的比重
    @task(1)
    def get_lesson(self):
        url = '/v1/lesson'
        r = self.client.post('/v1/lesson',headers = self.header,json=self.t)
        result = r.json()
        assert r.json()['code'] == 200
class Websiteuser(HttpLocust):
    task_set = Get_lesson
    max_wait = 6000
    min_wait = 3000

