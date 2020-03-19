from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt


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
    print('KNN基础模型准确率为: %s' % estimator.score(x_test, y_test))


def knn_WRN_Advanced():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=2)
    # 2.1）特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)

    # 3) 分析不同的超参数的变化对K近邻算法预测精度和泛化能力的影响
    neighbours_range = range(1, 11)
    weights_range = ['uniform', 'distance']
    algorithm_range = ['auto', 'kd_tree', 'ball_tree', 'brute']
    leaf_size_range = [10, 20, 30, 40, 50]

    train_accuracy1, train_accuracy2, train_accuracy3, train_accuracy4 = [], [], [], []
    test_accuracy1, test_accuracy2, test_accuracy3, test_accuracy4 = [], [], [], []

    # 4）分析 不同的超参数调整对KNeighbors预测效果的影响
    # n_neighbors 超参数对KNeighbors预测效果的影响
    for n in neighbours_range:
        # 构建模型
        estimator = KNeighborsClassifier(n_neighbors=n)
        estimator.fit(x_train, y_train)
        # 记录训练集精度S
        train_accuracy1.append(estimator.score(x_train, y_train))
        # 记录泛化能力
        test_accuracy1.append(estimator.score(x_test, y_test))

    # weights 超参数对KNeighbors预测效果的影响
    for i in weights_range:
        estimator = KNeighborsClassifier(weights=i)
        estimator.fit(x_train, y_train)
        train_accuracy2.append(estimator.score(x_train, y_train))
        test_accuracy2.append(estimator.score(x_test, y_test))

    # algorithm 超参数对KNeighbors预测效果的影响
    for j in algorithm_range:
        estimator = KNeighborsClassifier(algorithm=j)
        estimator.fit(x_train, y_train)
        train_accuracy3.append(estimator.score(x_train, y_train))
        test_accuracy3.append(estimator.score(x_test, y_test))

    # leaf_size 超参数对KNeighbors预测效果的影响
    for k in leaf_size_range:
        estimator = KNeighborsClassifier(leaf_size=k)
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


def naiveBayes_WNR_basics():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2,random_state=2)
    # 3）朴素贝叶斯算法预估器流程
    estimator = MultinomialNB()
    estimator.fit(x_train, y_train)
    # 4）模型评估
    print('朴素贝叶斯基础模型准确率为: %s' % estimator.score(x_test, y_test))


def naiveBayes_WNR_Advanced():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=2)
    # 3) 分析不同的超参数的变化对朴素贝叶斯算法预测精度和泛化能力的影响
    alpha_range = range(1, 50)
    # alpha_range = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    fit_prior_range = ['True', 'False']
    train_accuracy1, test_accuracy1, train_accuracy2, test_accuracy2 = [], [], [], []

    # 4.1) alpha 超参数对朴素贝叶斯预测效果的影响
    for a in alpha_range:
        # 构建模型
        estimator = MultinomialNB(alpha=a)
        estimator.fit(x_train, y_train)
        # 记录训练集精度
        train_accuracy1.append(estimator.score(x_train, y_train))
        # 记录泛化能力
        test_accuracy1.append(estimator.score(x_test, y_test))

    # 4.2) fit_prior 超参数对朴素贝叶斯预测效果的影响
    for f in fit_prior_range:
        estimator = MultinomialNB(fit_prior=f)
        estimator.fit(x_train, y_train)
        train_accuracy2.append(estimator.score(x_train, y_train))
        test_accuracy2.append(estimator.score(x_test, y_test))

    # 5)  绘图
    plt.figure(figsize=(10, 6))
    # 121 > 1行2列第1个
    figure1 = plt.subplot(121)
    plt.plot(alpha_range, train_accuracy1, label='training accuracy')
    plt.plot(alpha_range, test_accuracy1, label='test accuracy')
    plt.xlabel('alpha')
    plt.ylabel('Accuracy')
    plt.legend()

    # 122 > 1行2列第2个
    figure1 = plt.subplot(122)
    plt.plot(fit_prior_range, train_accuracy2, label='training accuracy')
    plt.plot(fit_prior_range, test_accuracy2, label='test accuracy')
    plt.xlabel('fit_prior')
    plt.ylabel('Accuracy')
    plt.legend()

    # 展示 画图的结果
    plt.tight_layout()
    plt.show()


def svm_WNR_basic():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=2)
    # # 2.1）特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 3）SVM算法预估器流程
    estimator = SVC(gamma='scale')
    estimator.fit(x_train, y_train)
    # 4）模型评估
    print('SVM基础模型准确率为: %s' % estimator.score(x_test, y_test))


def svm_WNR_Advanced():
    # 1）获取数据
    digits = load_digits()
    # 2) 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=2)
    # # 2.1）特征工程：标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 3) 分析不同的超参数的变化对SVM算法预测精度和泛化能力的影响
    C_range = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    kernel_range = ['linear', 'poly', 'rbf']
    degree_range = [1, 2, 3, 4, 5]
    random_state_range = [None, 0, 1, 2, 3, 4, 5]
    train_accuracy1, train_accuracy2, train_accuracy3, train_accuracy4 = [], [], [], []
    test_accuracy1, test_accuracy2, test_accuracy3, test_accuracy4 = [], [], [], []

    # 3.1) C 超参数对SVM预测效果的影响
    for c in C_range:
        estimator = SVC(gamma='scale', C=c)
        estimator.fit(x_train, y_train)
        train_accuracy1.append(estimator.score(x_train, y_train))
        test_accuracy1.append(estimator.score(x_test, y_test))
    # 3.2) kernel 超参数对SVM预测效果的影响
    for k in kernel_range:
        estimator = SVC(gamma='scale', kernel=k)
        estimator.fit(x_train, y_train)
        train_accuracy2.append(estimator.score(x_train, y_train))
        test_accuracy2.append(estimator.score(x_test, y_test))
    # 3.3) degree 超参数对SVM预测效果的影响
    for d in degree_range:
        estimator = SVC(gamma='scale', degree=d)
        estimator.fit(x_train, y_train)
        train_accuracy3.append(estimator.score(x_train, y_train))
        test_accuracy3.append(estimator.score(x_test, y_test))
    # 3.4) random_state 超参数对SVM预测效果的影响
    for r in random_state_range:
        estimator = SVC(gamma='scale', random_state=r)
        estimator.fit(x_train, y_train)
        train_accuracy4.append(estimator.score(x_train, y_train))
        test_accuracy4.append(estimator.score(x_test, y_test))

    # 5)  绘图
    plt.figure(figsize=(10, 6))
    # 221 > 2行2列第1个
    plt.subplot(221)
    plt.plot(C_range, train_accuracy1, label='training accuracy')
    plt.plot(C_range, test_accuracy1, label='test accuracy')
    plt.xlabel('C')
    plt.ylabel('Accuracy')
    plt.legend()
    # 222 > 2行2列第2个
    plt.subplot(222)
    plt.plot(kernel_range, train_accuracy2, label='training accuracy')
    plt.plot(kernel_range, test_accuracy2, label='test accuracy')
    plt.xlabel('kernel')
    plt.ylabel('Accuracy')
    plt.legend()
    # 223 > 2行2列第3个
    plt.subplot(223)
    plt.plot(degree_range, train_accuracy3, label='training accuracy')
    plt.plot(degree_range, test_accuracy3, label='test accuracy')
    plt.xlabel('degree')
    plt.ylabel('Accuracy')
    plt.legend()
    # 224 > 2行2列第4个
    plt.subplot(224)
    plt.plot(random_state_range, train_accuracy4, label='training accuracy')
    plt.plot(random_state_range, test_accuracy4, label='test accuracy')
    plt.xlabel('random state')
    plt.ylabel('Accuracy')
    plt.legend()

    # 展示 画图的结果
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # knn_WRN_basics()
    # naiveBayes_WNR_basics()
    # svm_WNR_basic()

    # knn_WRN_Advanced()
    naiveBayes_WNR_Advanced()
    # svm_WNR_Advanced()
