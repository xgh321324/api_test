#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
class Excel_util():
    def __init__(self,abspath):
        #打开表格
        self.data = xlrd.open_workbook(abspath) #只读
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
###############################################################################################################
    '''
    #获取要读取的sheet
    @property
    def get_tabel2(self):
         # 所以在打开时加cell_overwrite_ok=True 解决一个单元格重复操作报错问题
        tabel = self.w_data.add_sheet('demo',cell_overwrite_ok=True)
        return tabel

    #写入出参
    @property
    def write_out_parameter(self,value):
        self.get_tabel2.witr(2,4,lable=value)
        self.w_data.save(r'C:\Users\Administrator\Desktop\test.xls')

'''


if __name__== '__main__':
    s = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    s.write_out_parameter(value='888')








