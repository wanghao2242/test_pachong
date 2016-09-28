#_*_ coding:utf-8 _*_
import re
import urllib
import urllib.request
from collections import deque
import http.cookiejar

'''
url = 'http://www.baidu.com'
data = urllib.request.urlopen(url).read()
#decode解码
data = data.decode('UTF-8')
print(data)
'''
'''
data = {}
data['word'] = 'Jecvay Notes'

#urllib.parse.urlencode把一个通俗的字符串, 转化为url格式的字符串url_values
url_values = urllib.parse.urlencode(data)
# print(url_values)
url = 'http://www.baidu.com/s?'
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)
'''

queue = deque()
visited = set()

url = 'http://www.baidu.com'

queue.append(url)
cnt = 0
def saveFile(ddd):
    save_path = 'temp.out'
    f_obj = open(save_path, 'a+') 
    f_obj.write(ddd + '\n')
    f_obj.close()
    
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
while queue:
    url = queue.popleft()
    visited |= {url}
    ll = '已经抓取： ' + str(cnt) + '    正在抓取<----- ' + url
    saveFile(ll)
    cnt += 1
#     urlop = urllib.request.urlopen(url,timeout=2)
    oper = makeMyOpener()
    urlop = oper.open(url, timeout = 2)
    
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue
    
    linkre = re.compile('href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            mm = '加入队列 -----> ' + x
            saveFile(mm)
    
    
    
    














