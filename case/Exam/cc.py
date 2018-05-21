#coding:utf-8
import json

def get_formatte_name(first,last,middle=''):
    u'中间名师可选参数'
    if middle:
        formatted_name = first +' '+ middle + ' '+last
    else:
        formatted_name = first +' '+ last
    return formatted_name

