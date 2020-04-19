# 问题定义

- 需求：针对特定工作岗位，推荐给用户最相关的一些课程
    * 基于岗位招聘就业信息的 MOOC在线课程推荐系统
- 需求解释：
    * 职位招聘信息集合 J: 从每个 job 的描述中提取N个关键词
    * 课程信息集合 C:  从每个课程course 的描述中提取M个关键词
    * 找到一个预测函数 F(J, C) -> Y, 用来预测 某个course是否与某个job相关。 二分类取值。1代表相关，0代表其他。


# TF-IDF与余弦相似性的应用（一）：自动提取关键词
- TF-IDF，最开始用于信息检索
- TF-IDF模型的主要思想是：如果词w在一篇文档d中出现的频率高，并且在其他文档中很少出现，则认为词w具有很好的区分能力，适合用来把文章d和其他文章区分开来。
- 该模型主要包含了两个因素：TF,IDF
    * 词频TF(Term Frequency): 词w在文档d中出现次数count(w, d)和文档d中总词数size(d)的比值：        
        ** TF = count(w, d) / size(d)
    * 逆向文档频率IDF(Inverse Document Frequency): 文档总数N与出现词w的文件数docs(w, D)比值 的对数：
        ** IDF = log(N/ (1 + count(I(w_in_di)|{i=1,2,..N})))  , 加1是为了防止分母为0的情况
    * TF-IDF = TF * IDF (即：词频* 词权)
- 转化为特征选择：对最后的作为选取特征的TF-IDF = max （TF(Ci,t)*IDF） or avg(TF(Ci,t)*IDF) 
- 评价：TF-IDF算法的优点是简单快速，结果比较符合实际情况。缺点是，单纯以"词频"衡量一个词的重要性，不够全面，有时重要的词可能出现次数并不多


# 参考资源：
- 4个方面，系统总结个性化推荐系统  http://app.myzaker.com/news/article.php?pk=5a2de8f1d1f149576600003e

- python 读写csv文件（创建，追加，覆盖）  https://blog.csdn.net/lwgkzl/article/details/82147474
- 爬虫！教你用python里的json分分钟爬取腾讯招聘动态网站求职信息！(结构化数据) https://blog.csdn.net/Tianxuancsdn/article/details/105130683
- 使用 lxml 中的 xpath 高效提取文本与标签属性值 https://www.cnblogs.com/hhh5460/p/5079465.html
- Python爬虫之Xpath语法  https://www.cnblogs.com/lone5wolf/p/10905339.html

- pandas中的dataframe如何找出具有缺失值的行  https://segmentfault.com/q/1010000014210943
- 删除DataFrame中值全为NaN或者包含有NaN的列或行    https://blog.csdn.net/calorand/article/details/53742290
- DataFrame某些列值替换的三种方式  https://blog.csdn.net/weixin_37674494/article/details/82632621?utm_source=blogxgwz9
- 机器学习-nlp-sklearn进行关键词提取（基于tfidf）  https://blog.csdn.net/wangjie5540/article/details/103811651

- 推荐算法 协同过滤sklearn实现    https://blog.csdn.net/yangyang_yangqi/article/details/82782361
