from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def knn_iris():
    """
    knn算法 对鸢尾花分类
    @return:None
    """
    # 1）获取数据
    iris = load_iris()
    # 2）划分数据集
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)

    # 3）特征工程：标准化
    transfer = StandardScaler()
    # 对训练集进行标准化: fit在做计算， transform在做转换
    x_train = transfer.fit_transform(x_train)
    # 用训练集的平均值和标准差对测试集进行标准化
    x_test = transfer.transform(x_test)

    # 4）KNN算法预估器
    estimator = KNeighborsClassifier(n_neighbors=3)
    # 把训练集丢给 KNN 算法 进行计算，训练
    estimator.fit(x_train, y_train)

    # 5）模型评估
    # 方法1：直接比对真实值和预测值
    y_predict = estimator.predict(x_test)
    print('真实值: %s 和预测值: %s , 正确与否：%s' % (y_test, y_predict, y_test == y_predict))
    # 方法2：计算准确率 : 测试集的特征值，测试集的目标值
    score = estimator.score(x_test, y_test)
    print('准确率 %s' % score)


if __name__ == '__main__':
    knn_iris()
