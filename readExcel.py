# 读取Excel的方法
import os
# 己定义的内部类，该类返回项目的绝对路径
import getpathInfo
# 调用读Excel的第三方库xlrd
from xlrd import open_workbook


# 拿到该项目所在的绝对路径
path = getpathInfo.get_Path()


class readExcel:
    # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
    def get_xls(self, xls_name, sheet_name):
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, 'testFile/case', xls_name)
        # 打开用例的excel
        file = open_workbook(xlsPath)
        # 打开sheet文件
        sheet = file.sheet_by_name(sheet_name)
        # 获取这个sheet文件的行数
        nrows = sheet.nrows
        for i in range(nrows):
            # 如果这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    print(readExcel().get_xls('userCase.xlsx', 'login'))
    print(readExcel().get_xls('userCase.xlsx', 'login')[0][1])
    print(readExcel().get_xls('userCase.xlsx', 'login')[1][2])
