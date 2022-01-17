# 读取配置文件的方法，并返回文件中内容
import os
import configparser
# 引入自己写的获取路径的类
import getpathInfo

# 调用实例化，这个类返回的路径为 D:\pyhton\xmyInterfaceTest\testFile
path = getpathInfo.get_Path()
# 在path路径下再加一级，最后变成D:\pyhton\xmyInterfaceTest\testFile\config.ini
config_path = os.path.join(path, 'config.ini')
# 调用外部的读取配置文件的方法
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig:

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中开关on_off值为：', ReadConfig().get_email('on_off'))

