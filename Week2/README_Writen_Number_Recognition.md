### 任务要求与任务分解 - 初步分析
    
    1。手写数字识别的任务 可以用python的sklearn
    2。 输入：训练集图片 
        算法理解：按每个像素点 处理成矩阵形式？？然后丢给 算法模型进行训练
        输出：输出的预测数字结果
    3。算法流程分析：这是一个识别分类的算法问题
        * 获得数据：数据采集
        * 数据预处理：理解数据，清洗数据，检查数据的完整性
        * 进行分类：模型评估（把测试集丢给 训练好的模型 检验 预测的准确率，要防止过拟合问题），模型再训练，修改参数，提高精度
        
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
 
### 参考资源
    
    1。 【黑马程序员】python机器学习-视频教程：https://www.bilibili.com/video/av39137333?p=21
