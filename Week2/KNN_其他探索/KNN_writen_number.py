from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def knn_writen_numbers():
    """KNN 算法 识别手写数字, 添加网格搜索和交叉验证
        @return:
        """
    # 1）获取数据
    digits = load_digits()
    # print('数据集的大小：', digits.data.shape)
    # 展示图片 (以第一张图片为例)
    # plt.imshow(digits.images[0])
    # 也可以改变参数，图形以灰度图显示
    plt.imshow(digits.images[0], cmap='gray')
    plt.show()

    # 2) 数据集划分
    """random_state这个参数
    作用：控制随机状态
    固定random_state后，每次构建的模型是相同的、生成的数据集是相同的、每次的拆分结果也是相同的。
    """
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=0)

    # 3）特征工程：标准化
    transfer = StandardScaler()
    # 对训练集进行标准化: fit在做计算， transform在做转换
    x_train = transfer.fit_transform(x_train)
    # 用训练集的平均值和标准差对测试集进行标准化
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器 # 默认参数，创建空分类器
    estimator = KNeighborsClassifier()
    # 加入网格搜索与交叉验证 # 添加网格搜索参数
    # """网格搜索算法
    # GridSearchCV，它存在的意义就是自动调参，只要把参数输进去，就能给出最优化的结果和参数。
    # param_grid:需要最优化的参数的取值，值为字典或者列表
    # cv=None: 交叉验证参数，默认None，使用三折交叉验证。指定fold数量，默认为3
    # """
    # param_grid = [
    #     {
    #         'n_neighbors': [i for i in range(1, 11)],
    #         'weights': ['uniform', 'distance'],
    #         'algorithm': ['auto', 'kd_tree', 'ball_tree', 'brute'],
    #         'leaf_size': [20, 30, 40, 50]
    #      }
    # ]
    # estimator = GridSearchCV(estimator, param_grid=param_grid, cv=3)
    estimator.fit(x_train, y_train)


    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    # 用KNN算法预估器 对 测试集的特征值 进行预测
    y_predict = estimator.predict(x_test)
    print('真实结果:\n%s \n预测结果:\n%s \n正确与否\n%s' % (y_test, y_predict, y_test == y_predict))
    # 方法2：计算准确率 : 特征值，目标值
    score1 = estimator.score(x_train, y_train)
    score2 = estimator.score(x_test, y_test)
    print('训练集的准确率: %s， 而测试集的准确率为：%s' % (score1, score2))

    # # 找到最佳的:参数、准确率、估计器、 (交叉验证结果estimator.cv_results_)
    # print('最佳K参数: %s, \n最佳测试准确率: %s, \n最佳估计器: %s' % (estimator.best_params_, estimator.best_score_, estimator.best_estimator_))


if __name__ == '__main__':
    knn_writen_numbers()

