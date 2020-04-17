import jieba, csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer



def extract_keywords(text_data, stop_words):
    '''
    用tf-idf法抽取关键词
    @param text_data: 初始的文本数据
    @param top_n: 每个item要抽取出的关键词数量，（取前N个）
    @return: 某一项数据的关键词列表
    '''
    words_list = []
    # 使用进行 jieba 中文分词
    word = " ".join(list(jieba.cut(text_data)))
    # # 取掉单字词
    # if len(word) > 1:
    #     words_list.append(word)
    words_list.append(word)
    # 挑选关键词
    tv = TfidfVectorizer(stop_words=stop_words)
    tv_fit = tv.fit_transform(words_list)
    # 特征词
    t_feature_names = tv.get_feature_names()
    # 特征词的TFIDF权重值
    # t_weights = tv_fit.toarray()
    item_keywords= []
    # # 以 权重值 为指标对特征词进行降序排序，从而可以取得最重要的top N 关键词
    # # zip 打包中的数据：索引0： t_feature_names； 索引1： t_weights
    # sorted_keywords = sorted(zip(t_feature_names, t_weights), key=lambda x:x[1], reverse=True)
    # print(sorted_keywords)
    # # top N 关键词列表为前n项的数据
    # item_keywords = [w[0] for w in sorted_keywords[: top_n]]
    item_keywords.append(t_feature_names)
    # print(item_keywords)
    return item_keywords



def course_preprocessing(path_course, path_course_processed, stop_words):
    '''
    # 对课程信息的关键词提取
    @param path_course: 原始数据地址
    @param path_course_processed: 处理后的数据的保存地址
    @return: None
    '''
    # 1 数据清洗
    courses_data = pd.read_csv(path_course)
    # print(courses_data.shape[0])
    # print(np.any(pd.isnull(courses_data)))
    # 查找到所有缺失值的位置：
    # courses_data[courses_data.isnull().values==True].drop_duplicates()
    # 删除掉所有缺失值的行
    courses_data_processed = courses_data.dropna()
    # print(courses_data_new.shape[0])
    # courses_data_processed.set_index('course_name')
    # 2 数据关键词获取
    course_keywords_list = []
    for i in range(courses_data_processed.shape[0]):
        # 替换掉奇怪的符号
        c_info_data = courses_data_processed.iloc[i, 1].replace('\\n', '').replace('\\t', '').replace('\\xa0', '')\
            .replace('\\r', '').replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', '')
        c_keywords = extract_keywords(c_info_data, stop_words=stop_words)

        course_keywords_list.append(c_keywords)
    courses_data_processed.insert(2, 'course_keywords_list', course_keywords_list)
    # print(courses_data_new.head())

    # 3 写入新文件
    with open(path_course_processed, 'w', encoding='utf-8') as f:
        fieldnames = ['Course_Name', 'Course_Description', 'Course_Keywords_List']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    courses_data_processed.to_csv(path_course_processed, index=None, mode='a+', header=None, encoding='utf-8')

    return None


def jobs_preprocessing(path_jobs, path_jobs_processed, stop_words):
    '''
    对岗位信息的关键词提取
    @param path_jobs:
    @param path_jobs_processed:
    @param stop_words:
    @return:
    '''
    # 1 数据清洗
    jobs_data = pd.read_csv(path_jobs)
    # print(jobs_data.head())
    # print(np.any(pd.isnull(jobs_data))) # 判断是否有缺失值 返回True则说明有缺失值 此处返回false，说明没有缺失值
    # 2 数据关键词获取
    jobs_keywords_list = []
    for i in range(jobs_data.shape[0]):
        # 替换掉奇怪的符号
        j = jobs_data.iloc[i, 1].replace('\\n', '').replace('\\t', '').replace('\\xa0', '')\
            .replace('\\r', '').replace('\n', '').replace('\t', '').replace('\r', '').replace('\xa0', '')
        j_keywords = extract_keywords(j, stop_words= stop_words)
        jobs_keywords_list.append(j_keywords)
    jobs_data_processed = jobs_data
    jobs_data_processed.insert(2, 'jobs_keywords_list', jobs_keywords_list)
    # print(jobs_data_processed.head())
    # 3 写入新文件
    with open(path_jobs_processed, 'w', encoding='utf-8') as f:
        fieldnames = ['Job_Title', 'Job_Responsibility', 'Job_Keywords_List']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    jobs_data_processed.to_csv(path_jobs_processed, index=None, header=None, mode='a+', encoding='utf-8')

    return None



if __name__=="__main__":
    # 从文件导入停用词表
    stop_words_dic = open('./stop_words.txt', 'rb')
    stop_words = stop_words_dic.read().splitlines()
    stop_words_dic.close()

    path_course = './Jobs_Courses_Datas/courses_data.csv'
    path_course_processed = './Jobs_Courses_Datas/courses_data_processed.csv'
    course_preprocessing(path_course, path_course_processed, stop_words)

    path_jobs = './Jobs_Courses_Datas/jobs_data.csv'
    path_jobs_processed = './Jobs_Courses_Datas/jobs_data_processed.csv'
    jobs_preprocessing(path_jobs, path_jobs_processed, stop_words)
