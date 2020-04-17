import pandas as pd
import numpy as np


# Series的创建、Series的属性
def series_simple():
    p1 = pd.Series(np.arange(9))    # 指定内容，默认索引
    # print(p1)
    p2 = pd.Series(data=[6.7,5.6,3,10,2], index=[1,2,3,4,5])    # 指定索引
    # print(p2)
    p3 = pd.Series({'red':10, 'green': 20, 'blue': 50})     # 通过字典数据创建
    # print(p3)

    print(p3.index)
    print(p3.values)
    print(p3[1])


# DataFrame创建、DataFrame的属性
def dataframe_simple():
    score = np.random.randint(40, 100, (10, 5))
    score_df = pd.DataFrame(score)
    # print(score_df)
    subjects = ["语文", "数学", "英语", "政治", "体育"]
    stu = ['同学' + str(i) for i in range(score_df.shape[0])]
    data = pd.DataFrame(data=score, columns=subjects, index=stu)
    # print(data)
    # print(data.shape)
    # print(data.index)
    # print(data.columns)
    # print(data.values)
    # print(data.T)
    # print(data.head(3))
    # print(data.tail(3))

    # DatatFrame索引的设置
    # stu1 = ['同学_' + str(i) for i in range(score_df.shape[0])]
    # data.index = stu1
    # print(data)
    # 重设索引
    # data.reset_index(drop=True)
    # print(data)

    # 以某列值设置为新的索引
    df = pd.DataFrame({'month': [1, 4, 7, 10],
                       'year': [2012, 2014, 2013, 2014],
                       'sale': [55, 40, 84, 31]})
    # df.set_index('month')   # 以月份设置新的索引
    # print(df)
    df = df.set_index(['year', 'month'])    # 设置多个索引，以年和月份. 这样DataFrame就变成了一个具有MultiIndex的DataFrame。
    print(df)


if __name__ == '__main__':
    # series_simple()
    dataframe_simple()
