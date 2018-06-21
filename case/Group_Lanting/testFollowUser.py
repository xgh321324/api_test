#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
from common.Read_config import get_content
import json
urllib3.disable_warnings()

class Feed(unittest.TestCase):
    def setUp(self):
        self.s = requests.session()
        self.auto_login_token = auto_login_by_UID()  #auto_login_by_UID返回的token
        self.header = {'User-Agent': 'PelvicFloorPersonal/4.1.1 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '2',
                       'requestclient': '2',
                       'versionForApp': '4.1.1',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
        self.log = Log()
        self.excel = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')

    def test_follow_user(self):
        u'关注某一用户和取消关注某用户接口-参数正常'
        self.log.info('开始测试关注用户接口')
        follow_url = get_content('sns_base_url')+'/v1/follow'
        cancle_url = get_content('sns_base_url')+'/v1/cancel'
        #这是推荐用户列表接口
        pre_url = get_content('sns_base_url')+'/v1/recommend/user'
        pre_json_data = {
            "token":self.auto_login_token,
            "time":0,
            "page":1
        }
        re = self.s.post(pre_url,headers = self.header,json=pre_json_data)
        #取出每个用户关注状态
        con = re.json()['data']['content']
        #print(con)
        #循环content来判断用户是否被关注了
        L1=[]
        L2=[]
        for i in con:
            #如果该用户还未关注就关注他检查返回结果
            if i['is_follow'] == 0:
                L1.append(i['user_id'])
                json_data = {
                    "user_id":i['user_id'],
                    "token":self.auto_login_token
                }
                r = self.s.post(follow_url,headers = self.header,json=json_data)
                self.log.info('关注用户返回的内容是：%s' % r.json())
                self.assertEqual(200,r.json()['code'])
                self.assertEqual('关注成功.',r.json()['note'])
                #self.assertEqual(1,r.json()['data']['is_follow'])
            #如果该用户已经被关注就取消关注他没检查返回结果
            elif i['is_follow']=='1' or '2' :
                L2.append(i['user_id'])
                json_data = {
                    "user_id":i['user_id'],
                    "token":self.auto_login_token
                }
                r = self.s.post(cancle_url,headers = self.header,json=json_data)
                self.log.info('取消关注用户返回的内容是：%s' % r.json())
                self.assertEqual(200,r.json()['code'])
                self.assertEqual('取消关注成功.',r.json()['note'])
            else:
                pass

        self.log.info('关注用户接口测试结束\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()

