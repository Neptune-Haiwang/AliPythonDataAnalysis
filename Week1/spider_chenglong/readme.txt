任务：用python去豆瓣电影这个网站把”成龙“的相关海报抓取下来

任务分解：写一个 python爬虫的脚本， 去豆瓣电影，爬取 名字里含有 “成龙” 的海报照片


具体步骤：
1。 请求网页
    需要导入 request库， 如果有反爬虫， 可以另外定义 headers，告诉浏览器自己不是爬虫

2。 解析网页并正则匹配“成龙”
    url 的名字 使用找到的 a 标签
        <img src="https://img1.doubanio.com/view/celebrity/s_ratio_celebrity/public/p1537891305.49.jpg" alt="成龙 Jackie Chan" class="cover">
    导入re 库，使用正则匹配：相似的保留，需要匹配的用 （.*?）来替代， 可以得到很多 含有成龙的 url

3。 把匹配到的图片保存到文件夹
    创建一个新文件夹
    使用for 循环遍历 正则查找到的链接们，
    获取到这些链接，再写入到创建好的文件夹中

