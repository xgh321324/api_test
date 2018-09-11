#coding:utf-8
import requests
from common.Read_config import get_content

def auto_login_by_UID():
    #这是澜渟测试环境app的登录脚本
    header = {'User-Agent': 'LanTingDoctor/2.0.2 (iPad; iOS 10.1.1; Scale/2.00)',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-Hans-CN;q=1',
                       'Content-Type': 'application/json',
                       'requestApp': '3',
                       'requestclient': '2',
                       'versionForApp': '2.0',
                       'Authorization': 'Basic YXBpTGFudGluZ0BtZWRsYW5kZXIuY29tOkFwaVRobWxkTWxkQDIwMTM=',
                       'Connection': 'keep-alive'
                       }
    url = 'http://api.rih.sunnycare.cc/API/V1/LogForToken/autoLoginByUID'
    json_data = {"uiUID":"hms7W3a1nG54IeBD6C9qtiuw82TjZVMQ"}
    s = requests.session()
    r = s.post(url,headers = header,json=json_data,verify=False)
    #print(r.json())
    t = r.json()['data']['Token']
    #print(t)
    return (t)

if __name__=='__main__':
    auto_login_by_UID()