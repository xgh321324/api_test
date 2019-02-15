#coding:utf-8
import xlrd,time
import xlwt
from xlutils.copy import copy
import json

class Excel_util():
    #舒适化要传入表格绝对路径
    def __init__(self,abspath):
        self.path = abspath
        #添加对应的参数formatting_info=True，可以保留原有格式
        self.data = xlrd.open_workbook(abspath,formatting_info=True)
        #self.w_data = xlwt.Workbook(abspath)    #只写入

    #获取要读取的sheet
    @property
    def gettable(self):
        #获取索引
        table = self.data.sheet_by_name('Sheet1')
        return table

    #下面是常用的读取具体位置数值
    def read_value(self,row,col):
        try:
            value = self.gettable.cell_value(row,col)
            print('Read suceess!')
            #print(value)
            return value
        except Exception as e:
            print('读取数据有错，原因：%s' % e)

    #下面是写入具体位置数据
    def write_value(self,row,col,value):
        """修改数据"""
        rb =self.data
        wb = copy(rb)
        s = wb.get_sheet(0)
        #设置自动换行
        style = xlwt.easyxf('align: wrap on')
        if type(value) == dict:
            #如果写入类型是dict需要转换成str输出
            try:
                new_value = json.dumps(value)
                s.write(row,col,new_value,style)
                wb.save(self.path)
                print ("Write finished")
            except Exception as e:
                print('数据写入失败，原因：%s' % e)
        elif type(value)==list:
            u'如果写入的值是list'
            try:
                for i in value:
                    s.write(row,col,value,style)
                    wb.save(self.path)
                    print('Write finished!')
            except Exception as e:
                print('数据写入失败，原因：%s' % e)

        else:
            try:
                s.write(row,col,value,style)
                wb.save(self.path)
                print ("Write finished")
            except Exception as e :
                print('数据写入失败，原因：%s' % e)

    #这个方法是将表格中所有数据返回成字典的格式 ；每一行是一个字典
    def dict_data(self):
        #先获取行数，列数
        self.rownum = self.gettable.nrows
        self.colnum = self.gettable.ncols
        #获取第一行为key的值
        self.keys = self.gettable.row_values(0)

        if self.rownum <= 1:
            print('表格中的数据行数小于1行')
        else:
            L = []
            x = 1 #初始值为1
            for i in range(self.rownum-1):
                s = {}
                #从第二行取对应values值
                values = self.gettable.row_values(x)
                for n in range(self.colnum):
                    s[self.keys[n]] = values[n]
                L.append(s)
                x += 1
            print(L)
            return L

    #这个方法是将excel中每一行生成一个字典，只需要传入caseid，字典的key是表头
    def get_dict(self,caseid):
        '''传入caseid即可以将此行数据返回成dict，每一个表头key对应该行的值'''
        self.rownum = self.gettable.nrows  #行数
        self.colnum = self.gettable.ncols  #列数
        self.keys = self.gettable.row_values(0) #获取表头
        #print(self.keys)

        if self.rownum <= 1:
            print('表格中的数据行数小于1行')
        else:
            d = {}
            #获取该caseid的values
            caseid_values = self.gettable.row_values(caseid)
            #将caseid这行的每一个value赋值给字典的key
            for i in range(self.colnum):
                d[self.keys[i]] = caseid_values[i]
        print(d)
        return d

if __name__== '__main__':
    s = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    #s.read_value(1,5)
    #d= {'a':1,'b':99}
    #s.write_relation_param(10,d)
    s.get_dict(11)








