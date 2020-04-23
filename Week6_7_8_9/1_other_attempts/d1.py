import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.preprocessing import MinMaxScaler


v1 = [1,0,0,1,1,2,2,0,0,1]
v2 = [0,1,0,1,1,2,2,0,0,0]
a = np.array(v1)
b = np.array(v2)
sim1 = pearsonr(a, b)[0]
print(sim1)

sim2 = spearmanr(a,b)[0]
print(sim2)
s = (sim1 + sim2) / 2
print(s)

# # 使用标准化来把数据进行压缩到0, 1的区间 -> 无用的操作，因为向量缩放，夹角余弦值不变
scaler = MinMaxScaler()
vec1 = a.reshape(-1, 1)
vec2 = b.reshape(-1, 1)
vec1 = scaler.fit_transform(vec1)
vec2 = scaler.fit_transform(vec2)
