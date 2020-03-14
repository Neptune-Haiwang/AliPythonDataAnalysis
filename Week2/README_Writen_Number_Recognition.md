### 任务要求与任务分解 - 初步分析
    
    1。手写数字识别的任务 可以用python的sklearn
    2。 输入：训练集图片 
        算法理解：按每个像素点 处理成矩阵形式？？然后丢给 算法模型进行训练
        输出：输出的预测数字结果
    3。算法流程分析：这是一个识别分类的算法问题
        * 获得数据：数据采集
        * 数据预处理：理解数据，清洗数据，检查数据的完整性
        * 进行分类：模型评估（把测试集丢给 训练好的模型 检验 预测的准确率，要防止过拟合问题），模型再训练，修改参数，提高精度
    4。 要求你变化 KNeighborsClassifier 的默认参数看看预测效果有没有变化：
        * 试下不同的参数组合 用python matplotlib画图看看
        
### KNN 算法原理

    1。k-近邻（k-Nearest Neighbour，简称KNN），常用于有监督学习。
    2。核心思想：根据你的'邻居'来推断你的类别
        * 整个计算过程分为三步：
            A.计算待分类物体与其他物体之间的距离；
            B.统计距离最近的 K 个邻居；
            C.对于 K 个最近的邻居，它们属于哪个分类最多，待分类物体就属于哪一类
    3。定义：如果一个样本 x 在特征空间中的 K 个最相似的（即特征空间中最邻近）的样本大多属于类别A, 则该样本 x 也属于类别A.
    4。如何确定谁是邻居：一般用欧式距离
        * 欧式距离：平方差距离
        * 曼哈顿距离：绝对值距离
        * 闵可夫斯基距离：通用形式
    5。KNN分类算法的计算过程：
        * 计算待分类点与已知类别的点之间的距离
        * 按照距离递增次序排序
        * 选取与待分类点距离最小的K个点
        * 确定前K个点所在类别的出现次数
        * 返回前K个点出现次数最高的类别作为待分类点的预测分类
    
    6。 注意问题：
        * 把一个物体表示成向量/矩阵；
        * 计算两个物体之间的距离/相似度；距离度量，特征空间中样本点的距离是样本点间相似程度的反映
        * K 值过小（例 K = 1）：容易受到异常点的影响；    K 值过大：容易受到样本不均衡的影响
    7。数据处理：
        * 无量纲化：把不同规格的数据转换到同一规格：标准化
    
    8。 API:    
                from sklearn.neighbors import KNeighborsClassifier
                sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, algorithm='auto')
    9。算法步骤：
        * 获取数据  from sklearn.datasets import
        * (数据预处理)   from sklearn.preprocessing import
        * 数据集划分 from sklearn.model_selection import train_test_split                 
        * 特征工程：标准化、（降维） from sklearn.preprocessing import
        * KNN预估器流程  from sklearn.neighbors import
        * 算法模型评估    .predict    .score      

### KNeighborsClassifier 的参数设置与变化

    1。KNeighborsClassifier(n_neighbors=5, weights=‘uniform’, algorithm=‘auto’, leaf_size=30)
        * n_neighbors：即 KNN 中的 K 值，代表的是邻居的数量。
                K 值如果比较小，会造成过拟合。如果 K 值比较大，无法将未知物体分类出来。一般我们使用默认值 5。
        * weights：是用来确定邻居的权重，有三种方式：
                weights=uniform，代表所有邻居的权重相同；
                weights=distance，代表权重是距离的倒数，即与距离成反比；
                自定义函数，你可以自定义不同距离所对应的权重。大部分情况下不需要自己定义函数。
        * algorithm：用来规定计算邻居的方法，它有四种方式：
                algorithm=auto，根据数据的情况自动选择适合的算法，默认情况选择 auto；
                algorithm=kd_tree，也叫作 KD 树，是多维空间的数据结构，方便对关键数据进行检索，不过 KD 树适用于维度少的情况，一般维数不超过 20，如果维数大于 20 之后，效率反而会下降；
                algorithm=ball_tree，也叫作球树，它和 KD 树一样都是多维空间的数据结果，不同于 KD 树，球树更适用于维度大的情况；
                algorithm=brute，也叫作暴力搜索，它和 KD 树不同的地方是在于采用的是线性扫描，而不是通过构造树结构进行快速检索。当训练集大的时候，效率很低。
        * leaf_size：代表构造 KD 树或球树时的叶子数，默认是 30，调整 leaf_size 会影响到树的构造和搜索速度。
                创建完 KNN 分类器之后，我们就可以输入训练集对它进行训练，
                这里我们使用 fit() 函数，传入训练集中的样本特征矩阵和分类标识，会自动得到训练好的 KNN 分类器。
                然后可以使用 predict() 函数来对结果进行预测，这里传入测试集的特征矩阵，可以得到测试集的预测分类结果。
    2. 四个参数对 KNeighborsClassifier 算法预测准确率的影响如下：
        * （通过 matplotlib画图找到的规律）图：matplotlib分析KNN的超参数对KNN预测准确率的影响.png
        * n_neighbors 影响最大，训练集的准确率随 n_neighbors参数变大而减小；但测试集的准确率在n_neighbors 选择 3 时 达到最好
        * weights参数 选择 distance 时 训练集准确率最高；但对于测试集，distance 与 uniform 几乎没区别
        * algorithm参数和leaf_size在训练集和测试集上区别也都不大
        
 
### 参考资源
    
    1。 【黑马程序员】python机器学习-视频教程：https://www.bilibili.com/video/av39137333?p=21
    2。 查看neighbors大小对K近邻分类算法预测准确度和泛化能力的影响： https://www.cnblogs.com/yszd/p/9298214.html
    3。用Python中的matplotlib画出一个3行2列的饼图：https://blog.csdn.net/qq_33221533/article/details/81568244
