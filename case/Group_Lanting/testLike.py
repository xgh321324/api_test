#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
urllib3.disable_warnings()

class Like(unittest.TestCase):
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


    def test_like01(self):
        u'点赞接口'
        self.log.info('开始测试点赞接口')
        #点赞接口
        url = 'http://api.sns.sunnycare.cc/v1/like/add'
        #取消点赞接口
        url02 = 'http://api.sns.sunnycare.cc/v1/like/delete'
        #推荐的内容接口
        url01 = 'http://api.sns.sunnycare.cc/v1/recommend/content'
        #读取关联参数-推荐的动态的id，再循环去点赞，断言结果
        #read_recommened_ids = self.excel.read_value(13,6)
        #feed_ids = json.loads(read_recommened_ids)
        json_data01 = {
            "token":self.auto_login_token,
            "time":0,
            "page":2
        }
        r1 = self.s.post(url01,headers = self.header,json=json_data01)
        con = r1.json()['data']['content']
        #print(con)
        #从推荐内容接口返回的内容判断这条内容我是否已点赞
        for i in con:
            if 'is_like' in i:
                #如果没点赞了就调用点赞接口
                if i['is_like'] == '0':
                    json_data02 = {
                        "id":i['id'],
                        "token":self.auto_login_token
                    }
                    r2 = self.s.post(url,headers = self.header,json=json_data02)
                    self.log.info('点赞返回的内容是：%s' % r2.json())
                    #self.assertEqual()
                else:
                    pass
            else:
                print('这条内容已删除！')
        self.log.info('点赞接口测试结束！\n')

    def test_like02(self):
        u'取消点赞接口'
        self.log.info('开始测试取消点赞接口')
        #点赞接口
        url = 'http://api.sns.sunnycare.cc/v1/like/add'
        #取消点赞接口
        url02 = 'http://api.sns.sunnycare.cc/v1/like/delete'
        #推荐的内容接口
        url01 = 'http://api.sns.sunnycare.cc/v1/recommend/content'
        #读取关联参数-推荐的动态的id，再循环去点赞，断言结果
        #read_recommened_ids = self.excel.read_value(13,6)
        #feed_ids = json.loads(read_recommened_ids)
        json_data01 = {
            "token":self.auto_login_token,
            "time":0,
            "page":2
        }
        r1 = self.s.post(url01,headers = self.header,json=json_data01)
        con = r1.json()['data']['content']
        #print(con)
        #从推荐内容接口返回的内容判断这条内容我是否已点赞
        for i in con:
            #如果已经点赞了就调用取消点赞接口
            if 'is_like' in i:
                if i['is_like'] == '1':
                    json_data02 = {
                        "id":i['id'],
                        "token":self.auto_login_token
                    }
                    r2 = self.s.post(url02,headers = self.header,json=json_data02)
                    self.log.info('取消点赞返回的内容是：%s' % r2.json())
                    #self.assertEqual()
                else:
                    pass
            else:
                print('这条内容已删除！')
        self.log.info('取消点赞接口测试结束！\n')

    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


