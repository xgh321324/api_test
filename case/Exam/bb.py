#coding:utf-8
path = r'C:\Users\Administrator\Desktop\digist.txt'
with open(path) as f:
    #L=f.readline()#读取一行
    #L1=f.readlines()
    L2 = f.read()
print(L2)

#覆盖写入
with open(path,'w') as f:
    f.write('今天是个好日子\n')
    print('写入成功！')
#追加模式写入
with open(path,'a') as f:
    f.write('明天也是个好日子哦')
    print('写入成功！')

try:
    a = 7
    b = 0
    print(a/b)
except Exception as e:
    print(e)

title = 'alice in wonderland'
s = title.split()
print(s)

print('=======================')
import json
li = [2, 3, 5, '7', 11, 13]
path = r'C:\Users\Administrator\Desktop\numbers.json'
#json.dump() 写入json文件，dump要传入两个参数
with open(path,'w') as f:
    json.dump(li,f)


#json.load 将json文件中的内容读取到内存中
filename = r'C:\Users\Administrator\Desktop\numbers.json'
with open(filename) as f_obj:
    s = json.load(f_obj)
print(s)
print('=========================')

filename = r'C:\Users\Administrator\Desktop\number.json'
try:
    with open(filename) as f:
        username = json.load(f)
except Exception:
    username = input('what is your name?:')
    with open(filename,'w') as f:
        json.dump(username,f)
else:
    print('welcome '+ username+'!!!')
