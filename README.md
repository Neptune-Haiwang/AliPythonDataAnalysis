# AliPythonDataAnalysis
    这个项目为2020年3月初-5月初在阿里远程实习的实习内容总结
    
### 现已完成的任务
  
### week1
    * 一个豆瓣爬虫程序：包含对json数据的处理
  
### week2
    * 一个微博机器人：自动登录，自动关注用户，找到某个微博，添加评论，取关用户，自己写微博并发表
    * 用knn算法识别手写数字，调整knn的不同的超参数，并用 matplotlib画图查看参数的变化对算法模型准确率的影响。

### week3
    * 用朴素贝叶斯和SVM再实现同样的手写数字识别，调整参数查看变化
    * 了解更多关于SVM的算法逻辑知识，手写SVM参数推导公式
    
### week4
    * 用SVM和朴素贝叶斯模型 分析 花呗违约率分析的二分类问题

### week5
    * 用集成学习算法 bagging, bossting, stacking 三种模式，对花呗欺诈问题进行判断



# 网络下载源的问题
    这个正常步骤，在很多时候并不能安装成功，多数是因为网络被限制的原因，在这里提供一种方法，可以解决大部分情况下的安装问题，那就是修改下载来源。
    方法是在“Manage Repositories”中，修改数据来源，默认的是“https://pypi.python.org/simple”，我们可将其替换为如下的几个数据来源，这些都是国内的pip镜像：
    清华：https://pypi.tuna.tsinghua.edu.cn/simple
    阿里：http://mirrors.aliyun.com/pypi/simple/
    豆瓣：http://pypi.douban.com/simple/
    华中理工大学：http://pypi.hustunique.com/
    山东理工大学：http://pypi.sdutlinux.org/
    中国科学技术大学：http://pypi.mirrors.ustc.edu.cn/
