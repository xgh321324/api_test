#coding:utf-8
import requests,unittest
from common.login import LG
from common.logger import Log

class Query(unittest.TestCase):
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

    def test_query_hosName(self):
        u'模糊查询医院接口'
        url = 'http://api.rih.medohealth.com/API/V1/DoctorInfo/SeacherHosName'
        content = [' ','南京','02182','麦澜德']  #模糊查询的内容

        for i in content:
            print(i)
            json_data = {
                "token":self.uid_token,
                "query":i
            }
            print(json_data)

            r = self.s.post(url,headers = self.header,json=json_data)
            self.assertEqual('Success',r.json()['msg'],'查询出错')


    def tearDown(self):
        self.s.close()

if __name__ == '__main__':
    unittest.main()


