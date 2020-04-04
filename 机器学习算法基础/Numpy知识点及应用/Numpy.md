# numpy优势：
    1。用于快速处理任意维度的数组：numpy使用ndarray对象来处理多维数组
    2。numpy支持常见的数据和矩阵操作

# ndarray的介绍
    1。numpy中提供了一个N维数据类型ndarray，它描述了相同类型的items的集合
    2。ndarray的优势：
            * 内存块风格：数据与数据的地址是连续的 -> 批量处理数组数据更快
            * ndarray支持并行化运算（向量化运算）-> 当系统有多核心时，numpy则进行并行计算
            * 效率远高于纯python代码 -> numpy底层使用C语言编写，内部解除了GIL全局解释器锁，它对于数组的操作速度不受python解释器的限制。

# ndarray的使用：
    1。ndarray的属性：数组属性反映了数组本身固有的信息。
            属性名字	            属性解释
            ndarray.shape	    数组维度的元组
            ndarray.ndim	    数组维数
            ndarray.size	    数组中的元素数量
            ndarray.itemsize	一个数组元素的长度（字节）
            ndarray.dtype	    数组元素的类型


# 生成随机数组
    1。np.random模块
    2。正态分布： 正态分布是一种概率分布。正态分布是具有两个参数μ和σ的连续型随机变量的分布，
                第一参数μ是服从正态分布的随机变量的均值，：平均值：总和 / 总数
                第二个参数σ是此随机变量的标准差，：标准差：每个值与平均值的差值的平方和，再除以总数，结果再开根号。
                所以正态分布记作N(μ，σ )。
        2.1 正态分布特点：μ决定了其位置（左边，右边），其标准差σ决定了分布的幅度（峰值的高低）。当μ = 0,σ = 1时的正态分布是标准正态分布。
        2.2 标准差与方差的意义：可以理解成数据的一个离散程度的衡量
        2.3正态分布创建方式：
                np.random.randn(d0, d1, …, dn)      功能：从标准正态分布中返回一个或多个样本值
                np.random.normal(loc=0.0, scale=1.0, size=None)     
                                loc 均值（对应着整个分布的中心centre）、
                                scale 标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）、
                                size 输出的shape，默认为None，只输出一个值
                np.random.standard_normal(size=None)    返回指定形状的标准正态分布的数组。
    3。均匀分布：
        np.random.rand(d0, d1, ..., dn) 返回[0.0，1.0)内的一组均匀分布的数。
        np.random.uniform(low=0.0, high=1.0, size=None) 功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
                # 生成均匀分布的随机数
                x2 = np.random.uniform(-1, 1, 100000000)  
        np.random.randint(low, high=None, size=None, dtype='l') 从一个均匀分布中随机采样，生成一个整数或N维整数数组


# 数组的索引、切片
    1。如何索引？ 对象[:, :] -- 先行后列
        1.1 二维数组索引方式：stock_change[0, 0:3] ->获取第一行数据中的 [0， 3) 即前三列的数据
        1.2 三维数组索引方式：a1[0, 0, 1] -> 获取第一个二维数组中的第一个一维数组中的第二个元素

# 形状修改
    1. ndarray.reshape(shape, order)        返回一个具有相同数据域，但shape不一样的视图, 行、列不进行互换
            stock_change.reshape([5, 4])
    2. ndarray.resize(new_shape)    修改数组本身的形状（需要保持元素个数前后相同）行、列不进行互换
            stock_change.resize([5, 4])
            stock_change.shape
    3. ndarray.T        数组的转置、将数组的行、列进行互换
            stock_change.T.shape

# 类型修改
    1.ndarray.astype(type)  返回修改了类型之后的数组
            stock_change.astype(np.int32)
    2. ndarray.tostring([order])或者ndarray.tobytes([order])  构造包含数组中原始数据字节的Python字节
            arr = np.array([[[1, 2, 3], [4, 5, 6]], [[12, 3, 34], [5, 6, 7]]])
            arr.tostring()
    
# 数组的去重
    1.  temp = np.array([[1, 2, 3, 4],[3, 4, 5, 6]])
        np.unique(temp)


# ndarray的运算
    1. 通用判断函数:
            np.all(score[0:2, :] > 60)      判断前两名同学的成绩[0:2, :]是否全及格
            np.any(score[0:2, :] > 80)      判断前两名同学的成绩[0:2, :]是否有大于80分的
    2.np.where（三元运算符）:
            temp = score[:4, :4]            前四名学生,前四门课程
            np.where(temp > 60, 1, 0)       成绩中大于60的置为1，否则为0
            np.where(np.logical_and(temp > 60, temp < 90), 1, 0)    成绩中大于60且小于90的换为1，否则为0
            np.where(np.logical_or(temp > 90, temp < 60), 1, 0)     成绩中大于90或小于60的换为1，否则为0
    3. 统计运算：axis 轴的取值并不一定，需要注意
            np.max()    ：找到最大值
            np.min()
            np.mean()
            np.std()
            np.var()
            
            np.argmax() :找到最大值对应的索引下标
            np.argmin() :找到最小值对应的索引下标

# 矩阵
    1。矩阵加法和标量乘法
            矩阵的加法:行列数相等的可以加。
            矩阵的乘法:每个元素都要乘。
    2。矩阵和矩阵(向量)相乘 ：(M行, N列)*(N行, L列) = (M行, L列)
    3。单位矩阵：对角线都是1的矩阵,其他位置都为0
    4。矩阵运算：
            矩阵乘法api： np.matmul（）          np.dot（）
            二者都是矩阵乘法。 np.matmul中禁止矩阵与标量的乘法。 在矢量乘矢量的內积运算中，np.matmul与np.dot没有区别。
            
           ｜1 2 3｜      ｜1 2 1｜         ｜1+2+6  2+2+3   1+4+3 ｜         ｜9  7   8 ｜ 
           ｜4 5 6｜  *   ｜1 1 2｜  =      ｜4+5+12 8+5+6   4+10+6｜     =   ｜21 19  10｜
           ｜7 8 0｜      ｜2 1 1｜         ｜7+8+0  14+8+0  7+16+0｜         ｜15 22  23｜

