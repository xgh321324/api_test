#coding:utf-8
import requests,unittest
from common.login import LG
from common.logger import Log

class Doctor(unittest.TestCase):

    def setUp(self):
        self.log = Log()
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.gettoken_loginbyUID() #直接取第二部登录
        self.header = {'User-Agent': 'LanTingDoctor/1.3.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
    @unittest.skip('无条件跳过')
    def test_update_good_at(self):
        u'更新专业擅长接口'
        '''专业擅长内容：10 至 512 个字符'''
        self.log.info('开始测试更新专业擅长接口')

        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/modifyRep'
        content = [' ','08152','!@#$%^&~!@#$%^&*！@###@@','专业擅长吹牛a皮看电视手机立刻就','1asdddsa23WEsjkla在卡利姆多卢']

        for i in content:
            json_data = {"token":self.uid_token,
                             "rep":i
                             }
            r = self.s.post(url,headers = self.header,json=json_data)
            if len(i) < 10:
                self.assertEqual('请输入 10 至 512 个字符.',r.json()['msg'],msg='更新擅长内容失败')
            else:
                self.assertEqual('Success.',r.json()['msg'],msg='更新擅长内容失败')

        self.log.info('测试更新专业擅长接口结束！')

    @unittest.skip('无条件跳过')
    def test_update_person_info(self):
        u'更新个人简介接口'
        '''简介内容：10 至 512 个字符'''
        self.log.info('开始测试更新个人简介接口')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/modifyRemark'
        content = ['长度<10','长度等于十88888',
                   '长度大于10撒了很多哈桑的好阿三的快乐就到拉萨就叫',
                   '！@@#￥￥%&**……%……&*……&（是否合适2212WEJash'
                   ]

        for i in content:
            json_data = {"token":self.uid_token,
                             "remark":i
                             }
            r = self.s.post(url,headers = self.header,json=json_data)
            if len(i) < 10:
                self.assertEqual('请输入 10 至 512 个字符.',r.json()['msg'],msg='更新个人简介失败')
            else:
                self.assertEqual('Success.',r.json()['msg'],msg='更新个人简介失败')

        self.log.info('测试更新个人简介接口结束')

    @unittest.skip('无条件跳过')
    def test_update_born_date(self):
        u'测试更新出生日期接口'
        self.log.info('开始测试更新出生日期接口')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/modifyBorn'
        json_data = {"token":self.uid_token,
                     "born":"2017-05-01 00:00:00"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.assertEqual('Success.',r.json()['msg'],msg='更新出生日期失败')
        self.log.info('测试更新出生日期接口结束')

    @unittest.skip('无条件跳过')
    def test_uphospital_department(self):
        u'测试更新医院和科室接口'
        self.log.info('开始测试更新医院和科室接口')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/modifyHosDep'
        json_data = {"token":self.uid_token,
                     "huid":"99D8CA14B516813A698C63D745508D0E",
                     "kuid":"umvtDTbiCaR3Yl7xgEQSqWs0FAI1NHhd"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.assertEqual('Success.',r.json()['msg'],msg='更新医院和科室失败')
        self.log.info('测试更新医院和科室接口结束')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
