#coding:utf-8
import time,requests
h = {
    'token': 'asz120190213chau5c63a9bcfffd7cfcdf5aa03c0000000'
}
s = requests.session()

r = s.get('http://39.105.73.153/login/ali-login?os=android&device_token=Aq02lzYuCToe8oK7BXw0R_dBWMqD4iZ5fSL9ssqtR7uH&uuid=358543080625699&channel=应用宝', headers=h)
print(r.status_code)
print(r.text)

r2 = s.get('http://39.105.73.153/my/my-info')
print(r2.status_code)
print(r2.text)
