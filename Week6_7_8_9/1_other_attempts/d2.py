import numpy as np
from Week6_7_8_9.cosine_similarity import calculate_similarity


vec_total = [[1,0,0,18,1,2,2,0,0,1],
             [0,0,1,1,1,10,2,0,0,1],
             [2.3,0,0,1,1,0,2,0,0,1],
             [1,0,0,3,1,2,2,0,0,9],
             [0,0,0,7,1,2,2,0,0,1]]
result = []
for i in range(len(vec_total)):
    t = calculate_similarity(vec_total[i], vec_total[i+1])
    result.append(t)

result.sort(reverse=True)
r_dic = set(result)
r_new = list(r_dic)
print(r_dic[:3])

