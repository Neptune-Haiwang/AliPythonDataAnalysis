# 问题定义

- 需求：针对特定工作岗位，推荐给用户最相关的一些课程
- 需求解释：
    * 职位招聘信息集合 J: 从每个 job 的描述中提取N个关键词
    * 课程信息集合 C:  从每个课程course 的描述中提取M个关键词
    * 找到一个预测函数 F(J, C) -> Y, 用来预测 某个course是否与某个job相关。 二分类取值。1代表相关，0代表其他。







# 参考资源：
- 4个方面，系统总结个性化推荐系统  http://app.myzaker.com/news/article.php?pk=5a2de8f1d1f149576600003e
- python 读写csv文件（创建，追加，覆盖）  https://blog.csdn.net/lwgkzl/article/details/82147474
- 爬虫！教你用python里的json分分钟爬取腾讯招聘动态网站求职信息！(结构化数据) https://blog.csdn.net/Tianxuancsdn/article/details/105130683
- 使用 lxml 中的 xpath 高效提取文本与标签属性值 https://www.cnblogs.com/hhh5460/p/5079465.html
- Python爬虫之Xpath语法  https://www.cnblogs.com/lone5wolf/p/10905339.html
