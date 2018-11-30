#coding:utf-8
from locust import HttpLocust,TaskSet,task
import time
import login_lanting
import Hash
'''测试发表渟说接口的性能'''
#定义用户行为
class User(TaskSet):
    #下面是请求头header
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.0.0.13547',
                   'Accept-Encoding': 'gzip',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Content-Type': 'application/json',
                   'requestApp': '2',
                   'requestclient': '2',
                   'versionForApp': '4.3.1',
                   'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                   'Connection': 'keep-alive'
                   }
    #发布渟说的入参
    t = {
        "token": login_lanting.auto_login_by_UID(),
        "text": '嘻嘻嘻嘻嘻嘻',
        "nonce": Hash.get_digit(),
        "timestamp":str(int(time.time()))
        }
    t['sign'] = Hash.get_sign(t)
    #加入圈子的入参
    d = {
        "token":login_lanting.auto_login_by_UID(),
        "group_id":"G00006",
        "timestamp":str(int(time.time())),
        "nonce":Hash.get_digit()
       }
    d['sign'] = Hash.get_sign(d)

    #task()括号中代表执行压测时的比重
    @task(1)
    def post_word(self):
        u'发布文字渟说'
        r = self.client.post('/v1/feed/add',headers = self.header,json=self.t)
        result = r.json()
        #assert r.json()['code'] == 200


    @task(1)
    def post_artical(self):
        u'发布文章接口'
        r = self.client.post('/v1/group/add',headers = self.header,json= self.d)
        result = r.json()



class Websiteuser(HttpLocust):
    task_set = User
    #host = 'http://api.feed.sunnycare.cc'
    max_wait = 6000
    min_wait = 1000
