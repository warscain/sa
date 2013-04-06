#!/usr/bin/env python
# -*- coding: utf-8 *-*

fh_r = open('/home/lucifer/Download/RouterCfm.cfg', 'r')
fileall = fh_r.readlines()
fileall.sort()
print fileall
fh_w = open('tenda', 'w')
for line in fileall:
    print line
    fh_w.write(line)
fh_w.close()