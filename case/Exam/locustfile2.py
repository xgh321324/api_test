#coding:utf-8
import locust
from locust import HttpLocust,TaskSet,task
'''测试课程详情接口的性能'''

#定义用户行为
class Userbehavior(TaskSet):


    def login(self):

        r = self.client.post('http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorAutoLoginByUID',
                             {"UID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB","loginDevice":"2","loginCity":"no location"})
        x = r.json()['data']['Token']
        return x


    @task(2)
    def get_lesson(self):
        t = {"lesson_code":"K00011",
             "timestamp":"1527749688",
             "token":self.login()
             }
        self.client.post('/v1/lesson',t)


class Websiteuser(HttpLocust):
    task_set = Userbehavior
    max_wait = 6000
    min_wait = 3000