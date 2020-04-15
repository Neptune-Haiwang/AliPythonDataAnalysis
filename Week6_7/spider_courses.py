import requests, csv, time, random
from lxml import etree
import pandas as pd


def get_page_url():
    '''
    根据页码数构造链接
    @return:
    '''
    # http://www.xuetangx.com/courses?credential=0&page_type=0&cid=0&process=0&org=0&course_mode=0&page=2
    # http://www.xuetangx.com/courses?credential=0&page_type=0&cid=0&process=0&org=0&course_mode=0&page=3
    base_url = 'http://www.xuetangx.com/courses?credential=0&page_type=0&cid=0&process=0&org=0&course_mode=0&page={}'
    url_list = []
    # 对92个页面进行循环，
    for i in range(92):
        url = base_url.format(i+1)
        url_list.append(url)
    # print(url_list)
    return url_list


def get_course_info(src, path):
    '''
    获取某门课程的课程名称以及课程描述
    每个页面有10个课程
    @return:
    '''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3)'}
    response = requests.get(src, headers=headers).content.decode('utf-8')
    # print(response)
    content = etree.HTML(response)
    # 一个页面上的10条课程数据
    course_results = []
    url_lists = get_page_url()
    for i in range(10):
        course = {}
        course_name= content.xpath('//li[{}]//div[@class="coursename"]//h2/text()'.format(i+1))
        if len(course_name) > 0:
            course['course_name'] = course_name[0]
        course_description = content.xpath('//li[{}]//div[@class="coursename"]//p[1]/text()'.format(i+1))
        course['course_description'] = course_description
        # print(course)
        course_results.append(course)
    df = pd.DataFrame(course_results)
    # 追加内容，不要索引
    df.to_csv(path, index=None, mode='a+', header=None, encoding='utf-8')
    return None


def save_all_courses(path):
    # 创建表头
    with open(path, 'w', encoding='utf-8') as f:
        fieldnames = ['course_name', 'course_description']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
    # 递归对所有页面链接执行操作
    for u in get_page_url():
        get_course_info(u, path=path)
        time.sleep(random.randint(1, 2))
    return None


if __name__=='__main__':
    path = './Jobs_Courses_Datas/courses_data.csv'  # 文件的存储路径
    save_all_courses(path=path)
