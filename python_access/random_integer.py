#!/usr/bin/python2.7
#-*- coding:utf-8 -*-
#用于生成随机mac地址

import random

grandmac = ""
randmac_txt = file('randmac.txt', 'w')

for n in range(1, 10):
    x = []
    for i in range(1, 7):
        randnum = ''.join(random.sample('0123456789abcdef', 2))
        x.append(str(randnum))
    randmac = ":".join(x)
    grandmac += randmac
    grandmac += "\n"
print >> randmac_txt, grandmac
randmac_txt.close()

