# 1 任务说明：
- 下面我们再来探索一个非常实际而又尚未有太多人关注的数据分析任务， 这个任务没有标准解决方案，并且包括数据采集都要独立完成。
问题起源于现在互联网的两个现象产品MOOC(massive open online courses)和JobHunting。参加MOOC的人，很多都是抱着找工作的目的。
如何帮这些人找到合适的工作呢，手动的话当然是在JobHunting网站上找，但是借助数据分析AI技术，我们可以自动为这些人提供就业建议。
如果把这个问题做的足够的好，解决方案甚至可以商业化。
- 这个问题比较复杂，首先没有大规模的标签，所以这个问题不是一个supervised problem，你可以将改问题视作一个weak supervision. 
复杂问题首先需要比较好的问题定义，我们首先要做的是形式化定义学习任务，你试着研究一下这个问题，尝试给个数学定义。
- 请注意， 这件事情复杂度相当高， 请你自己考虑定义，不要给一个笼统的粗糙的没有可行性的定义
## 简要指导：
- 如何做？首先你得去了解MOOC和jobHunting*本质上*是啥东西，里面有哪些东西可以用来作为特征 如何用形式化的数学语言去表示 这是做一个分析任务开头必须做的事情。

# 2 初步理解与分析：
## 思路：
### 2.1 对MOOC用户属性的研究：
- MOOC的特点：规模大；开放免费；在线教育；课程资源：基础教育的延伸、技能型和针对性更强；
- MOOC用户行为分析：
    * 用户基本信息分析：用户类型（学生、在职）、年龄、性别、学历水平、当前住址、期望就业城市、职业规划水平
        ** 得出用户的职业期望的属性画像
    * 用户学习行为数据：学习目的（兴趣爱好、技能提升）、学习总时间投入、每周学习平均花费时间、选修课时数量、课程模块平均完成程度、课程平均成绩、
        ** 得出用户的实际水平属性画像 
### 2.2 对求职网站的招聘信息研究：
- 招聘方的基本信息：招聘公司的性质（民营、国企，外企、上市公司、其他组织）、公司规模
    ** 反馈给用户了解的公司属性画像
- 招聘内容分析：岗位地点、学历要求、工作经验要求、专业技能知识要求、业务能力要求、薪资福利待遇
    ** 反馈给用户了解的岗位招聘属性画像
### 2.3 智能就业信息推荐模块的设计
- MOOC用户画像 与 企业招聘方的招聘岗位画像：进行智能匹配
    * 针对匹配相似度很高的招聘信息，则给予该MOOC用户相应的招聘信息推送，并提供相应招聘信息的建议及服务。

## 数据源：Canvas Network开放数据集
- Massively Open Online Course for Educators (MOOC-Ed) network dataset：
    * https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/ZZH3UB

## 获取数据的思路：
- MOOC 用户基本信息、课程学习记录：
- 招聘网站信息爬取：岗位招聘信息

## 数据分析的思路：
- 根据用户的实际水平属性画像  -> 构造用户标签库，
- 再结合公司招聘岗位信息的属性画像 -> 自动对比分析用户的职位的匹配度 -> 从而得到该用户对某职位的应聘竞争力指数


# 参考来源：
- 基于Canvas Network开放数据集的MOOC学习分析  http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=bjgbdsdxxb201701006
- 基于文本挖掘的网络招聘信息分析   http://www.wanfangdata.com.cn/details/detail.do?_type=degree&id=D01675854
- 基于大数据的高校智能就业平台建设与应用   http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=xdjyjs202002017
- MOOC学习者特征聚类分析研究综述 http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=zgycjy201807002

- 爬取慕课网上的用户学习数据 https://www.pythonheidong.com/blog/article/147015/
- 爬取慕课网用户学习记录   https://www.imooc.com/article/277641     
- 拉勾网招聘数据爬取（公布源码）https://blog.csdn.net/weixin_41666747/article/details/82724831


