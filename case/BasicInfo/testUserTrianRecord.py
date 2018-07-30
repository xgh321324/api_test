#coding:utf-8
import requests,unittest,json
from common.login import LG
from common.logger import Log
from common.Excel import Excel_util

class Trian_record(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()
        self.lgin = LG(self.s) #实例化登录类
        self.uid_token = self.lgin.get_token() #直接取账号登录的token
        #self.auto_login_token = self.lgin.get_autologin_token() #取自动登录的token
        self.header = {'User-Agent':  'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding':  'gzip, deflate',
                       'Accept-Language':  'zh-Hans-CN;q=1',
                       'Content-Type':  'application/json',
                       'requestApp':  '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_get_user_trian_record(self):
        #测试前提是该医生有已绑定的用户
        u'医生根据日期查看用户训练记录接口'
        self.log.info('开始测试医生根据日期查看用户训练记录接口.....')

        #'这是获取已绑定的列表'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorToUserReleationShip/getReleathionShipInfo'
        json_data = {
            "token":self.uid_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        Patients = r.json()['data']
        User_UID = []
        for i in Patients:
            User_UID.append(i['UserUID'])
        print('当前医生绑定的用户的User_UID是：',User_UID)

        #判断当前医生是否有绑定的用户来执行不同操作
        if len(User_UID) >= 1:
            #如果有绑定的用户则：
            url2 = 'http://api.rih.sunnycare.cc/API/V1/UserTrainRecord/getUserTrainRecordByDoctorAndYearMonth'
            #列表存的是月份
            L = ['01','02','03','04','05','06']
            for i in L:
                json_data2 = {
                    "userUID":"hms7W3a1nG54IeBD6C9qtiuw82TjZVMQ",
                    "year":"2018",
                    "token":self.uid_token,
                    "month":i
                             }
                r2 = self.s.post(url2,headers = self.header,json=json_data2)
                print(r2.json())
                self.assertEqual(200,r2.json()['code'])

        else:
            self.log.warning('该医生还没有绑定的用户！')

        self.log.info('医生根据日期查看用户训练记录接口测试结束!!')

    def test_user_plan_trian_record(self):
        u'医生查看用户某一方案的治疗记录'
        self.log.info('开始测试医生查看用户某一方案训练记录接口.....')

         #'这是获取已绑定的列表'
        url = 'http://api.rih.sunnycare.cc/API/V1/DoctorToUserReleationShip/getReleathionShipInfo'
        json_data = {
            "token":self.uid_token
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        Patients = r.json()['data']
        User_UID = []
        for i in Patients:
            User_UID.append(i['UserUID'])
        print('当前医生绑定的用户的User_UID是：',User_UID)

        #判断当前医生是否有绑定的用户来执行不同操作
        if len(User_UID) >= 1:
            #将excel中courseid 读取出来
            read_course_id = self.excel.read_value(11,6)
            #将json转换成可用的dict
            need_course_id = json.loads(read_course_id)
            print(need_course_id)

            for c in need_course_id.values():
                url3 = 'http://api.rih.sunnycare.cc/API/V1/UserTrainRecord/getUserTrainRecordByCourseUIDForDoctor'
                json_data3 = {
                    "token":self.uid_token,
                    "userUID":User_UID[0],
                    "courseUID":c
                             }
                r3 = self.s.post(url3,headers = self.header,json=json_data3)
                #断言结果
                self.assertEqual(200,r3.json()['code'])

        else:
            self.log.warning('该医生还没有绑定的用户！')

        self.log.info('医生查看用户某一方案训练记录接口测试结束！！')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()
