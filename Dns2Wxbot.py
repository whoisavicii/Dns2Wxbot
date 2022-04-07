#coding:utf-8
import requests
import json
import time
import subprocess



def read_domain_list():
    with open('domain.txt','r') as f:
        domain = f.readlines()
    return domain

def dns_request(domain):
    try:
        dns_result = subprocess.check_output(['dig', '+short', domain])
        dns_result = dns_result.decode('utf-8')
        dns_result = dns_result.split('\n')
        return dns_result
    except Exception as e:
        print(e)
        return None
    

def send_to_wx(domain,dns_result):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=XXXXXX'
    data = {
        "msgtype": "text",
        "text": {
            "content": "域名："+domain+"\n"+"解析结果："+str(dns_result)
        },
        "at": {
            "atMobiles": [
                "15012345678"
            ],
            "isAtAll": False
        }
    }
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.text)
    time.sleep(3)

if __name__ == '__main__':
    dns_result = dns_request(domain)
    send_to_wx(domain,dns_result)
