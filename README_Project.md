# AliPythonDataAnalysis
这个项目为2020年3月初-5月初在阿里远程实习的实习内容总结
    
## 课题涉及的实验任务梳理总结
### 数据获取方面：
- 网站爬虫(爬取json格式的数据)：
    * 静态网站的爬虫：Week1/spider_chenglong_poster/spider_douban_posters.py
    * 动态网站的爬虫（主要是时间戳的处理与设置）: Week6_7/attempt2/spider_tencent1.py
- selenium，web自动化:
    * selenium，web自动化、使用 xpath或者 css selector 获取数据: Week2/weibo_auto.py
### 数据挖掘算法原理：
- 数据处理：matplotlib, numpy, pandas,
- 机器学习算法：
    * 分类问题：KNN, 朴素贝叶斯，支持向量机，决策树，k-means聚类算法，逻辑斯谛回归， 集成学习算法（随机森林、xgboost）
    * 回归问题：线性回归，岭回归，逻辑斯谛回归
- 深度学习算法
### 数据处理、分析（调参）、预测与可视化实战：
- KNN: Week2/KNN_classifier2.py
- 朴素贝叶斯、决策树、SVM支持向量机：Week3/MultipleAlgorithms_WNR.py
- SVM支持向量机、Logistic回归、随机森林、Gradient Boosting、AdaBoost：Week4/huabei_weiyue.py
- 随机森林、AdaBoost、XGBoost：Week5/huabei_fs1.py
### 面试准备：
- 常见PYTHON问题：机器学习算法基础/Python_常见问题集锦、 Week1/add_three_nums_sum_to_0.py
- SVM参数更新的数学推导：Week3/svm参数推导.pdf
- 数据挖掘面经：机器学习算法基础/数据挖掘面经.md

### 系统学习掌握人工智能机器学习算法基础
    https://www.bilibili.com/video/BV1a7411d7fk
# 网络下载源的问题
这个正常步骤，在很多时候并不能安装成功，多数是因为网络被限制的原因，在这里提供一种方法，可以解决大部分情况下的安装问题，那就是修改下载来源。
方法是在“Manage Repositories”中，修改数据来源，默认的是“https://pypi.python.org/simple”，我们可将其替换为如下的几个数据来源，这些都是国内的pip镜像：
清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里：http://mirrors.aliyun.com/pypi/simple/
豆瓣：http://pypi.douban.com/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
中国科学技术大学：http://pypi.mirrors.ustc.edu.cn/

Homebrew 使用国内镜像 https://blog.csdn.net/iroguel/article/details/93481795
Mac HomeBrew国内镜像安装方法    https://blog.csdn.net/weixin_34067980/article/details/88008241
        cd "$(brew --repo)"
        git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git
        cd "$(brew --repo)/Library/Taps/homebrew/homebrew-cask"
        echo 'export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.aliyun.com/homebrew/homebrew-bottles' >> ~/.bash_profile

大数据人才推荐系统 Talent RADAR  http://tech.it168.com/a2013/0805/1517/000001517009.shtml
