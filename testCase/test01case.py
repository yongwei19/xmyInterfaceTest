# 读取userCase.xlsx中的用例，使用unittest来进行断言校验
import json
import unittest
from common.configHttp import RunMain
import paramunittest
from geturlParams import geturlParams
import urllib.parse
import readExcel


# 调用我们的geturlParams 获取我们拼接的URL
url = geturlParams().get_url()
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')


@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):

    def setParameters(self, case_name, path, query, method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setUp(self):
        print(self.case_name + "测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):
        # 拼接完整的请求url
        new_url = url + self.query
        # 将一个完整的URL中的name=&pwd=转换成{'name':'xxx','pwd':'bbb'}
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        info = RunMain().run_main(self.method, url, data1)
        # 将响应转换成字典格式
        ss = json.loads(info)
        # 如果case_name是login，说明合法，返回code的值应该是200
        if self.case_name == 'login':
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'login_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'login_null':
            self.assertEqual(ss['code'], 10001)
