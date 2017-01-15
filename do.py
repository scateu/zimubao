#-*- coding: utf8
import pysrt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()


## 初始化单词库

dictbook = open('dictionary/GRE.txt','r').read().splitlines()
dictionary = {}

for d in dictbook:
    l = d.split()
    dictionary[l[0].lower()] = l[-1]

## PySRT
subs = pysrt.open(args.filename)

for i in subs:
    #print i.text
    target_words = [ w for w in i.text.lower().split() if dictionary.has_key(w) ]
    i.text = ""
    for t in target_words:
        print t
        i.text += "%s : %s\n"%(t, dictionary[t].decode('utf8'))

subs.save(args.filename.replace(".srt",".filtered-zimubao-GRE.srt"))


## TODO: 动词变形什么的怎么办?
