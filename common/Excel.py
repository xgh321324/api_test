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
    @property
    def get_row_num(self):
        row_num = self.gettable.nrows
        return row_num
    @property
    def get_col_num(self):
        col_num = self.gettable.ncols
        return col_num
    @property
    #获取每一列的值
    def get_case_name(self):
        names = []
        for i in range(1,self.get_row_num):
            names.append(self.gettable.cell_value(i,0))
        return names
    @property
    #获取请求方式
    def get_get_way(self):
        ways = []
        for i in range(1,self.get_row_num):
            ways.append(self.gettable.cell_value(i,1))
        return ways
    #获取接口url
    @property
    def get_url(self):
        urls = []
        for i in range(1,self.get_row_num):
            urls.append(self.gettable.cell_value(i,2))
        return urls

    #获取入参
    @property
    def get_Input_parameter(self):
        parameters = []
        for i in range(1,self.get_row_num):
            parameters.append(self.gettable.cell_value(i,3))
        return parameters
    #获取出参
    @property
    def get_out_parameter(self):
        parameters = []
        for i in range(1,self.get_row_num):
            parameters.append(self.gettable(i,4))
        return parameters
    #获取期望输出
    @property
    def get_Expect_out(self):
        parameters = []
        for i in range(1,self.get_row_num):
            parameters.append(self.gettable.cell_value(i,5))
        return parameters



###########################################################################################################
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
        else:
            try:
                s.write(row,col,value,style)
                wb.save(self.path)
                print ("Write finished")
            except Exception as e :
                print('数据写入失败，原因：%s' % e)

#########################################################################################################
    #一下两个方法只适用于以字典格式存储关联参数

    def write_relation_param(self,case_id,value):
        u'只需要传入一个caseid 就可以直接把关联参数写入对应的关联参数列'
        rb =self.data
        wb = copy(rb)
        s = wb.get_sheet(0)
        #设置自动换行
        style = xlwt.easyxf('align: wrap on')
        #将要写入内容转换为str写入
        str = json.dumps(value)
        try:
            s.write(case_id - 1,6,str)
        except Exception as e:
            print('写入失败，原因：%s' % e)

    def read_relation_param(self,case_id):
        u'只需要传入一个caseid 就可读取其中内容'
        try:
            value = self.gettable.cell_value(case_id,6)
            print('Read suceess!')
            #将读取的内容转换为字典格式
            real_value = json.loads(value)
            return real_value
        except Exception as e:
            print('读取数据有错，原因：%s' % e)



if __name__== '__main__':
    s = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    s.read_value(1,5)
    s.write_value(1,5,'今天是个好日子，阿三将会对阿什顿建的话，，阿神大叔大婶都卡的：{88888888888888888888888888888888888888888}')









