# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import datetime
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


def huabei_wei():

    # 第一步：加载数据(已经经过PCA降维了)
    # data = pd.read_csv('https://www.dropbox.com/s/qk3u8j529tgj72d/alipay_huabei_FS1.csv?dl=0')
    data = pd.read_csv('/Users/haiwangluo/Desktop/alipython_files/alipay_huabei_FS1.csv')
    # 筛选特征值
    x_data = data.iloc[:, 1: -2]
    print(x_data.head())
    # 筛选目标值
    x_target = data['Class']
    print(x_target.value_counts())

    # 第二步：准备数据
    x_train, x_test, y_train, y_test = train_test_split(x_data, x_target, test_size=0.3, stratify=x_target, random_state=1)

    # 第三步：构造各种分类器
    estimator_models = [
        Pipeline(steps=[('svc', SVC(random_state=1, kernel='rbf'))]),
        Pipeline(steps=[('rfc', RandomForestClassifier(random_state=1, criterion='gini'))]),
        Pipeline(steps=[('abc', AdaBoostClassifier(random_state=1, algorithm='SAMME.R'))])
    ]
    # 第四步：设置分类器的参数
    parameters_list = [
        {'svc__C': [1], 'svc__gamma': [0.01]},
        {'rfc__max_depth': [6, 9, 11], 'rfc__n_estimators': [3, 5, 9]},
        {'abc__n_estimators': [10, 50], 'abc__learning_rate': [0.1, 1.0, 10]}
    ]
    # 第五步：对具体的分类器进行GridSearchCV参数调优
    # gridsearchcv_works(x_train, x_test, y_train, y_test, 'SVM支持向量机算法', estimator_models[0], parameters_list[0])
    gridsearchcv_works(x_train, x_test, y_train, y_test, '随机森林算法', estimator_models[1], parameters_list[1])
    gridsearchcv_works(x_train, x_test, y_train, y_test, 'AdaBoost提升算法', estimator_models[2], parameters_list[2])


def gridsearchcv_works(x_train, x_test, y_train, y_test, estimator_name, estimator_model, params):
    '''GridSearchCV参数调优

    @param x_train: 训练集特征值
    @param x_test: 测试集特征值
    @param y_train: 训练集目标值
    @param y_test: 测试集目标值
    @param estimator_name: 算法模型的名称
    @param estimator_model: 算法模型
    @param params: 算法模型中需要调优的参数
    @return:
    '''
    # 调用 datetime 函数，-> 获取算法运行时间
    time_start = datetime.datetime.now()
    # 使用 GridSearchCV 调参数， 选择到对应的算法模型
    estimator = GridSearchCV(estimator_model, param_grid=params, scoring='accuracy', cv=3)
    estimator.fit(x_train, y_train)
    y_predict = estimator.predict(x_test)
    print('%s模型的最优参数组合为： %s' % (estimator_name, estimator.best_params_))
    print('%s模型的最优分数为：%.5f\t准确率为：%.5f' % (estimator_name, estimator.best_score_, accuracy_score(y_test, y_predict)))
    print('%s模型的分类结果报告：\n%s' % (estimator_name, classification_report(y_test, y_predict, target_names=['0 正常(非欺诈)', '1 代表欺诈'])))
    print('%s模型的混淆矩阵为：\n%s' % (estimator_name, confusion_matrix(y_test, y_predict)))
    time_period = datetime.datetime.now() - time_start
    print('%s模型的训练总耗时为：%s' % (estimator_name, time_period))


huabei_wei()