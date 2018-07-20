#coding:utf-8
import requests,unittest
from common.logger import Log
from common.login import LG

class Feedback(unittest.TestCase):


    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
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

    @unittest.skip('无理由跳过！')
    def test_feedback(self):
        u'测试一键反馈接口'
        self.log.info('测试意见反馈只反馈文字')
        url = 'http://api.rih.medohealth.com/API/V1/UserFeedBack/addAUserFeedBack'
        json_data = {"ufbTitle":"反馈信息",
                     "ufbUIUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                     "ufbDesc":"urjrjfjfjfjfjfjrjrjjffjj",
                     "token":self.auto_login_token,
                     "ufbImages":"[]",
                     }
        r = self.s.post(url,headers= self.header,json=json_data)
        print(r.json())
        self.assertEqual('反馈成功',r.json()['msg'],msg='只反馈文字出错了')
        self.log.info('意见反馈只反馈文字成功！')

        self.log.info('测试意见反馈反馈图片和文字:')
        json_data2 = {"ufbTitle":"反馈信息",
                      "ufbUIUID":"IKxSa8XhbiJH1CYlwQvkW50oLefZ62uB",
                      "ufbDesc":"南京今天",
                      "ufbImages":"[\"feedbackimages\/23411.png\"]",
                      "token":""
                      }
        r2 = self.s.post(url,headers = self.header,json=json_data2)
        print('r2',r2.json())
        self.assertEqual('反馈成功',r.json()['msg'],msg='反馈出错了')
        self.log.info('测试意见反馈反馈图片和文字成功！')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


