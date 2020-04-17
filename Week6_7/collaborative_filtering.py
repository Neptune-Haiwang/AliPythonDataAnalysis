import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def jobs_courses_matching():

    # 给工作推荐课程
    # 1 加载数据: 只选择 name 与 关键词
    jobs_data = pd.read_csv('./Jobs_Courses_Datas/jobs_data_processed.csv', usecols=['Job_Title', 'Job_Keywords_List'])
    courses_data = pd.read_csv('./Jobs_Courses_Datas/courses_data_processed.csv', usecols=['Course_Name', 'Course_Keywords_List'])
    # 1.1 选取一定比例的数据做匹配推荐
    jobs_data = pd.DataFrame.sample(jobs_data, frac=0.2, random_state=1)
    courses_data = pd.DataFrame.sample(courses_data, frac=0.2, random_state=1)
    # 1.2 统计唯一的课程与岗位信息的数量：
    n_jobs = jobs_data['Job_Title'].unique().shape[0]
    n_courses = courses_data['Course_Name'].unique().shape[0]
    print('职位数为：%s， 课程数为：%s' % (n_jobs, n_courses))

    # https://blog.csdn.net/m0_38045485/article/details/81174685
    # https://blog.csdn.net/yangyang_yangqi/article/details/82782361



    return None


if __name__=='__main__':
    jobs_courses_matching()
