from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np


contents = ['ios', 'web', '不断', '业务', '优化', '内容', '前端', '包括', '增值', '完善', '小游戏', '工作', '开发', '微信', '性能', '提升', '框架', '浏览器', '游戏', '相关', '精品', '终端', '自己', '质量', '运行', '需求']


def text1():
    countVectorizer = CountVectorizer()
    textVector = countVectorizer.fit_transform(contents)
    textVector.todense()
    countVectorizer.vocabulary_

    countVectorizer = CountVectorizer(min_df = 0, token_pattern= r"\b\w+\b")
    textVector = countVectorizer.fit_transform(contents)
    textVector.todense()
    countVectorizer.vocabulary_

    transformer = TfidfTransformer()
    tfid = transformer.fit_transform(textVector)

    TFIDFDataFrame = pd.DataFrame(tfid.toarray())
    TFIDFDataFrame.columns = countVectorizer.get_feature_names()
    TFIDFSorted = np.argsort(tfid.toarray(),axis=1)[:,-2:]

    TFIDFDataFrame.columns[TFIDFSorted].values
    print (TFIDFDataFrame)



text1()
# print(contents)

