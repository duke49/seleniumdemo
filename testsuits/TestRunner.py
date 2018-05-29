import HTMLTestRunner
import unittest
import os
import time

'''import testsuits
from testsuits.test_get_page_title import GetPageTitle
from testsuits.baidu_search import BaiduSearch'''


#设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
#获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

#设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile,"wb")

#定义测试用例的目录为当前目录
test_dir = './'
suites = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#suites = unittest.TestSuite(unittest.makeSuite(BaiduSearch))

if __name__ == '__main__':
    #初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='百度搜索测试报告',
                                           description='用例执行情况：')
    runner.run(suites)
    fp.close()
