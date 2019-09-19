#coding=utf-8

from pyhanlp import *
from collections import Counter

with open("./171160.txt","r",encoding="utf-8") as f:
    txt=f.read()

nlp=HanLP.newSegment().enableNameRecognize(True)

doc=nlp.seg(txt)

c=Counter()

for w in doc:
    if w.toString().find("nr")>=0:
        ww=w.toString()
        name=ww.split("/")[0]
        c[name]+=1
print(c.most_common(50))
