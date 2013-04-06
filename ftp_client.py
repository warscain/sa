#!/usr/bin/env python
# -*- coding: UTF-8 *-*

# 基础例子
#from ftplib import FTP
#
#f = FTP('192.168.1.100')
#f.login('anonymous', "")
#f.dir()
#f.retrlines('RETR test1')
#f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
#f.quit()

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
        f.quit()
        return

if __name__ == '__main__':
    main()
    
#    我们传了一个回调函数给 retrbinary(),它在每接收到一块二进制数据的时候都
#会被调用。
#这个函数就是我们创建的本地文件对应文件对象的 write 方法。
#在传输结束的时候,
#Python
#解释器会自动关闭这个文件对象,而不会丢失数据。虽然这样方便,但最好还是不要这样做,做为
#一个程序员,
#要尽量做到在资源不再被使用的时候就直接释放,
#而不是依赖其它代码来做释放操作。
#在 这 里 , 我 们 应 该 把 文 件 对 象 保 存 到 一 个 变 量 中 , 如 变 量 loc , 然 后 把 loc.write 传 给
#ftp.retrbinary()方法。

