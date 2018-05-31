#coding:utf-8
import json
import pymysql
def get_formatte_name(first,last,middle=''):
    u'中间名师可选参数'
    if middle:
        formatted_name = first +' '+ middle + ' '+last
    else:
        formatted_name = first +' '+ last
    return formatted_name

def write_sql():
    u'传入要写入文件的路径'
    path = r'C:\Users\Administrator\Desktop\digist.txt'

    for i in range(1,1001):
        #加入要造1000条假数据
        str_i = str(i)
        real_name = 'jack'+ str_i
        phone = 13800110000+i
        email = 'jack'+str_i+'@mail.com'
        #符串用双引号加单引号"''"
        #sql = 'insert into table_a (realname,phone,email,sign,event_id) values ("'+realname+'",' +str(phone)+ ',"'+email+'",0,1);'
        sql = "insert into sign_gust (realname,phone,email,sign,event_id) VALUES (%s,%s,%s,%s,%s)" % (real_name,phone,email,0,1)
        with open(path,'a') as f:
            #必须要用‘a’这样是追加写入
            f.write(sql)
            f.write('\n')


if __name__=='__main__':
    write_sql()




