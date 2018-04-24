#coding:utf-8
import xlwt
from xlrd import *
from xlutils.copy import copy
from datetime import datetime
import time
path = r'C:\Users\Administrator\Desktop\Interface_testcase.xls'

def write():
    """写入单个数据"""
    rb = xlwt.Workbook()
    sheet = rb.add_sheet(u'copy',cell_overwrite_ok=True)
    sheet.write(1,1,"foo")        #向第0行第0列写入foo
    rb.save(path)

def wirte02():
    """写入一列数据,不能修改"""
    f = xlwt.Workbook()               #创建工作簿
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    l_=range(5)
    x = [42,4,14,14,14]
    for i in l_:
        sheet1.write(0,i,x[i])    #write的第一个,第二个参数时坐标, 第三个是要写入的数据
        sheet1.write(1,i,x[i])
    #sheet1.write(0,0,start_date,set_style('Times New Roman',220,True))
    f.save("2.xlsx")#保存文件

def write03(row,col,value):
    """修改数据"""
    rb =open_workbook(path)
    wb = copy(rb)
    s = wb.get_sheet(0)
    s.write(row,col,value)
    wb.save(path)
    print ("write finished")

def style1():
    """设置样式"""
    font = xlwt.Font()                            # Create the font
    font.name = 'Times New Roman'
    font.bold = True
    font.underline = True
    font.italic = True
    font.colour_index = 2

    style0 = xlwt.XFStyle()
    style0.font = font                           # Add font to Style

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    style1 = xlwt.XFStyle()
    style1.num_format_str = 'D-M-Y'

    ws.write(0, 0, 'Test', style0)
    # ws.write(2, 2, xlwt.Formula("A3+B3"))
    ws.write(2,2,time.strftime( "%Y-%m-%d %X", time.localtime()),style1)      #写入当前时间,精确到分钟
    wb.save('example425.xls')

if __name__=="__main__":
    write03()