# _*_ coding:utf-8 _*_

import urllib.request

# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read())

values = {'username':'w224278096','password':'swangohaos880611'}
data = urllib.parse.urlencode(values)
url = 'http://passport.csdn.net/account/login'
geturl = url + "?"+data
re = urllib.request.urlopen(geturl).read()
re = re.decode()
print(re)