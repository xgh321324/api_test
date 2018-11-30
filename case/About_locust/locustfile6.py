#coding:utf-8
from locust import HttpLocust,TaskSet,task
from common.Hash import get_md5

'''
实现场景：先登录（只登录一次），然后访问->我的地盘页->产品页->项目页
访问我的地盘页面权重为2，产品页和项目页权重各为1
'''

class UserBehavior(TaskSet):
    u'蝗虫类行为'
    def login(self):
        '登录方法'
        log_url = '/index.php?m=user&f=login'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'account': 'xuguanghui',
            'password': get_md5('xuguanghui@123'),
            'keepLogin[]': 'on',
            'referer': '/index.php?m=my&f=index'
        }
        r = self.client.post(log_url,headers = header,data=body)
        print(r.text)

    def on_start(self):
        '任务开始前会执行的工作'
        self.login()

    @task(2)
    def zendao_my(self):
        '我的地盘'
        print('访问禅道我的地盘')
        r = self.client.get('/index.php?m=my&f=index')
        assert '我的地盘' in r.text

    @task(1)
    def product(self):
        '产品页'
        print('访问产品页')
        r = self.client.get('/index.php?m=product&f=index')
        assert "产品" in r.text

    @task(1)
    def project(self):
        '项目'
        print('访问项目页')
        r = self.client.get('/index.php?m=project&f=task')
        assert "项目" in r.text

class WebsiteUser(HttpLocust):
    '用户行为'
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0

if __name__=='__main__':
    import os
    os.system('locust -f locustfile6.py --host=http://bug.zt.medohealth.com')

