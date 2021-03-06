#coding:utf-8
import requests,unittest,time
from common.login_lanting import auto_login_by_UID
from common.logger import Log
import urllib3
from common.Read_config import get_content
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

    def test_post_feed01(self):
        u'测试发布文字-不发布到圈子'
        self.log.info('测试发布文字接口-不发布到圈子')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {
            "token":self.auto_login_token,
            "text":"不知道自己的心"
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布文字接口-不发布到圈子情况测试结束\n')

    def test_post_feed02(self):
        u'测试发布文字到圈子-参数正常'
        self.log.info('测试发布文字到圈子-参数正常')
        url = get_content('sns_base_url')+'/v1/feed/add'
        t="背影作者: 打算跟着父亲奔丧回家。到徐州见着父亲，看见满院狼藉的东西，又想起祖母，不禁簌簌地流下眼泪。父亲说，“事已如此，不必难过，好在天无绝人之路！”回家变卖典质，父亲还了亏空；又借钱办了丧事。这些日子，家中光景很是惨淡，一半为了丧事，一半为了父亲赋闲。丧事完毕，父亲要到南京谋事，我也要回北京念书，我们便同行。到南京时，有朋友约去游逛，勾留了一日；第二日上午便须渡江到浦口，下午上车北去。父亲因为事忙，本已说定不送我，叫旅馆里一个熟识的茶房陪我同去。他再三嘱咐茶房，甚是仔细。但他终于不放心，怕茶房不妥帖；颇踌躇了一会。其实我那年已二十岁，北京已来往过两三次，是没有甚么要紧的了。他踌躇了一会，终于决定还是自己送我去。我两三回劝他不必去；他只说，“不要紧，他们去不好！”我们过了江，进了车站。我买票，他忙着照看行李。行李太多了，得向脚夫行些小费，才可过去。他便又忙着和他们讲价钱。我那时真是聪明过分，总觉他说话不大漂亮，非自己插嘴不可。但他终于讲定了价钱；就送我上车。他给我拣定了靠车门的一张椅子；我将他给我做的紫毛大衣铺好坐位。他嘱我路上小心，夜里警醒些，不要受凉。又嘱托茶房好好照应我。我心里暗笑他的迂；他们只认得钱，托他们直是白托！而且我这样大年纪的人，难道还不能料理自己么？唉，月台的栅栏外见！"
        json_data = {
            "token":self.auto_login_token,
            "text":t,
            'groups':['G00018']
                     }
        #for i in range(0,20):
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual(200,r.json()['code'])
        self.assertEqual('动态发布成功.',r.json()['note'])
        self.log.info('测试发布文字到圈子-参数正常情况测试结束\n')

    def test_post_feed03(self):
        u'测试发布文字到大于3个圈子-参数正常'
        self.log.info('测试发布文字到大于3个圈子-参数正常')
        url = get_content('sns_base_url')+'/v1/feed/add'
        json_data = {
            "token":self.auto_login_token,
            "text":"不知道自己的心",
            'groups':['G00001','G000016','G000017','G000018']
                     }
        r = self.s.post(url,headers = self.header,json=json_data)
        self.log.info('返回的内容是是：%s' % r.json())
        self.assertEqual('最多只能分享到 3 个圈子.',r.json()['note'])
        self.log.info('测试发布文字到大于3个圈子-参数正常情况测试结束\n')


    def tearDown(self):
        self.s.close()


if __name__=='__main__':
    unittest.main()
