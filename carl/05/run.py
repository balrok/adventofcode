#!/usr/bin/env python
# -*- coding: utf-8 -*-


from hashlib import *
id=0
pw="abc%d"
pw="ugkcyxxp%d"
code = ""
code2 = ["_"for i in [0]*16]
while 1:
    h=md5(pw%id).hexdigest()
    if h[:5]=="0"*5:
        code+=h[5]
        q=int(h[5],16)
        code2[int(h[5],16)]=(code2[q],h[6])[code2[q]=="_"]
        print id,h,code,"".join(code2)
        if "_" not in code2[:8]:
            break
    id+=1
print code[:8]
print "".join(code2)[:8]


