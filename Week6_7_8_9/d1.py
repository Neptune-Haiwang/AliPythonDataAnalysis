import pandas as pd
import numpy as np

courses_data = pd.read_csv('./Jobs_Courses_Datas/courses_data.csv')

# courses_data = courses_data.dropna()
q = courses_data[courses_data.isna().T.any()]
print(q)
