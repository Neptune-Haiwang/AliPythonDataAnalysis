# 问题与需求定义：
    - 需求：针对特定工作岗位，推荐给用户最相关的一些课程
        * 基于岗位招聘就业信息的 MOOC在线课程推荐系统
    - 需求解释：
        * 职位招聘信息集合 J: 从每个 job 的描述中提取N个关键词
        * 课程信息集合 C:  从每个课程course 的描述中提取M个关键词
        * 找到一个预测函数 F(J, C) -> Y, 用来预测 某个course是否与某个job相关。 二分类取值。1代表相关，0代表其他。

# 思路与步骤总结
## 1 数据爬取
    - 爬取XX招聘的岗位信息：JSON格式数据的抓取 -> job_title，job_responsibility
    - 爬取XX在线的课程信息：XPATH路径获取属性的文本数据 -> course_name， course_description
## 2 数据处理
### 提取关键词与计算相似度
    - jieba中文分词处理，去掉奇怪符号，去掉停用词，去掉空值，去掉单字，去掉数字
    - 词频统计：两个文本获取的关键词列表丢进一个集合，然后统计两个文本对应的关键词的词频计数，没有就是0，有则统计总出现次数+1， 
    - 计算余弦相似度：根据词频统计得出的词频向量计算向量夹角的余弦值
### 给出推荐结果
    - 根据向量的余弦相似度，进行排序，并给出topN的推荐结果。
## 3 进一步思考
    - 对特定关键词增加权重：比如标题的权重需要增加; 两篇文档都出现相同的词，则权重需要增加
    - 错分样本的再思考：人工选择标记出分错的样本，再把选择的结果丢给模型。然后模型对于分错的样本 Mi 降低相似度。
    （这样做法的另一种意义上就是，如果在备选课程表中有和分错的样本Mi 相似度很高的Ni，二次推荐时就不用把Ni也推荐给我了）

# 参考资源：
    - python 读写csv文件（创建，追加，覆盖）  https://blog.csdn.net/lwgkzl/article/details/82147474
    - 爬虫！教你用python里的json分分钟爬取腾讯招聘动态网站求职信息！(结构化数据) https://blog.csdn.net/Tianxuancsdn/article/details/105130683
    - 使用 lxml 中的 xpath 高效提取文本与标签属性值 https://www.cnblogs.com/hhh5460/p/5079465.html
    - Python爬虫之Xpath语法  https://www.cnblogs.com/lone5wolf/p/10905339.html
    
    - pandas中的dataframe如何找出具有缺失值的行  https://segmentfault.com/q/1010000014210943
    - 删除DataFrame中值全为NaN或者包含有NaN的列或行    https://blog.csdn.net/calorand/article/details/53742290
    - DataFrame某些列值替换的三种方式  https://blog.csdn.net/weixin_37674494/article/details/82632621?utm_source=blogxgwz9
    - 用pandas中的DataFrame时选取行或列  https://blog.csdn.net/wanglingli95/article/details/78887771/
    - 机器学习-nlp-sklearn进行关键词提取（基于tfidf）  https://blog.csdn.net/wangjie5540/article/details/103811651
    
    - 推荐系统学习笔记之四——相似度计算以及权重的重要性 https://blog.csdn.net/qq_35946969/article/details/88233080
