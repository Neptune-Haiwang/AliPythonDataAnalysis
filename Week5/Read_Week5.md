# 任务说明
1。新的任务我们来做一个蚂蚁金服中借呗额度欺诈的问题， 
2。数据集包括了 2015 年 9 月份两天时间内的交易数据，284807 笔交易中，一共有 492 笔是欺诈行为。
3。输入数据一共包括了 28 个特征 V1，V2，……V28 对应的取值，以及交易时间 Time 和交易金额 Amount。
4。为了保护数据隐私，我们不知道 V1 到 V28 这些特征代表的具体含义，只知道这 28 个特征值是通过 PCA 变换得到的结果。
5。另外字段 Class 代表该笔交易的分类，Class=0 为正常（非欺诈），Class=1 代表欺诈。
6。我们的目标是针对这个数据集构建一个信用卡欺诈分析的分类器。还是通过加载数据，准备数据和分类阶段这三个步骤去做本次项目的分析吧

# 解决数据类别不平衡问题
1。本次任务中 二分类问题 样本极为不均衡
2。如何解决：
3。评价指标角度：
        不要只看Accuracy：Accuracy可以说是最模糊的一个指标了，因为这个指标高可能压根就不能代表业务的效果好，
        在实际生产中，我们可能更关注precision/recall/mAP等具体的指标，具体侧重那个指标，得结合实际情况看。
4。从算法角度：
        选择对数据倾斜相对不敏感的算法。如树模型
        集成学习（Ensemble集成算法）：
                首先从多数类中独立随机抽取出若干子集，将每个子集与少数类数据联合起来训练生成多个基分类器，
                再加权组成新的分类器，如加法模型、Adaboost、随机森林等。
        将任务转换成异常检测问题。
                譬如有这样一个项目，需要从高压线的航拍图片中，将松动的螺丝/零件判断为待检测站点，即负样本，其他作为正样本，
                这样来看，数据倾斜是非常严重的，而且在图像质量一般的情况下小物体检测的难度较大，
                所以不如将其转换为无监督的异常检测算法，不用过多的去考虑将数据转换为平衡问题来解决。

# 集成学习：自助聚合bagging、提升法boosting 、堆叠法stacking
1。何为集成方法？
        集成学习是一种机器学习范式。在集成学习中，我们会训练多个模型（通常称为「弱学习器」）解决相同的问题，并将它们结合起来以获得更好的结果。
        最重要的假设是：当弱模型被正确组合时，我们可以得到更精确和/或更鲁棒的模型。
        集成方法的思想是通过将这些弱学习器的偏置和/或方差结合起来，从而创建一个「强学习器」（或「集成模型」），从而获得更好的性能。
2。组合弱学习器：很重要的一点是：我们对弱学习器的选择应该和我们聚合这些模型的方式相一致。
        如果我们选择具有低偏置高方差的基础模型，我们应该使用一种倾向于减小方差的聚合方法；
        而如果我们选择具有低方差高偏置的基础模型，我们应该使用一种倾向于减小偏置的聚合方法。

如何组合这些模型的问题？
# 偏差和方差
        广义的偏差（bias）描述的是预测值和真实值之间的差异，方差（variance）描述距的是预测值作为随机变量的离散程度
        模型的偏差和方差：bagging和stacking中的基模型为强模型（偏差低方差高），boosting中的基模型为弱模型。

2.1 自助聚合bagging：该方法通常考虑的是同质弱学习器，相互独立地并行学习这些弱学习器，并按照某种确定性的平均过程将它们组合起来。 
        Bagging是Bootstrap Aggregating的缩写。
        Bagging是为了得到泛化能力强的集成，因而就需要让各个子学习器之间尽可能独立，
        但是如果将样本分为了不同的不重合子集，那么每个基学习器学习的样本就会不足。
        所以它采用一种自助采样的方法（boostrap sampling）
                每次从数据集中随机选择一个subset，然后放回初始数据集，
                下次取时，该样本仍然有一定概率取到。然后根据对每个subset训练出一个基学习器，
                然后将这些基学习器进行结合。对于分类任务可以通过vote来输出结果，回归任务可以求平均值。
        Bagging的代表是Random Forest，RF是在决策树作为基学习器通过Bagging思想建立的。
                Random Forest是一种基于Bagging思想的Ensemble learning方法，它实际上就是Bagging + 决策树。
                Random Forest可以用来做分类也可以做回归，
                        做分类时最后多棵树的分类器通过voting来决定分类结果；
                        做回归时，由多棵树预测值的averaging来决定预测结果。
     
2.2 提升法boosting：该方法通常考虑的也是同质弱学习器。它以一种高度自适应的方法顺序地学习这些弱学习器（每个基础模型都依赖于前面的模型），并按照某种确定性的策略将它们组合起来。
        Boosting是一种将弱学习器转换为强学习器的算法，
        它的机制是：
                先从初始训练集训练出一个基学习器，
                然后根据基学习器的表现对训练样本进行调整，使得先前基学习器做错的训练样本在后续的训练中得到更多的关注，
                然后基于调整后的样本分布来训练下一个基学习器。
        Boosting的代表是Adam Boosting。
                Adaboost是Boosting算法中的代表，它的思想也便是基于Boosting思想的。
                在adaboost的运算过程中，一开始在训练样本时，为每个子样本赋予一个权重，一开始这些权重都是相等的，
                然后在训练数据集上训练出一个弱分类器，并计算这个弱分类器在每个子样本上的错误率，
                在第二次对这同一数据集进行训练时，将会根据分类器的错误率对子数据集中各个权重进行调整，分类正确的权重降低，分类错误的权重上升，这些权重的总和不变。
                最终得到的分类器会基于这些训练的弱分类器的分类错误率来分配不同的决定系数，从而使权重更新时，错误样本具有更高的权重。
                最后以此来更新各个样本的权重，直至达到迭代次数或者错误率为0。所以Adaboost会对那些影响准确率的数据额外关注，从而会降低bias，而导致overfit。

2.3 堆叠法stacking：该方法通常考虑的是异质弱学习器，并行地学习它们，并通过训练一个「元模型」将它们组合起来，
                并通过训练一个「元模型」将它们组合起来，根据不同弱模型的预测结果输出一个最终的预测结果。
        stacking是一种将弱学习器集成进行输出的策略，
        其中，在stacking中，所有的弱学习器被称作0级（0 level）学习器，他们的输出结果被一个1级（1 level）学习器接受，然后再输出最后的结果。
        这是实际上是一种分层的结构，前面提到的就是一种最基本的二级Stacking。
        另外，在bagging或者boosting中，所有的弱学习器一般都要求是相同的模型，如决策树，而stacking中可以是不同的模型，如KNN、SVM、LR、RF等。
        
2.4 bagging 的重点在于获得一个方差比其组成部分更小的集成模型，
    而 boosting 和 stacking 则将主要生成偏置比其组成部分更低的强模型（即使方差也可以被减小）。
2.5 我现在对集成学习的三种模式的理解是：
    自助聚合bagging：（并行集成）是为了得到泛化能力强的集成，因而就需要让各个子学习器之间尽可能独立, 
    提升法boosting：（序列集成）是一种将弱学习器转换为强学习器的算法, 根据基学习器的表现对训练样本进行调整，然后基于调整后的样本分布来训练下一个基学习器。
    堆叠法stacking： 考虑的是异质弱学习器，并行地学习它们、并通过训练一个「元模型」将它们组合起来，根据不同弱模型的预测结果输出一个最终的预测结果。

# 进一步探索
1。随机森林的剪枝：集成学习在实践中的训练效果很好  如果在测试集中的表现都是100% 那应该是过拟合了 考虑一下剪枝 
    * n_estimators：这是森林中树木的数量，即基评估器的数量。n_estimators越大，模型的效果往往越好。
    * max_features：决策树划分时考虑的最大特征数。max_features 值越大，模型学习能学习到的信息越多，越容易过拟合。
    * max_depth：决策树最大深度。常用的可以取值10-100之间。值越大，决策树越复杂，越容易过拟合。
    * min_samples_split：内部节点再划分所需最小样本数。值越大，决策树越简单，越不容易过拟合。
    * min_samples_leaf：叶子节点最少样本数。值越大，叶子节点越容易被被剪枝，决策树越简单，越不容易过拟合。
    * max_leaf_nodes: 最大叶子节点数。值越小，叶子节点个数越少，可以防止过拟合。
2。Adaboost剪枝:
    * n_estimators:基分类器提升（循环）次数，默认是50次，这个值过大，模型容易过拟合；值过小，模型容易欠拟合。
    * learning_rate:学习率，表示梯度收敛速度，默认为1，如果过大，容易错过最优值，如果过小，则收敛速度会很慢
    * algorithm:boosting算法，也就是模型提升准则，有两种方式SAMME, 和SAMME.R两种，默认是SAMME.R，两者的区别主要是弱学习器权重的度量。
            SAMME是对样本集预测错误的概率进行划分的，SAMME.R是对样本集的预测错误的比例，即错分率进行划分的，默认是用的SAMME.R。 
    * random_state: 随机种子设置

3。xgboost 
    3.1 传统的GBDT，(gradient boosting decision tree)也就是梯度提升决策树:
            这是一种基于树的集成算法.多棵树的集合就构成了GBDT。其实GBDT是对残差的拟合.
            GBDT的目标函数是预测值和真实值差的累加，也就是误差累加，可以看出每一步计算都依赖于上面所有步的误差，效率比较低
    3.2 xgboost特点：
        3.2.1 传统GBDT以CART作为基分类器，xgboost还支持线性分类器，
                这个时候xgboost相当于带L1和L2正则化项的逻辑斯蒂回归（分类问题）或者线性回归（回归问题）。
            -- 可以通过booster [default=gbtree]设置参数:gbtree: tree-based models/gblinear: linear models
        3.2.2 传统GBDT在优化时只用到一阶导数信息，xgboost则对代价函数进行了二阶泰勒展开，同时用到了一阶和二阶导数。
                顺便提一下，xgboost工具支持自定义代价函数，只要函数可一阶和二阶求导。
            -- 对损失函数做了改进（泰勒展开，一阶信息g和二阶信息h）
        3.2.3 xgboost在代价函数里加入了正则项，用于控制模型的复杂度。
                正则项里包含了树的叶子节点个数、每个叶子节点上输出的score的L2模的平方和。
                从Bias-variance tradeoff角度来讲，正则项降低了模型variance，使学习出来的模型更加简单，防止过拟合，
                这也是xgboost优于传统GBDT的一个特性 
            -- 正则化包括了两个部分，都是为了防止过拟合，剪枝是都有的，叶子结点输出L2平滑是新增的。
        3.2.4 shrinkage and column subsampling
                shrinkage缩减类似于学习速率，在每一步tree boosting之后增加了一个参数n（权重），通过这种方式来减小每棵树的影响力，给后面的树提供空间去优化模型。
                column subsampling列(特征)抽样，说是从随机森林那边学习来的，防止过拟合的效果比传统的行抽样还好（行抽样功能也有），并且有利于后面提到的并行化处理算法。
        3.2.5 split finding algorithms(划分点查找算法)
                split finding algorithms(划分点查找算法)
                approximate algorithm— 近似算法，提出了候选分割点概念，先通过直方图算法获得候选分割点的分布情况，然后根据候选分割点将连续的特征信息映射到不同的buckets中，并统计汇总信息。
                Weighted Quantile Sketch—分布式加权直方图算法
                可并行的近似直方图算法。树节点在进行分裂时，我们需要计算每个特征的每个分割点对应的增益，即用贪心法枚举所有可能的分割点。
                当数据无法一次载入内存或者在分布式情况下，贪心算法效率就会变得很低，所以xgboost还提出了一种可并行的近似直方图算法，用于高效地生成候选的分割点。
        3.2.6 对缺失值的处理。对于特征的值有缺失的样本，xgboost可以自动学习出它的分裂方向。 
        3.2.7 Built-in Cross-Validation（内置交叉验证)
        3.2.8 continue on Existing Model（接着已有模型学习）
        3.2.9 High Flexibility（高灵活性）
        3.2.10 并行化处理 —系统设计模块,块结构设计等   
3.3 模型参数
    * max_depth:int |每个基本学习器树的最大深度，可以用来控制过拟合。典型值是3-10
    * learning_rate=0.1：即是eta，为了防止过拟合，更新过程中用到的收缩步长，使得模型更加健壮。典型值一般设置为：0.01-0.2。
    * n_estimators=100,估计器的数量
    * objective：定义学习任务及相应的学习目标，可选目标函数如下：
            “reg:linear”          —— 线性回归
        　　“reg:logistic”        —— 逻辑回归 
        　　“binary:logistic”    —— 二分类的逻辑回归问题，输出为概率
        　　“binary:logitraw”  —— 二分类的逻辑回归问题，输出的结果为wTx            
        　　“count:poisson”   —— 计数问题的poisson回归，输出结果为poisson分布。在poisson回归中，max_delta_step的缺省值为0.7。(used to safeguard optimization)            
        　　“multi:softmax”    —— 让XGBoost采用softmax目标函数处理多分类问题，同时需要设置参数num_class（类别个数）。返回预测的类别(不是概率)。            
        　　“multi:softprob”   —— 和softmax一样，但是输出的是ndata * nclass的向量，可以将该向量reshape成ndata行nclass列的矩阵。每行数据表示样本所属于每个类别的概率。            
        　　“rank:pairwise”   —— set XGBoost to do ranking task by minimizing the pairwise loss
    * booster: default="gbtree"，可选gbtree和gblinear，gbtree使用基于树的模型进行提升计算，gblinear使用线性模型进行提升计算
    * n_jobs：线程数目
    * gamma：0，损失阈值，在树的一个叶节点上进行进一步分裂所需的最小损失减少量，越大，算法越保守。取值范围为：[0,∞]。
            在节点分裂时，只有分裂后损失函数的值下降了，才会分裂这个节点。Gamma指定了节点分裂所需的最小损失函数下降值。
            这个参数的值越大，算法越保守。这个参数的值和损失函数息息相关，所以是需要调整的。
    * min_child_weight=1, 拆分节点权重和阈值，如果节点的样本权重和小于该阈值，就不再进行拆分。在现行回归模型中，这个是指建立每个模型所需要的最小样本数。越大，算法越保守，可以用来减少过拟合。 取值范围为：[0,∞]
    * max_delta_step=0, 每棵树的最大权重估计。如果它的值被设置为0，意味着没有约束；如果它被设置为一个正值，它能够使得更新的步骤更加保守。通常这个参数是没有必要的，但是如果在逻辑回归中类别极其不平衡这时候他有可能会起到帮助作用。把它范围设置为1-10之间也许能控制更新。 取值范围为：[0,∞]
    * scale_pos_weight=1,用来控制正负样本的比例，平衡正负样本权重，处理样本不平衡。在类别高度不平衡的情况下，将参数设置大于0，可以加快收敛。
        
 # 调参数及算法结论：
1。随机森林：准确率 0.99939，训练时间22秒； adaboost：准确率0.99939，训练时间2分钟； XGBoost：准确率0.99961，训练时间2分钟。
2。XGBOOST 调参数过程：
    n_estimators    ：10，15，12，11，11，11
    max_depth       ：80，70，68，67，62，60，55，54，54   
    learning_rate   ：1，1，1
    min_child_weight：1，1，1
    ...

3。代码文件：https://github.com/Neptune-Haiwang/AliPythonDataAnalysis/blob/master/Week5/huabei_fs1.py
   说明文档：https://github.com/Neptune-Haiwang/AliPythonDataAnalysis/blob/master/Week5/Read_Week5.md


# 参考资源
1。【机器学习】如何解决数据不平衡问题 https://www.cnblogs.com/charlotte77/p/10455900.html
2。常用的模型集成方法介绍：bagging、boosting 、stacking    https://www.jianshu.com/p/943f698c0215
3。Ensemble Learning常见方法总结（Bagging、Boosting、Stacking、Blending）   https://blog.csdn.net/FrankieHello/article/details/81664135
4。使用sklearn进行集成学习——理论   https://www.cnblogs.com/jasonfreak/p/5657196.html
5. 集成学习总结 & Stacking方法详解    https://blog.csdn.net/willduan1/article/details/73618677
6. 随机森林sklearn FandomForest，及其调参    https://blog.csdn.net/geduo_feng/article/details/79558572
7. sklearn 集成学习AdaBoostClassifier参数详解   https://blog.csdn.net/JohnsonSmile/article/details/88759761
8。xgboost入门与实战（原理篇） https://blog.csdn.net/sb19931201/article/details/52557382
9。Mac Ananconda Python下载安装 xgboost【可参考多个报错类型】   https://blog.csdn.net/hahameier/article/details/105027178
10. xgboost的sklearn接口和原生接口参数详细说明及调参指点   https://www.cnblogs.com/wzdLY/p/9831282.html
11. 
    Scikit中的特征选择，XGboost进行回归预测，模型优化的实战  https://blog.csdn.net/sinat_35512245/article/details/79668363
    XGboost数据比赛实战之调参篇(完整流程) https://blog.csdn.net/sinat_35512245/article/details/79700029
12. pandas的DataFrame的append方法详细介绍   https://blog.csdn.net/sinat_29957455/article/details/84961936
13. 十分钟AI知识点】pandas最详细教程    https://zhuanlan.zhihu.com/p/99889912