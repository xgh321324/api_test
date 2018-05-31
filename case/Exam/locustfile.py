#coding:utf-8
import locust
from locust import HttpLocust,TaskSet,task

#定义用户行为
class Userbehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        # = {'phoneInput':15651797525,'passwordInput':797525}
        r = self.client.post('/index.php?c=login',{'phoneInput':15651797525,'passwordInput':797525})


    @task
    def get_rec(self):
        #y = {'ci_session':'b66kucj24fr0q35rgqsr6c1afd51dhip'}
        self.client.post('/index.php?c=order',{'ci_session':'b66kucj24fr0q35rgqsr6c1afd51dhip'})


class Websiteuser(HttpLocust):
    task_set = Userbehavior
    max_wait = 6000
    min_wait = 3000
