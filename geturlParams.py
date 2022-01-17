# 获取接口的URL、参数、method等
import readConfig as readConfig

readconfig = readConfig.ReadConfig()


# 定义一个类，将从配置文件中读取数据，并进行拼接
class geturlParams:

    def get_url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/login' + '?'
        # logger.info('new_url' + new_url)
        return new_url


if __name__ == '__main__':
    print(geturlParams().get_url())
