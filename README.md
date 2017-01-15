# 字幕宝

把 SRT 字幕里的生词提取出来。 其它见: [商业计划<del>输</del>书](http://scateu.me/2017/01/13/subtitles-cet4.html)。


![DEMO: House of Cards](https://github.com/scateu/zimubao/raw/master/snapshots/House.of.Cards.S01E01.jpg)
![DEMO: Yes Prime Minister](https://github.com/scateu/zimubao/raw/master/snapshots/Yes.Prime.Minister.S02E08.png)

示例字幕文件见 `testcase/`

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
 - [ ] publish to pip
 - [ ] 处理codec错误的情况，PySRT承.受.不.了
