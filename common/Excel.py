#coding:utf-8
import xlrd
class Excel_util():
    def __init__(self,abspath):
        #打开表格
        self.data = xlrd.open_workbook(abspath)

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
if __name__== '__main__':
    s = Excel_util(r'C:\Users\Administrator\Desktop\Interface_testcase.xls')
    print(s.get_row_num)
    print(s.get_col_num)
    print(s.get_case_name)
    print(s.get_get_way)
    print(s.get_Expect_out)
    print(s.get_url)








