#coding:utf-8
import locust
import time
from common.Hash import get_digit,get_sign
from locust import HttpLocust,TaskSet,task


'''测试课程详情接口的性能'''

#定义用户行为
class Userbehavior(TaskSet):


    def login(self):

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
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'
        json_data = {"UID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB"}
        r = self.client.post(url,headers = header,json = json_data)
        x = r.json()['data']['Token']
        try:
            with open(r'C:\Users\Administrator\Desktop\token.txt','w') as f:
                f.write(x)
        except Exception as e:
            print(e)



    @task(2)
    def get_lesson(self):
        with open(r'C:\Users\Administrator\Desktop\token.txt','r') as f:
            t = {"lesson_code":"K00011",
                 "timestamp":str(int(time.time())),
                 "token":'8lV1bJcq76IsjkFvdY5DnM904zOgGHTB',
                 "nonce": get_digit()
                 }
            t['sign'] = get_sign(t)

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
            url = 'http://api.lesson.wrightin.com/v1/lesson'
            self.client.post(url,headers = header,json=t)


class Websiteuser(HttpLocust):
    task_set = Userbehavior
    max_wait = 6000
    min_wait = 3000