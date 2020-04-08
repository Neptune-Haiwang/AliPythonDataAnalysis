import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score


def kmeans_simple():
    # 1 创建数据集
    # 例：以[-1,-1]为中心点的数据簇的标准差为0.4, 以[0,0]为中心点的数据簇的标准差为0.2, ..
    X, y = make_blobs(n_samples=1000, n_features=2, centers=[[-1,-1], [0,0], [1,1], [2,2]],
                      cluster_std=[0.4, 0.2, 0.2, 0.2], random_state=9)
    # 共两个维度，
    plt.scatter(X[:, 0], X[:, 1], marker='o')
    plt.show()
    # 2 k-means训练
    # 设置分类的个数
    y_predict = KMeans(n_clusters=4, random_state=9).fit_predict(X)
    # 可视化展示
    # 以预测出的质心坐标，为中心
    plt.scatter(X[:, 0], X[:, 1], c=y_predict)
    plt.show()
    # 3 使用CH方法评估
    print('评估的聚类分数: %s' % calinski_harabasz_score(X, y_predict))




if __name__=='__main__':
    kmeans_simple()