# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import datetime
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score
from xgboost import XGBClassifier
import numpy as np


def huabei_wei():

    # 第一步：加载数据(已经经过PCA降维了)
    # data = pd.read_csv('https://www.dropbox.com/s/qk3u8j529tgj72d/alipay_huabei_FS1.csv?dl=0')
    data = pd.read_csv('/Users/haiwangluo/Desktop/alipython_files/alipay_huabei_FS1.csv')
    # 筛选特征值
    x_data = data.iloc[:, 1: -2]
    # print(x_data.head())
    # 筛选目标值
    x_target = data['Class']
    # print(x_target.value_counts())

    # 第二步：准备数据
    x_train, x_test, y_train, y_test = train_test_split(x_data, x_target, test_size=0.3, stratify=x_target, random_state=1)

    # 第三步：构造各种分类器
    estimator_models = [
        Pipeline(steps=[('rfc', RandomForestClassifier(random_state=1))]),
        Pipeline(steps=[('abc', AdaBoostClassifier(random_state=1))]),
        Pipeline(steps=[('xgbc', XGBClassifier(random_state=1))])
    ]
    # 第四步：设置分类器的参数
    parameters_list = [
        {'rfc__max_depth': [9], 'rfc__n_estimators': [9], 'rfc__min_samples_leaf': [10], 'rfc__criterion': ['gini']},
        {'abc__n_estimators': [50], 'abc__learning_rate': [1.0], 'abc__algorithm': ['SAMME.R']},
        {'xgbc__max_depth': [11], 'xgbc__n_estimators': [54], 'xgbc__learning_rate': [1.0], 'xgbc__min_child_weight': [1]}
    ]
    # 第五步：对具体的分类器进行GridSearchCV参数调优
    gw1 = gridsearchcv_works(x_train, x_test, y_train, y_test, '随机森林算法', estimator_models[0], parameters_list[0])
    gw2 = gridsearchcv_works(x_train, x_test, y_train, y_test, 'AdaBoost提升算法', estimator_models[1], parameters_list[1])
    gw3 = gridsearchcv_works(x_train, x_test, y_train, y_test, 'XGBoost分类提升算法', estimator_models[2], parameters_list[2])

    # 第六步：画一个表格 把所有model的结果都集中到一起
    # 列(0-5)：'最优分数', '准确率', '精确率', '召回率', 'F1 score', '训练时间'
    col = ['最优分数', '准确率', '精确率', '召回率', 'F1 score', '训练时间']
    df = pd.DataFrame(columns=col)
    d1 = pd.Series({col[0]:gw1[0], col[1]:gw1[1], col[2]:gw1[2], col[3]:gw1[3], col[4]:gw1[4], col[5]:gw1[5]}, name='随机森林算法')
    d2 = pd.Series({col[0]:gw2[0], col[1]:gw2[1], col[2]:gw2[2], col[3]:gw2[3], col[4]:gw2[4], col[5]:gw2[5]}, name='AdaBoost提升算法')
    d3 = pd.Series({col[0]:gw3[0], col[1]:gw3[1], col[2]:gw3[2], col[3]:gw3[3], col[4]:gw3[4], col[5]:gw3[5]}, name='XGBoost分类提升算法')
    df = df.append(d1).append(d2).append(d3)
    print(df)


def gridsearchcv_works(x_train, x_test, y_train, y_test, estimator_name, estimator_model, params):
    '''GridSearchCV参数调优

    @param x_train: 训练集特征值
    @param x_test: 测试集特征值
    @param y_train: 训练集目标值
    @param y_test: 测试集目标值
    @param estimator_name: 算法模型的名称
    @param estimator_model: 算法模型
    @param params: 算法模型中需要调优的参数
    @return: 返回关于训练结果的列表
    '''
    # 调用 datetime 函数，-> 获取算法运行时间
    time_start = datetime.datetime.now()
    # 使用 GridSearchCV 调参数， 选择到对应的算法模型
    estimator = GridSearchCV(estimator_model, param_grid=params, scoring='accuracy', cv=3)
    estimator.fit(x_train, y_train)
    y_predict = estimator.predict(x_test)
    print('%s模型的最优参数组合为 %s' % (estimator_name, estimator.best_params_))
    # print('%s模型的分类结果报告：\n%s' % (estimator_name, classification_report(y_test, y_predict, target_names=['0 正常(非欺诈)', '1 代表欺诈'])))
    # print('%s模型的混淆矩阵为：\n%s' % (estimator_name, confusion_matrix(y_test, y_predict)))

    # 把这些输出数据保存在列表中: 最优分数、准确率、精确率、召回率、F1 score、训练时间
    e_bs = estimator.best_score_  # 最优分数
    e_bs = float('%.5f' % e_bs)
    e_ac = accuracy_score(y_test, y_predict)  # 准确率
    e_ac = float('%.5f' % e_ac)
    e_ps = precision_score(y_test,y_predict) # 精确率
    e_ps = float('%.5f' % e_ps)
    e_rs = recall_score(y_test, y_predict) # 召回率、
    e_rs = float('%.5f' % e_rs)
    e_fs = f1_score(y_test, y_predict) # F1 score
    e_fs = float('%.5f' % e_fs)
    e_tp = datetime.datetime.now() - time_start # 训练时间
    # 构建一个列表，并返回给外界使用
    list = [e_bs, e_ac, e_ps, e_rs, e_fs, e_tp]
    print(list)
    return list


huabei_wei()