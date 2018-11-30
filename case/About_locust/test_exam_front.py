#coding:utf-8
import requests,unittest,time
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util
from common.Hash import get_digit,get_sign
import json

class Meet(unittest.TestCase):
    def setUp(self):
        #banner获取接口
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.login() #直接取第二部登录
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
        self.log = Log()
        self.EXCEL = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_getbanner(self):
        u'测试获取banner链接接口'
        self.log.info('----------开始测试获取banner接口-----------')
        url = 'http://api.meet.sunnycare.cc/v2/banner'
        json_data = {
            "token":self.uid_token,
            'timestamp': str(int(time.time())),
            'nonce':get_digit()
        }
        json_data['sign'] = get_sign(json_data)
        r = self.s.post(url=url,headers = self.header,json=json_data)
        self.log.info('返回的内容是：%s' % r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
            self.assertEqual(200,r.json()['code'])
            self.log.info('接口返回状态成功！')
        except Exception as e:
            self.log.error('请求失败，原因是：%s' % e)
            raise AssertionError

        #取出json中banner链接依次进行get
        links = r.json()['data']
        for link in links:
            super_link = link['image']
            r2 = self.s.get(url=super_link,headers = self.header)
            try:
                self.assertEqual(200,r2.status_code)
                self.log.info('banner链接请求成功')
            except Exception as e:
                self.log.error('banner链接请求失败，原因：%s' % e)
                raise AssertionError
        self.log.info('----------banner接口测试结束-----------')


    def test_get_meets(self):
        u'测试获取会议接口'
        url = 'http://api.exam.wrightin.com/v1/meetNew'
        self.log.info('------开始获取会议接口测试-------')
        json_data = {
            "token":self.uid_token,
            "time":"0"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        #判断返回状态
        #print(r.json())
        try:
            self.assertEqual('请求成功.',r.json()['note'])
            self.log.info('获取会议接口返回状态成功')
        except Exception as e:
            self.log.error('返回状态不成功，原因：%s' % e)
            raise AssertionError


        #判断会议内容不为空
        meet_list = r.json()['data']['list']
        try:
            self.assertLessEqual(1,len(meet_list))
            self.log.info('会议内容不为空')
        except Exception as e:
            self.log.error('会议内容为空。原因：%s' % e)
        self.log.info('------获取会议接口测试结束-------')

    def test_meet_info(self):
        u'测试每个具体的会议信息'
        self.log.info('=========开始测试会议信息接口==========')
        #要先获取到每个会议的code
        url_1 = 'http://api.meet.sunnycare.cc/v2/meet/records'
        json_data_1 = {
            "token":self.uid_token,
            "time":"0",
            'timestamp': str(int(time.time())),
            'nonce': get_digit()
        }
        json_data_1['sign'] = get_sign(json_data_1)
        #先获取会议列表
        r1 = self.s.post(url_1,headers = self.header,json=json_data_1)
        #从会议列表中取会议code
        response = r1.json()['data']['list']
        codes = []
        for i in response:
            codes.append(i['code'])
        #print('code::::',codes)
        #循环对每一个会议code获取会议信息
        url_2 = 'http://api.meet.sunnycare.cc/v2/meet'
        #创建考试code list
        exam_codes = []

        for code in codes:
            json_data_2 = {
                "token":self.uid_token,
                "meet_code":code,
                'timestamp': str(int(time.time())),
                'nonce': get_digit()
            }
            json_data_2['sign'] = get_sign(json_data_2)
            r2 = self.s.post(url_2,headers = self.header,json=json_data_2)#json_data可以共用
            #print(r2.json())
            #断言每个会议信息的返回状态
            try:
                self.assertEqual('请求成功.',r2.json()['note'])
                self.log.info('会议信息返回状态成功')
            except Exception as e:
                self.log.error('会议信息返回状态失败，原因：%s' % e)
                raise AssertionError

            #获取试卷code作为关联参数
            d = r2.json()['data']
            exam_codes.append(d['exam_code'])

        #去除exam列表中的空元素
        new_exam_codes = []
        for i in exam_codes:
            if i != '':
                new_exam_codes.append(i)
        print('exam code:' ,new_exam_codes)
        #将exam code 以字典格式写入excel
        D = {}
        x = 1
        for i in new_exam_codes:
            D['exam_code'+ str(x)] = i
            x += 1
        self.EXCEL.write_value(3,5,json.dumps(D))
        self.log.info('=========测试会议信息接口结束==========')


    def test_exam_msg(self):
        u'测试获取考试信息 接口'
        self.log.info('-----------开始测试获取考试信息 接口-----------')
        #之前写入excel是str类型，现在转换为dict类型
        exam_codes = json.loads(self.EXCEL.read_value(3,5))
        self.log.info('读取的考试code是：%s' % exam_codes)
        url = 'http://api.exam.sunnycare.cc/v1/examMsgByMeetCode'
        #循环字典的value作为examcode
        for value in exam_codes.values():
            json_data = {
                "token":self.uid_token,
                "examcode":value,
                "userid":"107dfd1c1ade4a0f820e4897491710c6"
            }
            r = self.s.post(url,headers=self.header,json=json_data)
            try:
                self.assertEqual('请求成功.',r.json()['note'])
                self.log.info('考试信息获取成功！')
            except Exception as e:
                self.log.error('考试信息获取失败，原因是：%s' % e)
                raise AssertionError

        self.log.info('-----------开始测试获取考试信息 接口测试结束！-----------')

    def tearDown(self):
        self.s.close()
if __name__ == '__main__':
    unittest.main()
