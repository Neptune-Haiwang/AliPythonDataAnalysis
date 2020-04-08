import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# 癌症分类预测-良／恶性乳腺癌肿瘤预测
def cancer():
    # 1.获取数据
    names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
             'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
             'Normal Nucleoli', 'Mitoses', 'Class']
    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=names)
    print(data.head())
    # 2.基本数据处理
    # 2.1 缺失值处理
    data = data.replace(to_replace='?', value=np.NaN)
    data = data.dropna()
    # 2.2 确定特征值,目标值
    x_data = data.iloc[:, 1:10]
    print(x_data.head())
    x_target = data['Class']
    print(x_target.head())
    # 2.3 分割数据
    x_train, x_test, y_train, y_test = train_test_split(x_data, x_target, random_state=22)

    # 3.特征工程(标准化)
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)
    # 4.机器学习(逻辑回归)
    estimator = LogisticRegression()
    estimator.fit(x_train, y_train)
    # 5.模型评估
    y_predict = estimator.predict(x_test)
    print(y_predict)
    print(estimator.score(x_test, y_test))


if __name__=='__main__':
    cancer()