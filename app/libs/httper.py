"""
 Created by sz on 2021/2/3
"""
__author__ = 'sz'

# urllib
# requests
# from urllib import request
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        # 发送请求
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''
