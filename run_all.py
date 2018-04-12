import time
import HTMLTestRunner
#from BeautifulReport import BeautifulReport
def all_case():
    '''
    .discover 方法里面有三个参数：
    -case_dir:这个是待执行用例的目录。
    -pattern：这个是匹配脚本名称的规则，test*.py 意思是匹配 test 开头的所有脚本。
    -top_level_dir：这个是顶层目录的名称，一般默认等于 None 就行了
    '''
    #待执行的测试用例
    case_dir = r'C:\Users\Administrator\Documents\GitHub\Real_practice\case\Interface'
    test_case = unittest.TestSuite()   #创建测试套件(此时是个空的)
    discover = unittest.defaultTestLoader.discover(case_dir,pattern='test_d*.py',top_level_dir=None)
    #将discover筛选出的测试用例循环添加到测试套件中
    for case in discover:
        test_case.addTest(case)
    print(test_case)
    return test_case
if __name__ == '__main__':
    #be_run=unittest.TextTestRunner() #返回实例
    #run所有用例
    #be_run.run(all_case())
    report_path = r'C:\Users\Administrator\Documents\GitHub\Real_practice\report\kiss.html'  #报告存放路径,若用HTMLTestRunner则要加上具体文件名称

    with open(report_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='我的博客园接口测试报告',description='这是4月10日的测试结果',verbosity=2)
        runner.run(all_case())#这种用法也不错，也挺好看
    '''
    result = BeautifulReport(all_case())
    result.report(filename='测试接口1',description='这是4月10日的测试结果',log_path=report_path)#这种模板会好看一点
    '''