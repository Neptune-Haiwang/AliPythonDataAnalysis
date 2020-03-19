### 概率基础回顾
    1。概率的定义：一件事情发生的可能性， P(X) 取值范围为[0,1]
    2。联合概率：包含多个条件，且所有条件同时成立的概率：P(A, B)
    3。条件概率：就是事件A在另外一个事件B已经发生条件下的发生概率：P(A|B)，P(A,C|B)
    4。相互独立：P(A, B) = P(A)P(B) <=> 事件A与事件B相互独立

### 朴素贝叶斯算法
    1。朴素？假设：特征与特征之间是相互独立 ！！！
    2。贝叶斯公式：P(C|W) = P(W|C)P(C) / P(W)  注：W 为给定文档的特征值（频数统计，预测文档提供），C 为文档类别
            推广到一般公式：P(C|F1,F2,...) = P(F1,F2,...|C)P(C) / P(F1,F2,...)  其中 C 可以是不同类别
                    注：P(F1,F2,...)： 为预测文档中，每个词的概率
                       P(C）：每个文档类别的概率（某文档的类别数 / 总文档数量）
                       P(W|C) ：给定类别特征下（被预测文档中出现的词）的概率
    3。朴素贝叶斯算法：朴素 + 贝叶斯
    4。应用场景：文本分类 单词作为特征
    5。拉普拉斯平滑系数：目的：为了防止计算出的分类概率为0：   P(F1|C) = (Ni +a) / (N + am)
            注：a 为指定的系数，一般为1， m 为训练文档中统计出的特征词个数
        
    6。朴素贝叶斯算法流程： 获取数据、划分数据集、特征工程、文本特征抽取、朴素贝叶斯预估器流程、模型评估
    7。朴素贝叶斯算法总结：
        优点：对缺失数据不太敏感，算法也比较简单，常用于文本分类。分类准确度高，速度快
        缺点：由于使用了样本属性独立性的假设，所以如果特征属性有关联时其效果不好

### 文本分类的一个例子

                文档ID        文档中的词                       属于 C = CHINA 类 
    训练集         1    Chinese, Beijing, Chinese                  yes
                  2    Chinese,Chinese, Shanghai                  yes
                  3    Chinese Macao                              yes
                  4    Tokyo, Chinese, Japan                      no
    测试集         5    Chinese Chinese Chinese Tokyo Japan        ?
                  
    P(C|Chinese,Chinese,Chinese,Tokyo,Japan) 
            =  P (Chinese,Chinese,Chinese,Tokyo,Japan|C) * P(C) / P(Chinese,Chinese,Chinese,Tokyo,Japan)    
        
        P (Chinese,Chinese,Chinese,Tokyo,Japan|C) = （P(Chinese|C)^3） * P(Tokyo|C) * P(Japan|C) 
        P(Chinese,Chinese,Chinese,Tokyo,Japan) = (P(Chinese)^3) * P(Tokyo) * P(Japan) = ((6/11)^3) * (1/11) * (1/11)
    * 统一都要加上拉普拉斯平滑系数
        解释：5 + 1 -> 属于 C = CHINA 类的情况下，特征词为 Chinese 的一共有5个；拉普拉斯平滑系数为1*1 = 1
             8 + 6 -> 属于 C = CHINA 类的情况下，总共有8个单词；所有文档下，总共有6种不同的单词 ，即 有6种特征词
        P(C) = 3/4      ：4个文档种，共有3个属于 C = CHINA 类 
        P(Chinese|C) = (5+1)/(8+6) = 6/14 = 3/7
        P(Tokyo|C) = (0+1)|(8+6) = 1/14
        P(Japan|C) = (0+1)|(8+6) = 1/14  
         
    P(非C|Chinese,Chinese,Chinese,Tokyo,Japan) = P (Chinese,Chinese,Chinese,Tokyo,Japan|非C) * P(非C) / P(Chinese,Chinese,Chinese,Tokyo,Japan)  
    

### 参考资源
    1。 【黑马程序员】朴素贝叶斯算法：  https://www.bilibili.com/video/av39137333?p=25