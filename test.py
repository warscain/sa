#!/usr/bin/env python
# -*- coding: utf-8 *-*

import shutil
import os
import time
import stat


print os.path.splitext('/home/lucifer/dest.cc')
#('/home/lucifer/dest', '.cc')
print os.path.split('/home/lucifer/dest.cc')
#('/home/lucifer', 'dest.cc')
#print os.path.splitdrive('C:/asa\ddd.cc') 暂时没弄出来分割路径名 path 到一个(drive, tail) 对中，drive 是每个驱动器的说明或空字符串。在系统上不使用驱动器说明的，drive 将一直是空字符。在所有情况中，drive + tail 将和 path 相同。1.3版本中的新特性。 

print os.path.join('/home/lucifer/', 'ddd.cc')

#os.makedirs(name, mode)
#os.mkdir(path)
#os.remove(path)
#os.removedirs(name)
#os.rmdir(path)

print os.listdir('/') #不递归
print os.getcwd()
print os.getcwdu()

print os.getgroups()
print os.geteuid()
#root@lucifer:~# id lucifer
#uid=1000(lucifer) gid=1000(lucifer) 组=1000(lucifer),4(adm),24(cdrom),30(dip),46(plugdev),109(lpadmin),124(sambashare)

print os.getloadavg()
#print os.getlogin()
#>>> import os
#>>> os.getlogin()
#'lucifer'

#st= os.stat('/home/lucifer')
#print st
#def dump(st):
#    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
#    print "- size:", size, "bytes"
#    print "- owner:", uid, gid
#    print "- created:", time.ctime(ctime)
#    print "- last accessed:", time.ctime(atime)
#    print "- last modified:", time.ctime(mtime)
#    print "- mode:", oct(mode)
#    print "- inode/dev:", ino, dev

#dump(st)

fh = open('aaa', 'r')
print os.fstat(fh.fileno())
print os.stat('aaa')  #与上面功能类似 上面的是读取打开的文件的stat
#####################################################3333333333333333333
#infile = "samples/sample.jpg"
#outfile = "out.jpg"
#
## copy contents
#fi = open(infile, "rb")
#fo = open(outfile, "wb")
#
#while 1:
#    s = fi.read(10000)
#    if not s:
#        break
#    fo.write(s)
#
#fi.close()
#fo.close()
#st = os.stat(infile)
#os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
#os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))
#
#print "original", "2=>"
#print "mode", oct(stat.S_IMODE(st[stat.ST_MODE]))
#print "atime", time.ctime(st[stat.ST_ATIME])
#print "mtime", time.ctime(st[stat.ST_MTIME])
#
#print "copy", "=>"
#st = os.stat(outfile)
#print "mode", oct(stat.S_IMODE(st[stat.ST_MODE]))
#print "atime", time.ctime(st[stat.ST_ATIME])
#print "mtime", time.ctime(st[stat.ST_MTIME])
###########################################################################################

#print os.utime(path, (atime, mtime)

#os.chmod(path, mode)
#os.chown(path, uid, gid)

#import os
#
#if os.name == "nt":
#    command = "dir"
#else:
#    command = "ls -l"
#
#os.system(command)

































