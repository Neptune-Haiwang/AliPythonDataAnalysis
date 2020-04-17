from sklearn.datasets import make_classification
import my_KNN
from my_Preprocessing import train_test_split, accuracy_rate


def knn_classification():
    data = make_classification(n_samples=200, n_features=4, n_informative=2, n_redundant=2, n_repeated=0, n_classes=2)
    # 分出 特征值 与目标值
    x_data, y_target = data[0], data[1]
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.33, shuffle=True)
    # 调用封装好的文件中的类 -> 设置初始k
    clf = my_KNN.KNN(k=5)
    y_predict = clf.predict(x_test, x_train, y_train)
    accur = accuracy_rate(y_test, y_predict)
    print('预测准确率 %s' % accur)
    return None


if __name__=='__main__':
    knn_classification()
