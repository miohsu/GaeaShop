import requests
import json


class SendMsg(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'
        # self.single_send_url = 'https://www.baidu.com'

    def send_msg(self, code, mobile):
        data = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': 'test {code}'.format(code=code)
        }
        response = requests.post(self.single_send_url, data=data)
        return json.loads(response.text)


if __name__ == '__main__':
    SendMsg('123').send_msg('4325', '11222222222')
