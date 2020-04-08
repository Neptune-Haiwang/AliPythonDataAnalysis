import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz


# 泰坦尼克号乘客生存预测
def titanic():
    # 1、获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")

    # 2 数据基本处理
    # 2.1 确定特征值,目标值
    x = titan[["pclass", "age", "sex"]]
    y = titan['survived']
    # 2.2 缺失值处理
    x['age'] = x['age'].fillna(x['age'].mean(), inplace=True)
    # 2.3 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=22)

    # 3.特征工程(字典特征抽取)
    # 对于x转换成字典数据x.to_dict(orient="records")
    # [{"pclass": "1st", "age": 29.00, "sex": "female"}, {...}, {...}, ...]
    transfer = DictVectorizer(sparse=False)
    x_train = transfer.fit_transform(x_train.to_dict(orient="records"))
    x_test = transfer.fit_transform(x_test.to_dict(orient="records"))

    # 4.机器学习(决策树)
    estimator = DecisionTreeClassifier(criterion="entropy", max_depth=5)
    estimator.fit(x_train, y_train)
    # 5.模型评估
    estimator.score(x_test, y_test)
    estimator.predict(x_test)
    # # 保存树的结构到dot文件, 使用此网址查看 http://webgraphviz.com/
    # export_graphviz(estimator, out_file="./data/tree.dot",
    #                 feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', '女性', '男性'])


if __name__=='__main__':
    titanic()