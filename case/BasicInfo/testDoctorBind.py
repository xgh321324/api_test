#coding:utf-8
import requests,unittest,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util

#注意：
#执行该py模块之前请确保澜渟医生端无绑定请求，且无绑定数据

class Doctor_bind(unittest.TestCase):
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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')


    def test_bind_01(self):
        u'这是获取已绑定的列表'
        url = 'http://api.rih.medohealth.com/API/V1/DoctorToUserReleationShip/getReleathionShipInfo'
        json_data = {"token":self.auto_login_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        t = r.json()
        self.excel.write_value(10,5,t)
        Patients = r.json()['data']
        Patient_ids = {}
        n = 1
        for i in Patients:
            Patient_ids['user_id'+str(n)]=i['UserUID']
            n += 1
        self.excel.write_value(10,6,Patient_ids)



    def test_bind_02(self):
        u'添加 医生 - 患者 的绑定关系请求接口--医生绑定病人'

        #DoctorUID	:医生的身份标识符
        #UserUID	:患者的身份标识符
        #BindReqDevices:请求绑定的设备类型
        #token :Token
        self.log.info('添加 医生 - 患者 的绑定关系请求接口测试开始.....')
        self.log.info('医生先发出绑定邀请')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorAndUserBindStatus/addABindReq'
        json_data = {"UserUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH",
                     "BindReqDevices":"2",
                     "DoctorUID":'IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB',
                     "token":self.auto_login_token
                     }
        r = self.s.post(url,headers= self.header,json=json_data)
        self.assertEqual('邀请成功' or '保存成功',r.json()['msg'])
        self.log.info('医生先发出邀请成功。。。')

        self.log.info('医生再取消此邀请：')
        #邀请成功后再取消邀请
        url2 = 'http://api.rih.medohealth.com/API/V1/DoctorAndUserBindStatus/cancelBind'
        json_data2 = {"UserUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH",
                      "DoctorUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                      "BindReqUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                      "token":self.auto_login_token,
                      "BindRspDevices":"2"
                      }
        r2 = self.s.post(url2,headers = self.header,json=json_data2)
        self.assertEqual(200,r2.json()['code'])
        self.log.info('医生再取消邀请成功')

        self.log.info('添加 医生 - 患者 的绑定关系请求接口测试结束！')

    def test_bind_03(self):
        u'取消绑定接口-医生解除绑定病人'
        self.log.info('同意绑定请求接口测试开始...\n')

        self.log.info('1.医生先发出绑定邀请:')

        url_1 = 'http://api.rih.medohealth.com/API/V1/DoctorAndUserBindStatus/addABindReq'
        json_data1 = {"UserUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH",
                     "BindReqDevices":"2",
                     "DoctorUID":'IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB',
                     "token":self.auto_login_token
                     }
        r1 = self.s.post(url_1,headers= self.header,json=json_data1)
        self.assertEqual('邀请成功' or '保存成功',r1.json()['msg'])
        self.log.info('1.邀请成功。')

        self.log.info('2.用户同意邀请:')
        #这里要用到澜渟app端的token
        url_before = 'http://api.rih.medohealth.com/API/V1/LogForToken/autoLoginByUID'
        js_data = {"uiUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH",
                   "loginDevice":"2",
                   "loginCity":"no location"
                   }
        before_response = self.s.post(url=url_before,headers = self.header,json=js_data)
        t = before_response.json()['data']['Token']
        print('澜渟app的登录token：',t)

        url_2 = 'http://api.rih.medohealth.com/API/V1/DoctorAndUserBindStatus/agreeBind'
        json_data2 = {"UserUID":"Y7xdvSRFmWiKqEM195u6CNyt8kfrLJBH",
                      "DoctorUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                      "BindReqUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                      "token":t,
                      "BindRspDevices":"2"
                      }
        self.header['requestApp'] = "4.1"
        r2 = self.s.post(url_2,headers = self.header,json=json_data2)
        self.assertEqual('同意成功',r2.json()['msg'],msg='同意绑定出错！')
        self.log.info('2.用户同意成功！\n')

        self.log.info('同意绑定接口测试结束！！')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
