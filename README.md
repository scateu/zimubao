# 字幕宝

把 SRT 字幕里的生词提取出来。 其它见: [商业计划<del>输</del>书](http://scateu.me/2017/01/13/subtitles-cet4.html)。


![DEMO: House of Cards](https://github.com/scateu/zimubao/raw/master/snapshots/House.of.Cards.S01E01.jpg)


|![DEMO: Yes Prime Minister](https://github.com/scateu/zimubao/raw/master/snapshots/Yes.Prime.Minister.S02E08.png) |![DEMO: Yes Prime Minister](https://github.com/scateu/zimubao/raw/master/snapshots/Yes.Prime.Minister.S02E08-2.png) |
|----|----|

示例字幕文件见 `testcase/`, 在线字幕示例: <http://subsmax.com/subtitles-movie/yes-prime-minister>

## Usage

```bash
zimubao.py /path/to/your/subtitles.srt

# batch:
for i in *;do echo $i;zimubao.py "$i";done
```

## TODO

 - [ ] 处理时态 
 - [ ] 复数
 - [ ] 引入牛津词库
 - [ ] 处理ass
 - [ ] 处理mkv内建字幕
 - [ ] 变成web操作
 - [ ] 引入自然语言处理的库,如Word API
 - [X] argparse
 - [ ] argparse: stdin
 - [ ] argparse: 处理多个文件 `*`
 - [ ] publish to pip
 - [X] 处理codec错误的情况，PySRT承.受.不.了: `iconv -f ISO-8859-1 -t utf8`
 - [ ] 一条字幕中的重复单词
 - [ ] 一整个SRT文件中，生词只在第一次出现? (Optional)
 - [ ] 或者根本就不用PySRT，直接全文替换得了....简单方便
 - [ ] 使用过程中: 每一部剧，可以由人工专门生成一个glossary
 - [ ] 支持词组匹配替换
