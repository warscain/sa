#!/usr/bin/env python
# coding=gbk

import httplib2

#h1 = httplib2.Http(".cache")
#response, content = h1.request("http://www.baidu.com/", "GET")



h2 = httplib2.Http()
h2.add_credentials('zhpeng', 'h3HGja,s0')
h2.add_certificate(key='/home/lucifer/Desktop/yourcert.nopass.key', cert='/home/lucifer/Desktop/tcms.engineering.redhat.com', domain='tcms.engineering.redhat.com')
response, content = h2.request("https://tcms.engineering.redhat.com/" )


#h3 = httplib2.Http(ca_certs='/home/lucifer/Desktop/www.alipay.com')
#h3.add_credentials('name', 'password')
#response, content = h3.request("https://www.alipay.com/",
#    "GET",headers={'content-type':'text/plain'} )

for item in response:
    print item, ":", response[item]
print "==============�����ķָ���================"
print content


#status : 200
#content-length : 9777
#content-location : http://www.baidu.com/
#set-cookie : BAIDUID=F2B99BBD8A388E717887533BB8B7BDD4:FG=1; expires=Mon, 07-Jan-43 13:40:42 GMT; path=/; domain=.baidu.com
#expires : Mon, 07 Jan 2013 13:40:42 GMT
#server : BWS/1.0
#connection : Keep-Alive
#-content-encoding : gzip
#cache-control : private
#date : Mon, 07 Jan 2013 13:40:42 GMT
#p3p : CP=" OTI DSP COR IVA OUR IND COM "
#content-type : text/html;charset=gbk
#��http post method��response���õ�cookie��Ȼ��֮�������cookie�������������
#import urllib
#import httplib2
#
#http = httplib2.Http()
#url = 'http://www.example.com/login'
#body = {'USERNAME': 'foo', 'PASSWORD': 'bar'}
#headers = {'Content-type': 'application/x-www-form-urlencoded'}
#response, content = http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
#headers = {'Cookie': response['set-cookie']}
#url = 'http://www.example.com/home'
#response, content = http.request(url, 'GET', headers=headers)
#���ݵĴ��ݿ�����wireshark��׽����������ֱ����firefox�µ�live http headers������Ҳ������linux�µ�GET
#��POST�����(man GET, man POST, man lwp-request) 
