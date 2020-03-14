from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

def knn_writen_numbers():

    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=66)

    # 3) 分析不同参数的变化对K近邻算法预测精度和泛化能力的影响
    neighbours_range = range(1, 11)
    weights_range = ['uniform', 'distance']
    algorithm_range = ['auto', 'kd_tree', 'ball_tree', 'brute']
    leaf_size_range = [10, 20, 30, 40, 50]

    train_accuracy1, train_accuracy2, train_accuracy3, train_accuracy4 = [],[],[],[]
    test_accuracy1, test_accuracy2, test_accuracy3, test_accuracy4 = [],[],[],[]

    # 4）分析 不同的参数对KNeighbors预测效果的影响
    # n_neighbors参数对KNeighbors预测效果的影响
    for k in neighbours_range:
        # 构建模型
        estimator = KNeighborsClassifier(n_neighbors=k)
        estimator.fit(x_train, y_train)
        # 记录训练集精度S
        train_accuracy1.append(estimator.score(x_train, y_train))
        # 记录泛化能力
        test_accuracy1.append(estimator.score(x_test, y_test))

    # weights 参数对KNeighbors预测效果的影响
    for i in weights_range:
        estimator = KNeighborsClassifier(n_neighbors=5, weights=i)
        estimator.fit(x_train, y_train)
        train_accuracy2.append(estimator.score(x_train, y_train))
        test_accuracy2.append(estimator.score(x_test, y_test))

    # algorithm 参数对KNeighbors预测效果的影响
    for j in algorithm_range:
        estimator = KNeighborsClassifier(n_neighbors=5, algorithm=j)
        estimator.fit(x_train, y_train)
        train_accuracy3.append(estimator.score(x_train, y_train))
        test_accuracy3.append(estimator.score(x_test, y_test))

    # leaf_size 参数对KNeighbors预测效果的影响
    for k in leaf_size_range:
        estimator = KNeighborsClassifier(n_neighbors=5, leaf_size=k)
        estimator.fit(x_train, y_train)
        train_accuracy4.append(estimator.score(x_train, y_train))
        test_accuracy4.append(estimator.score(x_test, y_test))

    # 图大小
    plt.figure(figsize=(10, 6))

    # 221 > 2行2列第1个
    figure1 = plt.subplot(221)
    plt.plot(neighbours_range, train_accuracy1, label='training accuracy')
    plt.plot(neighbours_range, test_accuracy1, label='test accuracy')
    plt.xlabel('N_neighbors')
    plt.ylabel('Accuracy')
    plt.legend()

    # 222 > 2行2列第2个
    figure2 = plt.subplot(222)
    plt.plot(weights_range, train_accuracy2, label='training accuracy')
    plt.plot(weights_range, test_accuracy2, label='test accuracy')
    plt.xlabel('Weights')
    plt.ylabel('Accuracy')
    plt.legend()

    # 223 > 2行2列第3个
    figure3 = plt.subplot(223)
    plt.plot(algorithm_range, train_accuracy3, label='training accuracy')
    plt.plot(algorithm_range, test_accuracy3, label='test accuracy')
    plt.xlabel('Algorithm')
    plt.ylabel('Accuracy')
    plt.legend()

    # 224 > 2行2列第4个
    figure4 = plt.subplot(224)
    plt.plot(leaf_size_range, train_accuracy4, label='training accuracy')
    plt.plot(leaf_size_range, test_accuracy4, label='test accuracy')
    plt.xlabel('Leaf Size')
    plt.ylabel('Accuracy')
    plt.legend()

    # 展示 画图的结果
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    knn_writen_numbers()
