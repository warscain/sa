#!/usr/bin/env python
# coding=gbk

import urllib

#wh1 = urllib.urlopen('http://www.baidu.com')
#wh1 = urllib.urlopen('https://zhpeng:h3HGja,s0@tcms.engineering.redhat.com/plan/6578/test-plan-for-libvirt-features-rhel64#testcases')
##urllib.url
#print wh1.info()
#print wh1.getcode()
#print wh1.geturl()
#print wh1.read()

#wh2 = urllib.urlretrieve('https://zhpeng:h3HGja,s0@tcms.engineering.redhat.com/plan/6578/test-plan-for-libvirt-features-rhel64#testcases', 'aaa.html')
print urllib.quote('http://www/~foo/cgi-bin/s.py?name=joe mama&num=6')
print urllib.quote_plus('http://www/~foo/cgi-bin/s.py?name=joe mama&num=6')
print urllib.unquote('http%3A//www/%7Efoo/cgi-bin/s.py%3Fname%3Djoe%20mama%26num%3D6')
print urllib.unquote_plus('http%3A%2F%2Fwww%2F%7Efoo%2Fcgi-bin%2Fs.py%3Fname%3Djoe+mama%26num%3D6')

aDict = { 'name': 'Georgina Garcia', 'hmdir': '~ggarcia' }
print urllib.urlencode(aDict)
#'name=Georgina+Garcia&hmdir=%7eggarcia'
