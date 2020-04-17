from sklearn.datasets import make_classification, load_iris
from my_Preprocessing import train_test_split, accuracy_rate
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import pandas as pd
from my_KNN import KNN
from my_PCA import PCA



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
    clf = KNN(k=5)  # clf 是创建的一个对象，用来调用各种函数方法
    y_predict = clf.predict(x_test, x_train, y_train)
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




if __name__=='__main__':
    knn_classification()
    # PCA_decomposition()
    