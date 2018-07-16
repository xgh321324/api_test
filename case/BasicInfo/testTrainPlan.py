#coding:utf-8
import requests,time,unittest
from common.logger import Log
from common.login import LG
from common.Excel import Excel_util

class Trian(unittest.TestCase):

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
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_get_user_plan(self):
        u'医生获取用户训练方案接口'
        self.log.info('开始测试医生查看用户训练方案接口.....')

        #'这是获取已绑定的列表'
        url = 'http://api.rih.medohealth.com/API/V1/DoctorToUserReleationShip/getReleathionShipInfo'
        json_data = {"token":self.auto_login_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        Patients = r.json()['data']
        User_UID = []
        for i in Patients:
            User_UID.append(i['UserUID'])
        print(User_UID)

        #判断当前医生是否有绑定的用户来执行不同操作
        if len(User_UID) >= 1:
            #当绑定不为空时，医生再去获取用户的方案
            for id in User_UID:
                url_2 = 'http://api.rih.medohealth.com/API/V1/UserTrainCourse/getUserTrainCourseByDoctor'
                json_data_2 = {"token":self.auto_login_token,
                             "userUID":id
                             }
                r2 = self.s.post(url_2,headers = self.header,json=json_data_2)
                self.assertEqual(200,r2.json()['code'])
                plans = r2.json()['data']
            #将方案的course id写入excel供调用
            course_ids = {}
            n = 1
            for p in plans:
                #print(p)
                course_ids['corse_id_'+ str(n)]=p['utcUID']
                n += 1
            self.excel.write_value(11,6,course_ids)

        else:
            self.log.warning('该医生还没有绑定的用户！')

        self.log.info('医生查看用户训练方案接口测试结束！')



    def test_get_doctor_plan(self):
        u'医生获取训练方案接口'
        self.log.info('开始测试医生的训练方案接口.....')
        url = 'http://api.rih.medohealth.com/API/V1/DoctorTrainCourse/getTrainCourseForDoctor'
        json_data = {"token":self.auto_login_token}
        r = self.s.post(url,headers = self.header,json=json_data)
        print(r.json())
        self.assertEqual(200,r.json()['code'])
        self.log.info('医生的训练方案接口测试结束！！')




    def tearDown(self):
        self.s.close()

if __name__ == '__mian__':
    unittest.main()

