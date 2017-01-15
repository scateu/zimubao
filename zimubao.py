#!/usr/bin/env python
#-*- coding: utf8
import pysrt
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()


## 初始化单词库

dictbook = open(os.path.join(os.path.dirname(__file__), 'dictionary/GRE.txt'),'r').read().splitlines()
dictionary = {}

for d in dictbook:
    l = d.split()
    dictionary[l[0].lower()] = l[-1]

## PySRT
try:
    subs = pysrt.open(args.filename)
except:
    subs = pysrt.open(args.filename, encoding='iso-8859-1')

for i in subs:
    #print i.text
    target_words = [ w for w in i.text.lower().split() if dictionary.has_key(w) ]
    i.text = ""
    for t in target_words:
        print t
        i.text += "%s : %s\n"%(t, dictionary[t].decode('utf8'))

subs.save(args.filename.replace(".srt",".filtered-zimubao-GRE.srt"), encoding='utf-8')


## TODO: 动词变形什么的怎么办?
