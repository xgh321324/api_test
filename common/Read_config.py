#coding:utf-8
import json

#这个文件主要是封装一个读取配置文件的方法

def get_content(key):
    #传入要读取的内容的key
    with open(r'C:\Users\Administrator\Documents\GitHub\Medohealth\config\config.json') as f:
        #先读取
        text = json.load(f)
    print(type(text)) #此时数据已经是dict
    print(text[key])
    return text[key] #返回dict的value


if __name__=='__main__':
    get_content('base_url')
