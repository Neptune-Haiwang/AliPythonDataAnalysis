import requests, json, time, os, csv
import pandas as pd


# 存储想要查询的职位关键词列表：可以继续添加
keywords = ['后台开发', '自然语言处理', '产品经理']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}


def get_page_link(keyword):
    '''
    构造搜索一个关键词的真正的动态的json数据的请求链接
    https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1586499083819&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=自然语言处理&pageIndex=1&pageSize=10&language=zh-cn&area=cn
    @param keyword:  要查询的关键词
    @return: 以列表形式 返回关键词对应的json数据的请求链接
    '''
    base_src = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    src_list = []
    for i in range(10): # 每个页面有10个招聘岗位信息
        # 动态时间戳的处理
        src = base_src.format(int(time.time())*1000, keyword, (i+1))
        src_list.append(src)
    # print(src_list)
    return src_list


# 获取职位的相关信息
def get_job_info(keyword):
    '''
    根获取对应的岗位信息
    @param keyword: 要查询的关键词
    存储一个关键词对应的招聘岗位信息的csv文件
    '''
    src_links = get_page_link(keyword)
    jobs_result = []
    for src in src_links[0:5]: # 取前5个页面的25条数据
        response = requests.get(url=src, headers= headers).content.decode('utf-8')
        # 获取json格式的数据{"Code":200,"Data":{"Count":516,"Posts":[{...},{...}]}}
        json_datas = json.loads(response)['Data']['Posts']
        for j in json_datas:
            job = {}
            job['job_title'] = j['RecruitPostName']
            job['job_country'] = j['CountryName']
            job['job_city'] = j['LocationName']
            job['job_category'] = j['CategoryName']
            job['job_responsibility'] = j['Responsibility']
            job['job_available'] = j['IsValid']
            jobs_result.append(job)
    df = pd.DataFrame(jobs_result)
    path = './data/{}.csv'.format(keyword)  # 要存储路径
    with open(path, 'w', encoding='utf-8') as f:
        fieldnames = ['job_title', 'job_country', 'job_city', 'job_category', 'job_responsibility', 'job_available']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    df.to_csv(path, mode='a+', header=None, encoding='utf-8')   # 采用追加的方式存储数据


if __name__=='__main__':
    for i in keywords:
        get_job_info(i)

