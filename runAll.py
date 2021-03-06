# 开始执行接口自动化，项目工程部署完毕后直接运行该文件即可
import os
import unittest
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import readConfig
from common.configEmail import SendEmail
import common.Log

send_mail = SendEmail(
    username='zxxxx@mxxxx.com',
    passwd='',
    recv=[''],
    title='测试报告',
    content='测试报告',
    file=r'D:\pyhton\xmyInterfaceTest\result\report.html',
    ssl=True,
)
path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = common.Log.logger


class AllTest:
    # 初始化一些参数和数据
    def __init__(self):
        global resultPath
        # result/report.html
        resultPath = os.path.join(report_path, "report.html")
        # 配置执行哪些测试文件的配置文件路径
        self.caseListFile = os.path.join(path, "caselist.txt")
        # 真正的测试断言文件路径
        self.caseFile = os.path.join(path, "testCase")
        self.caseList = []

        # 将resultPath的值输出到日志中，方便定位问题
        log.info('resultPath: ' + resultPath)
        log.info('caseListFile: ' + self.caseListFile)
        log.info('caseList: %s', self.caseList)

    def set_case_list(self):
        # 取caselist.txt文件中的用例名称，并添加到caselist元素组
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            # 如果data非空且不以#号开头
            if data != '' and not data.startswith("#"):
                # 读取每行数据会将换行转换为\n，去掉每行数据中的\n
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        # 通过set_case_list()拿到caselist元素组
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        # 从caseList元素组中循环取出case
        for case in self.caseList:
            # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            case_name = case.split("/")[-1]
            print(case_name + ".py")
            # 批量加载用例，第一个参数为用例存放路径，第二个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(start_dir=self.caseFile, pattern='test*.py',
                                                           top_level_dir=None)
            # 将discover存入suite_module元素组
            suite_module.append(discover)
            print('suite_module:' + str(suite_module))
        # 判断suite_module元素组是否存在元素
        if len(suite_module) > 0:
            # 如果存在，循环取出元素组内容，命名为suite
            for suite in suite_module:
                # 从discover中取出test_name，使用addTest添加到测试集
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print("else:")
            return None
        return test_suite

    def run(self):
        try:
            suit = self.set_case_suite()
            print("try")
            print(str(suit))
            if suit is not None:
                print("if-suit")
                fp = open(resultPath, 'wb')
                # 调用HTMLTestRunner
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report',
                                                       description='Test Description')
                runner.run(suit)
            else:
                print("Have no case to test.")
        except Exception as ex:
            print(str(ex))
            log.info(str(ex))
        finally:
            print("*********TEST END*********")
            log.info("*********TEST END*********")
            fp.close()
        # 判断邮件发送的开关
        if on_off == 'on':
            send_mail.send_email()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")


if __name__ == '__main__':
    AllTest().run()
