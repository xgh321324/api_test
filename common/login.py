#coding:utf-8
import time
import unittest
import requests
class LG():

    def __init__(self,s):
        self.s = requests.session()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.0.0.13547',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '1',
                       'versionForApp': '2.1.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'}

    def login(self):
        '''登录方法'''
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/loginByUsername'
        #利用自己固定的账号密码登录
        t = {"username":"15651797525","password":"123456","loginDevice":"2","loginCity":"南京市"}
        r = self.s.post(url,headers=self.header,json=t)
        #print(r.json())
        tok = r.json()['data']['Token']
        #print(tok)
        return tok


    def get_token(self):
        '''取第一步登录成功后的token作为下一步的请求体'''
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/loginByUsername'
        #利用自己固定的账号密码登录
        t = {
            "username": "15651797525",
            "password": "123456",
            "loginDevice": "1",
            "loginCity": "南京市"
        }
        r = self.s.post(url,headers=self.header,json=t)
        success_token = r.json()['data']['Token']  #后面的很多操作会用到这个token，该token在登录成功后的步骤中作为请求的数据
        #print('success token:%s' % success_token)
        return success_token

    def get_duid(self):
        '''取第一步登录成功后的duid作为第二部登录的请求体'''
        #url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/loginByUsername' #测试环境
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/loginByUsername'
        t = {
            "username": "15651797525",
            "password": "123456",
            "loginDevice": "1",
            "loginCity": "南京市"
        }
        r = self.s.post(url,headers=self.header,json=t)
        success_duid = r.json()['data']['doctorInfo']['duid']  #后面的很多操作会用到这个duid，
        #print(success_duid)
        return success_duid


    def gettoken_loginbyUID(self):
        u'取第二部UID登录成功后的token'
        #url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'  #医生用uid自动登录接口'  测试环境
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'
        json_data1 = {
            "UID": str(self.get_duid()),
            "loginDevice": "1",
            "loginCity": "南京市"
        }  #device 1是安卓
        r = self.s.post(url,headers= self.header,json=json_data1) ##医生用uid自动登录接口的请求数据又是登录成功后返回的json中的duid
        UID_token = r.json()['data']['Token'] #取到我想要的token
        #print(UID_token)
        return UID_token

    def get_autologin_token(self):
        url = 'http://api.rih.medohealth.com/API/V1/DoctorLoginForToken/doctorAutoLoginByUID'
        json_data = {
            "UID": str(self.get_duid())
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        t = r.json()['data']['Token']
        return t


if __name__=='__main__':
    s = requests.session()
    x = LG(s)
    x.login()

