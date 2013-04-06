#!/usr/bin/env python
# -*- coding: UTF-8 *-*


from nntplib import NNTP
n = NNTP('your.nntp.server')
rsp, ct, fst, lst, grp = n.group('comp.lang.python')
rsp, anum, mid, data = n.article('110457')
for eachLine in data:
    print eachLine
From: "Alex Martelli" <alex@...> Subject: Re: Rounding Question
Date: Wed, 21 Feb 2001 17:05:36 +0100
"Remco Gerlich" <remco@...> wrote:
Jacob Kaplan-Moss <jacob@...> wrote in comp.lang.python:
So I've got a number between 40 and 130 that I want to round up to
the nearest 10. That is:

40 --> 40, 41 --> 50, ..., 49 --> 50, 50 --> 50, 51 --> 60
Rounding like this is the same as adding 5 to the number and then
rounding down. Rounding down is substracting the remainder if you were
to divide by 10, for which we use the % operator in Python.
This will work if you use +9 in each case rather than +5 (note that he doesn't
really want rounding -- he wants 41 to 'round' to 50, for ex).
Alex
>>> n.quit()
'205 closing connection - goodbye!'




























