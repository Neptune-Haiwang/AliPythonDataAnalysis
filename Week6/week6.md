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

## 推荐系统的设计实现
- User Profile
    * 主要是用户（注册）信息，以及对用户反馈的信息进行处理，聚合，用于描述用户的特征； 是后续推荐和排序的基石。 
    * 一般情况下，user profile会包含以下具体内容：
        ** 用户兴趣数据
        ** 用户的基础注册信息，背景信息：例如用户出生地，年龄，性别，星座，职业等。这些信息一般从用户注册信息中获取
        ** 用户行为反馈：包括显示的反馈(explicit)和隐藏(implicit)的反馈，
                显示的反馈包括用户的评分，点赞等操作，百度关键词搜索推荐工具上的点赞（正向显示反馈）和垃圾桶（负向显示反馈），淘宝上的评分；
                隐式反馈包括用户的浏览行为，例如在百度关键词搜索推荐上搜过那些词，淘宝上点击了那些页面，在高德上点击了那些POI等
        ** 用户交互偏好：例如用户喜欢使用哪些入口，喜欢哪些操作，以及从这些操作中分析出来的偏好，比如在高德地图上根据用户行为反馈分析出来的用户对美食的偏好：更喜欢火锅，粤菜，还是快餐
        ** 用户上下文信息：这些信息有些是分析出来的，例如在LBS中分析出来的用户的家在哪儿，公司在哪儿，经常活动的商圈，经常使用的路线等
    * user profile经常是一份维护好的数据，在使用的时候，会直接使用该数据，或是将该数据存储在KV系统中，供Online系统实时使用。 
    * 在搜索或是推荐的场景下，每次请求一般只会涉及到一次user profile的KV请求，所以online使用的时候，主要的实现困难是存储，以及快速KV的快速响应。
- 基础挖掘推荐算法 -> 建立user和item的关系
    ** 基础推荐挖掘， 和传统的推荐部分比较类似，主要结合user profile， 挖掘哪些item适合推给哪些user。 
    ** 但仅根据这些挖掘就直接进行推荐是不够的。 真实online推荐场景中， 需要考虑更多其他因素， 例如：相关性，推荐的上下文，CTR预估，以及商业业务规则。
    * Content Based推荐： 按内容推荐，主要的工作是user profile, item profile的提取和维护，然后研究各种相似度度量方法
    * 协同过滤：相当于应用了用户的行为进行推荐（区别于Content based算法），比较经典的算法包括传统的item-based/user-based算法
    * 上下文相关推荐：和传统推荐相比， 考虑更多上下文因素，LBS， 移动场景下使用比较多
    * 基于图的关系挖掘推荐：主要是利用图论原理，根据item,user之间的数据，反馈关联关系，挖掘更深层次的关系进行推荐
    * 在实际应用时，我们经常使用按内容推荐，item-based寻找从感知的角度比较靠谱的结果，使用SVD,SVD++，图关系寻找更深层次的联系结果。
    * 同时在推荐时，会结合很多因素来进行综合排序，例如关键词， 或是LBS中POI的热度等
    ** 算法效果衡量：使用Cross-Validation方式。对于预测Rating准确性主要是用RMSE，或是MA
- Ranking
    * 相关性： item与用户的相关性，这是大多数搜索和推荐任务的基石，
        ** 例如在搜索中判定一个query和一个document的相关性，或是一个query 和 另一个query的相关性，或是在特征比较多的情况下， 一个user 和一个item 记录的相关性。
        ** 实现方式：传统的相似度度量方式、对于文本使用的TF*IDF
        ** 不过很多时候我们需要增加更多维度特征，包括推荐item本身的重要性，例如IDF，Pagerank
    * 推荐的上下文：例如推荐产品的入口，交互方式， 不同的入口，甚至同一入口的不同交互方式， 推荐的结果有可能都需要不一样； 
        ** 在LBS生活服务中， 请求发生的时间， 地点也是推荐需要重点考虑的上下文因素，例如饭点对餐饮item的提权； 异地情况下对酒店等结果的加权等
    * CTR预估：成熟的商业系统都会使用模型来完成CTR预估，或是转化预估
    * 商业业务规则：例如黑白名单，或者强制调权。例如在百度关键词搜索推荐中，某些有比较高变现潜力的词， 就应该加权往前排；



# 参考来源：
- 基于Canvas Network开放数据集的MOOC学习分析  http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=bjgbdsdxxb201701006
- 基于文本挖掘的网络招聘信息分析   http://www.wanfangdata.com.cn/details/detail.do?_type=degree&id=D01675854
- 基于大数据的高校智能就业平台建设与应用   http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=xdjyjs202002017
- MOOC学习者特征聚类分析研究综述 http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=zgycjy201807002

- 爬取慕课网上的用户学习数据 https://www.pythonheidong.com/blog/article/147015/
- 爬取慕课网用户学习记录   https://www.imooc.com/article/277641     
- 拉勾网招聘数据爬取（公布源码）https://blog.csdn.net/weixin_41666747/article/details/82724831

- 一个完整推荐系统的设计实现 https://blog.csdn.net/miner_zhu/article/details/81667971
- 基于物品/用户的协同过滤算法（使用Scikit-learn实现）  https://blog.csdn.net/m0_38045485/article/details/81174685
- 基于sklearn TFIDF模型 的文章推荐算法 https://blog.csdn.net/qq_34333481/article/details/85126228
- 推荐系统系列 - 引导 - 5类系统推荐算法,非常好使,非常全   https://blog.csdn.net/u010670689/article/details/71513133/

- pythonFlask框架学习   https://www.jianshu.com/p/6452596c4edb
- 使用 lxml 中的 xpath 高效提取文本与标签属性值 https://www.cnblogs.com/hhh5460/p/5079465.html
- Python爬虫之Xpath语法  https://www.cnblogs.com/lone5wolf/p/10905339.html
- 爬虫！教你用python里的json分分钟爬取腾讯招聘动态网站求职信息！(结构化数据) https://blog.csdn.net/Tianxuancsdn/article/details/105130683
- python 读写csv文件（创建，追加，覆盖）  https://blog.csdn.net/lwgkzl/article/details/82147474