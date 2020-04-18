from sklearn.datasets import make_classification, load_iris, make_blobs
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
from my_Preprocessing import train_test_split, accuracy_rate, normalize
from my_KNN import KNN_classifier
from my_PCA import PCA
from my_NaiveBayes import NaiveBayes_classifier
from my_Kmeans import Kmeans
from my_logisticRegression import LogisticRegression_classifier


def knn_classification():
    '''
    KNN分类算法
    @return:
    '''
    data = make_classification(n_samples=200, n_features=4, n_informative=2, n_redundant=2, n_repeated=0, n_classes=2)
    # 分出 特征值 与目标值
    x_data, y_target = data[0], data[1]
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.33, shuffle=True)
    # 调用封装好的文件中的类 -> 设置初始k
    estimator = KNN_classifier(k=5)  # clf 是创建的一个对象，用来调用各种函数方法
    y_predict = estimator.predict(x_test, x_train, y_train)
    accur = accuracy_rate(y_test, y_predict)
    print('预测准确率 %s' % accur)
    return None


def PCA_decomposition():
    '''
    PCA主成分分析降维
    @return:
    '''
    data = load_iris()
    x_data = data.data
    y_target = data.target
    # 将数据集X映射到低维空间
    x_transform = PCA().transform(x_data)
    x1 = x_transform[:, 0]
    x2 = x_transform[:, 1]
    cmap = plt.get_cmap('viridis')
    colors = [cmap(i) for i in np.linspace(0, 1, len(np.unique(y_target)))]
    class_distr = []
    # Plot the different class distributions
    for i, j in enumerate(np.unique(y_target)):
        x1_1 = x1[y_target == j]
        x2_1 = x2[y_target == j]
        y_1 = y_target[y_target == j]
        class_distr.append(plt.scatter(x1_1, x2_1, color=colors[i]))
    plt.legend(class_distr, y_target, loc=1)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()


def NaiveBayes_classification():
    x_data = np.array([
        ['M','北京'], ['F', '上海'], ['M' ,'广州'], ['M' ,'北京'], ['F' ,'上海'],
        ['M','北京'], ['F', '上海'], ['M' ,'广州'], ['M' ,'北京'], ['F' ,'上海']])
    y_target = np.array([1,0,1,1,0,
                         1,0,1,1,0])
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.3)
    estimator = NaiveBayes_classifier()
    estimator.fit(x_train, y_train)
    y_predict = np.array(estimator.predict(x_test))
    accu = accuracy_rate(y_test, y_predict)
    print('预测准确率 %s' % accu)
    return None


def kmeans_cluster():
    # Load the dataset
    x_data, y_target = make_blobs(n_samples=1000, n_features=3, centers=[[0,0,0], [1,1,1], [2,2,2],[3,3,3]],
                                  cluster_std=[0.1, 0.2, 0.2, 0.2], random_state=9)
    # 用Kmeans算法进行聚类
    estimator = Kmeans(k=4)
    y_predict = estimator.predict(x_data)
    # 可视化聚类效果
    fig = plt.figure(figsize=(12, 8))
    ax = Axes3D(fig, rect=[0,0,1,1], elev=30, azim=20)
    plt.scatter(x_data[y_target == 0][:, 0], x_data[y_target == 0][:, 1], x_data[y_target == 0][:, 2])
    plt.scatter(x_data[y_target == 1][:, 0], x_data[y_target == 1][:, 1], x_data[y_target == 1][:, 2])
    plt.scatter(x_data[y_target == 2][:, 0], x_data[y_target == 2][:, 1], x_data[y_target == 2][:, 2])
    plt.scatter(x_data[y_target == 3][:, 0], x_data[y_target == 3][:, 1], x_data[y_target == 3][:, 2])
    plt.show()


def logisticregression_classification():
    # 加载数据集
    data = load_iris()
    x_data = normalize(data.data[data.target != 0])
    y_target = data.target[data.target != 0]
    y_target[y_target == 1] = 0
    y_target[y_target == 2] = 1
    # 划分数据集
    x_train ,x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.3, seed=1)
    # 进行预测
    estimator = LogisticRegression_classifier()
    estimator.fit(x_train, y_train)
    y_predict = estimator.predict(x_test)
    print('预测准确率为： %.5f' % accuracy_rate(y_test, y_predict))

    plt.figure(figsize=(12,8))
    plt.scatter(x_data[y_target == 0][:, 0], x_data[y_target == 0][:, 1])
    plt.scatter(x_data[y_target == 1][:, 0], x_data[y_target == 1][:, 1])
    plt.show()




if __name__=='__main__':
    # knn_classification()
    # PCA_decomposition()
    # NaiveBayes_classification()
    # kmeans_cluster()
    logisticregression_classification()
