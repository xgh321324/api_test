#coding:utf-8
import unittest
from case.Exam.cc import get_formatte_name
from datetime import datetime
import time
from common.Hash import get_str,get_digit
'''
class Name(unittest.TestCase):
    def test_name(self):
        t_name = get_formatte_name('join','bob')
        self.assertEqual('join bob',t_name)

    def test_name2(self):
        s_name = get_formatte_name('tom','bob',middle='mm')
        self.assertEqual('tom mm bob',s_name)
'''
i = datetime.now()
n = i.timestamp()
print(n)
n1 = str(n).split('.')
print(n1[0])

j = time.time()
print('j:',j)
t = get_str()
print('t:',t)

#KX6pgwQt5OJU8xYjvFslkfZ4G3MTyNnP
#43148090150783523220180619093825
d1 = get_digit()
print('d1:',d1)

