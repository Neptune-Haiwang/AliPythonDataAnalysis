from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def knn_WRN_basics():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=2)
    # # 2.1）特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 3）朴素贝叶斯算法预估器流程
    estimator = KNeighborsClassifier()
    estimator.fit(x_train, y_train)
    # 4）模型评估
    # print('KNN基础模型准确率为: %s' % estimator.score(x_test, y_test))

    y_predict = estimator.predict(x_test)    # 获取预测结果
    # 预测结果展示
    labels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(100):
        print('第%d次测试:真实值:%s\t预测值:%s' % ((i + 1), labels[y_test[i]], labels[y_predict[i]]))
    print('KNN基础模型准确率为: %s' % estimator.score(x_test, y_test))


if __name__ == '__main__':
    knn_WRN_basics()