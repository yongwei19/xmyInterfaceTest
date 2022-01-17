# 通过get、post、put、delete等方法来进行http请求，并拿到请求响应
import requests
import json


class RunMain:

    # 定义一个方法，传入需要的参数url 和 data
    def send_post(self, url, data):
        # 因为要封装post方法，所以这里的url和data不能写死
        # 参数必须要按照url、data顺序写入
        result = requests.post(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url=url, params=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    # 定义一个run_main方法，通过传过来的method来进行不同的get或post请求
    def run_main(self, method, url=None, data=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值有误")
        return result


# 验证一下自己写的请求是否正确
if __name__ == '__main__':
    result1 = RunMain().run_main('post', 'http://127.0.0.1:8888/login', {'name': 'xiaoming', 'pwd': '1113'})
    result2 = RunMain().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaoming&pwd=111')
    print(result1)
    print(result2)
