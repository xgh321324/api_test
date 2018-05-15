#coding:utf-8
import requests,unittest,random
from common.login import LG
from common.logger import Log

class ConfigInfo(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgin = LG() #实例化登录类
        self.uid_token = self.lgin.get_token() #直接取账号登录的token
        self.auto_login_token = self.lgin.get_autologin_token() #取自动登录的token
        self.header = {'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()

    def test_config_info(self):
        u'设置医生实名认证信息接口'
        self.log.info('开始测试医生实名认证接口.....')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/setDoctorInfoandTitle'
        json_data = {"id_card":"321324199103041432",
                     "image":"RightInDoctrorFiles\/Distribute\/TitleAuthentication\/IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB\/84810175026042607520180515134933.png",
                     "huid":"A596D422B726308EA01A9EB27D4417C0",
                     "key":random.randint(0,9),
                     "token":self.auto_login_token,
                     "kuid":"457BDE586E8AD22B683AB5740EDBA9F9",
                     "name":"许牛逼"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual('更新医生资料成功',r.json()['msg'])
        self.log.info('医生实名认证接口测试结束!')

    def test_doctor_profession(self):
        u'设置医生职称接口'
        self.log.info('开始测试设置医生职称.....')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/SetDoctorTitle'
        json_data = {"token":self.auto_login_token,
                     "duid":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                     "data":[{
                         #"image":'',
                         "key":"learn",
                         "code":random.randint(0,6)
                     }]
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())

        self.log.info('设置医生职称接口测试结束!')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

