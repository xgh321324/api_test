#coding:utf-8
import requests,unittest
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Excel import Excel_util
import json
from common.Read_config import get_content
urllib3.disable_warnings()

class Comment(unittest.TestCase):
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

    def test_comment01(self):
        u'测试评论接口-评论内容正常'
        self.log.info('开始测试评论渟说接口-评论内容正常')
        url = get_content('sns_base_url')+'/v1/comment/add'
        #读取关联参数-推荐的动态的id
        read_recommened_ids = self.excel.read_value(13,6)
        feed_ids = json.loads(read_recommened_ids)
        L = []
        for i in feed_ids.values():
            L.append(i)
        json_data = {
            "id":L[0],
            "type":"1",
            "token":self.auto_login_token,
            "text":"很棒！"
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('评论feed返回的内容是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('评论成功.',r.json()['note'])
        self.log.info('评论渟说接口测试结束\n')

    def test_comment02(self):
        u'测试评论接口-评论内容为空'
        self.log.info('开始测试评论渟说接口-评论内容为空')
        url = get_content('sns_base_url')+'/v1/comment/add'
        #读取关联参数-推荐的动态的id
        read_recommened_ids = self.excel.read_value(13,6)
        feed_ids = json.loads(read_recommened_ids)
        L = []
        for i in feed_ids.values():
            L.append(i)
        json_data = {
            "id":L[0],
            "type":"1",
            "token":self.auto_login_token,
            "text":""
        }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('评论为空feed返回的内容是：%s' % r.json())
        self.assertEqual(501,r.json()['code'])
        self.assertEqual('text 的长度要求为 1 - 140.',r.json()['note'])
        self.log.info('评论渟说-评论内容为空测试结束\n')

    def test_comment03(self):
        u'删除评论接口'
        self.log.info('开始测试删除评论接口')
        #删除评论接口
        url = get_content('sns_base_url')+'/v1/comment/delete'
        #评论记录接口
        pre_url = get_content('sns_base_url')+'/v1/comment/records'
        #读取关联参数-推荐的动态的id
        read_recommened_ids = self.excel.read_value(13,6)
        feed_ids = json.loads(read_recommened_ids)
        L = []
        for i in feed_ids.values():
            L.append(i)
        pre_json_data = {"token":self.auto_login_token,"id":L[0],"time":0,"page":1}
        respon = self.s.post(pre_url,headers = self.header,json=pre_json_data)
        comment = respon.json()['data']['content']
        #获取评论id
        comment_id = []
        for x in comment:
            comment_id.append(x['comment_id'])
        #循环删除评论
        for y in comment_id:
            json_data = {"token":self.auto_login_token,"comment_id":y}
            r = self.s.post(url,headers = self.header,json=json_data)
            self.log.info('删除评论feed返回的内容是：%s' % r.json())
            self.assertEqual(200,r.json()['code'])
            self.assertEqual('删除评论成功.',r.json()['note'])
        self.log.info('删除评论接口测试结束\n')


    def tearDown(self):
        self.s.close()

if __name__=='__main__':
    unittest.main()


