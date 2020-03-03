任务：用python去豆瓣电影这个网站把”成龙“的相关海报抓取下来

任务分解：写一个 python爬虫的脚本， 去豆瓣电影，爬取 名字里含有 “成龙” 的海报照片


具体分析：
    1。请求网页：用 response.get(）获得， 如果有反爬虫， 则可以重新定义 headers 中的 User agent

    2。 翻页问题：https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=0
                https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=15
                https://search.douban.com/movie/subject_search?search_text=成龙&cat=1002&start=30
            总共有19个 url 页面
        浏览器中的url 变化， start 控制每个页面显示的电影数，以 15 个为步长
        可以使用正则表达式 获得一个 urls 列表

    3。 每个页面里的问题：
                <a href="https://movie.douban.com/subject/26654146/" data-moreurl="onclick=&quot;moreurl(this,{i:'32',query:'%E6%88%90%E9%BE%99',subject_id:'26654146',from:'mv_subject_search',is_tv:'0'})&quot;" class="cover-link">
                <img src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2503544593.jpg" alt="解忧杂货店‎ (2017)" class="cover"></a>
            每个页面里有 15 个 src 电影海报
        在这样的 img 标签里有每个海报图片的 src 链接
        可以使用正则表达式 获得一个 srcs 列表

    4。 下载与保存海报：
            对获得到的 urls 列表循环， 获取其中的每一个 srcs 小列表元素，
            在对 srcs 小列表中的每一个 src 遍历：用 response.get 来获得 url， 再把获得到的 src内容保存到文件里

