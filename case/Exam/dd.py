#coding:utf-8
import unittest
from case.Exam.cc import get_formatte_name
class Name(unittest.TestCase):
    def test_name(self):
        t_name = get_formatte_name('join','bob')
        self.assertEqual('join bob',t_name)

    def test_name2(self):
        s_name = get_formatte_name('tom','bob',middle='mm')
        self.assertEqual('tom mm bob',s_name)

if __name__=='__main__':
    unittest.main()


