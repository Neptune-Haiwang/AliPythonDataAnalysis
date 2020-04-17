import numpy as np
import matplotlib.pyplot as plt


# ndarray的属性、ndarray的形状、ndarray的类型
def simple_numpy():
    score = np.array(
        [[80, 89, 86, 67, 79],
        [78, 97, 89, 67, 81],
        [90, 94, 78, 67, 74],
        [91, 91, 90, 67, 69],
        [76, 87, 75, 67, 86],
        [70, 79, 84, 67, 84],
        [94, 92, 93, 67, 64],
        [86, 85, 83, 67, 80]]
    )
    print(score)
    print(score.shape)  # 数组维度的元组：返回（8，5）->表示数组为 8行5列
    print(score.ndim)   # 数组维数：返回 2 -> 表示是一个二维数组
    print(score.size)   # 数组中的元素数量：返回 40 ->表示数组中一共有40个元素
    print(score.itemsize)   # 一个数组元素的长度（字节）：返回 8 -> 表示数组中每个元素的长度是8个字节
    print(score.dtype)      # 数组元素的类型：返回 int64 ->表示数组中元素的类型是 int64

    a = np.array([1,2,3])   # 一维数组
    print(a.shape)  # 返回为 （3，）    -> 代表：这个数组中有三个元素
    b = np.array([[1,2,3], [4,5,6]])  # 二维数组
    print(b.shape)  # 返回为 （2，3）   -> 代表：这个数组中有2个一维数组，每个一维数组中有三个元素
    c = np.array([[[1,2,3], [4,5,6]],[[1,2,3], [4,5,6]]])   # 三维数组
    print(c.shape)  # 返回为 （2, 2，3）-> 代表：这个数组中有2个二维数组，每个二维数组中有2个一维数组，每个一维数组中有三个元素

    # 创建数组的时候指定类型
    ar = np.array(['abc','www', 'wwwa'], dtype=np.string_)
    print(ar.dtype)


# 数组的基本操作
def basic_numpy():
    # 1 生成数组的方法
    # 1.1 生成0和1的数组
    ones = np.ones([4, 8])
    print(ones)
    zeros= np.zeros_like(ones)
    print(zeros)
    # 1.2 从现有数组生成
    a = np.array([[1,2,3],[4,5,6]])
    a1 = np.array(a) # 深拷贝
    print(a1)
    a2 = np.asarray(a)  # 浅拷贝
    a[0,0] = 100
    print(a1)
    print(a2)

    # 1.3 生成固定范围的数组
    # 1.3.1 np.linspace (start, stop, num, endpoint) 创建等差数组 — 指定数量( 生成等间隔的多少个)
    m = np.linspace(0, 100, 11)    # 从0到100，生成11个数字-> [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]
    print(m)
    #  1.3.2 np.arange(start,stop, step, dtype) -> 创建等差数组 — 指定步长(每间隔多少生成数据)
    m2 = np.arange(10, 50, 2)   # -> [10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48]
    print(m2)
    # 1.3.3 np.logspace(start,stop, num) -> 创建等比数列 (生成以10的N次幂的数据)
    m3 = np.logspace(0, 2, 3)   # -> [  1.  10. 100.]
    print(m3)


# 生成随机数组
def suijishuzu():
    # 随机生成4支股票1周的交易日涨幅数据
    # 1. 生成数据：创建符合正态分布的4只股票5天的涨跌幅数据
    stock_change = np.random.normal(loc=0, scale=1, size=(4,5))   # 四行五列
    # 2. 创建画布
    plt.figure(figsize=(10,4), dpi=100)
    # 3. 绘制折线图
    plt.plot(stock_change)
    # 4. 显示图像
    plt.show()


# 数组的索引、切片
def suoyin_qiepian():
    # 1 二维数组索引方式
    stock_change = np.random.normal(loc=0, scale=1, size=(4, 5))  # 四行五列
    print(stock_change[0, 0:3])
    # 2 三维数组索引方式
    a1 = np.array([[[1, 2, 3], [4, 5, 6]],
                   [[12, 3, 34], [5, 6, 7]]])
    print(a1[1,0,0]) # 输出为12


# ndarray的运算
def ndarray_yunsuan():
    # 1. 逻辑运算
    score = np.random.randint(40, 100, (10, 5))     # 生成10名同学，5门功课的数据
    test_score = score[6:, 0:5]  # 取出最后4名同学的成绩，用于逻辑判断
    print(test_score)
    print(test_score>60)
    test_score[test_score>60] = 1
    print(test_score)





if __name__ == '__main__':
    # simple_numpy()
    # basic_numpy()
    # suijishuzu()
    # suoyin_qiepian()
    ndarray_yunsuan()