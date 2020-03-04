import requests
import os
import shutil
import subprocess
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) ''AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'
}

# 下载并保存单个海报
def download_poster(image_src, image_localpath):
    response = requests.get(image_src, stream=True)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)

# 从单个页面中获取 海报图片
def get_poster_of_the_page(page):
    page_flag = str(15 * (page - 1))
    """
    https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=0
    https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=15
    https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=30
    # 根据页数构造对应的URL: 1, 2,  3,  4
    # {} 里的数字分别是：    0, 15, 30, 45
    
    """
    # 构造不同页面对应的url链接
    url = "https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start={}".format(page_flag)
    print("get movie of the page {}".format(page))
    print(url)
    response = requests.get(url, headers=headers)
    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')
    # 找到对应的div层的内容
    get_content = soup.find_all('a', class_='cover-click')
    for pic_href in get_content:
        # 找到img 标签的内容
        for pic in pic_href.find_all('img'):
            img_src = pic.get('src')
            # print(img_src)
            # 设置保存路径
            dir = os.path.abspath('.')
            data_path = dir + "/data"
            # print(data_path)
            file_name = os.path.basename(img_src)
            img_path = os.path.join(data_path, file_name)
            print('开始下载 %s' % img_src)
            download_poster(img_src, img_path)

# 指定需要下载的页数
for page in range(1, 4):
    get_poster_of_the_page(page)

