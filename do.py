#-*- coding: utf8
import pysrt

## 初始化单词库

dictbook = open('dictionary/GRE.txt','r').read().splitlines()
dictionary = {}

for d in dictbook:
    l = d.split()
    dictionary[l[0].lower()] = l[-1]

## PySRT
subs = pysrt.open('House.of.Cards.S01E01.WEBRip.720p.H.264.AAC.2.0-HoC.srt')

for i in subs:
    #print i.text
    target_words = [ w for w in i.text.lower().split() if dictionary.has_key(w) ]
    i.text = ""
    for t in target_words:
        print t
        i.text += "%s : %s\n"%(t, dictionary[t].decode('utf8'))

subs.save('House.of.Cards.S01E01.WEBRip.720p.H.264.AAC.2.0-HoC.filtered-GRE.srt')


## TODO: 动词变形什么的怎么办?

