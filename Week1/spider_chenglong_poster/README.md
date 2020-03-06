###任务：
    1. 用python去豆瓣电影这个网站把”成龙“的相关海报抓取下来
    
    2. 任务分解：写一个 python爬虫的脚本， 去豆瓣电影，爬取 名字里含有 “成龙” 的海报照片

###具体分析：
    1。什么是爬虫：爬虫实际上是用浏览器访问的方式模拟了访问网站的过程，整个过程包括三个阶段：打开网页、提取数据和保存数据
        * 打开网页：Requests， 发送HTTP请求：
            A. request主要分GET和POST
            B. 用法分分别是：r = requests.get('http://www.douban.com')
                和r = requests.post('http://xxx.com', data = {'key':'value'})
        * 提取数据： 如果是 HTML 页面，可以使用 XPath 进行元素定位，提取数据；如果是JSON 数据，可以使用 JSON 进行解析
        * 保存数据： 可以使用 Pandas 保存数据，最后导出 CSV 文件
        
    2。 XPath知识补充：XPath 是 XML 的路径语言，实际上是通过元素和属性进行导航，帮我们定位位置。它有几种常用的路径表达方式。
            简单举一些例子：1.xpath(‘node’) 选取了 node 节点的所有子节点；
                          2.xpath(’/div’) 从根节点上选取 div 节点；
                          3.xpath(’//div’) 选取所有的 div 节点；  剩余的你网上可以查
                          
    3。 JSON 是一种轻量级的交互方式 就比较简单了 将 JSON 对象直接转换成为 Python 对象，我们对数据进行解析就更方便 我们一般用json库

###谷歌开发者工具的了解：
    1。 在chrome开发者工具里面监控 输入人名后网络流的全过程 https://www.douban.com/search?cat=1025&q=
        在 inspect -> network -> XHR 里，找到对应的 name 可以复制链接， 在下买你的
            A. headers 查看网络请求内容, 
            B. response 查看JSON格式的数据

###豆瓣网站的深入了解：
    1。 JSON数据的格式：
        {"images":[{"src":"https://img9.doubanio.com\/view\/photo\/photo\/public\/p2237159394.jpg",
                        "author":"一二三四五六","url":"https:\/\/www.douban.com\/link2\/?url=http%3A%2F%2Fwww.douban.com%2Fphotos%2Fphoto%2F2237159394%2F&query=%E6%88%90%E9%BE%99&cat_id=1025&type=search",
                        "id":"2237159394","title":"永远的邓丽君","width":400,"height":421},...
    
    2。 URL链接的构造形式：
        https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=0
        https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=20
        https://www.douban.com/j/search_photo?q=%E6%88%90%E9%BE%99&limit=20&start=40
        找到页面和URL之间的对应规律：1   2   3
        最后的start控制步长：       0   20  40

###网站参考资源：
    1。 https://blog.csdn.net/qq_43659281/article/details/86528921
    
    2。 https://www.cnblogs.com/hexia7935/p/9960368.html
    
    3。 https://blog.csdn.net/fei347795790/article/details/101696368
    
    4: B站爬虫知识学习资源：https://www.bilibili.com/video/av9784617?from=search&seid=12110687049083554443
