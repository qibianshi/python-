import re


ret = re.search(r"\d+", "阅读次数为9999").group()
# ret.group()
print(ret)

ret1 = re.findall(r"\d+", "阅读次数：999,点赞数：888")
print(ret1)

ret2 = re.sub(r"<.*>\d*、*", "", """<div class="job-detail">
        职位职责：
<br>1、负责网页信息和APP数据抽取、清洗、消重、数据结构化等工作；
<br>2、维护现有的数据处理代码并优化。
<br>
<br>职位要求：
<br>1、本科及以上学历，每周能实习4天或以上，连续实习3个月以上；
<br>2、优秀的编码能力，有良好的设计模式、数据结构和算法功底；
<br>3、掌握 golang/java/c++/php/python中的一种，对编程有强烈的热情；
<br>4、有求知欲，认真负责，乐于协作。
        </div>""")
print(ret2)
