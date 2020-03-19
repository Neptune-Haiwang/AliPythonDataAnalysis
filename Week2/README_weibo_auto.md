### 任务安排及说明
    1。 数据采集的任务 : 编写微博自动化功能模块：登录微博；查找用户：加关注，写评论，取关； 回自己主页发微博

### selenium 工具包介绍

    1。Selenium 是一个 Web 应用的自动化框架。
        * 通过它，我们可以写出自动化程序，像人一样在浏览器里操作web界面。 比如点击界面按钮，在文本框中输入文字 等操作。
        * 而且还能从web界面获取信息。
    2。自动化程序（Selenium客户端库）<-> 浏览器驱动 <-> 浏览器（CHROME,FOX等）
    3。Selenium 安装：
        * Selenium环境的安装主要就是安装两样东西： 客户端库 和浏览器 驱动
    4。安装客户端库：pip install selenium
    5。安装浏览器驱动：在 help -> about google chrome -> 查看对应版本号
        *（例：Version 80.0.3987.132 (Official Build) (64-bit)）
        * 再去下载对应版本的浏览器驱动：https://chromedriver.storage.googleapis.com/index.html

### selenium 选择与操作元素

    1。在网页中，操控界面元素：我们必须要让浏览器 先找到元素，然后，才能操作元素。
    2。选择与操作元素的方法：告诉浏览器，你要操作的这个 web 元素的 特征：
    3。操控元素的基本方法：选择到元素之后，我们的代码会返回元素对应的 WebElement对象，通过这个对象，我们就可以 操控 元素了。
        * 点击操作：click方法
        * 输入操作：send_keys方法
        * 获取属性内容：text 属性可以获取元素 展示在界面上的 文本内容、get_attribute 方法来获取元素的属性值。
    4。 等待界面元素出现的方法： 
        A. # 设置最大等待时长为 5 秒：     wd.implicitly_wait(5)
        B. 设置延时操作：      time.sleep(1) 
    5。浏览器滚动条操作：在进行web自动化的时候，selenium只能找当前屏幕上的标签，
        如果标签在当前页面没显示下，需要拖动滚动条才能查看到这个元素，这时候就要操作浏览器的滚动条，让当前页面显示这个元素才可以操作
            xpath_here = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]".format(weibo_no)
            specific_weibo = wd.find_element_by_xpath(xpath_here)
            js = 'arguments[0].scrollIntoView();'   # 操作浏览器向下滑动到指定的div区域
            wd.execute_script(js, specific_weibo)     
    
### xpath 语法简要
   
    1. 用 command + f 查找， 输入对应的xpath看是否可以查找对应到该标签
    2。 xpath 语法分为三大类：
        * 层级：/ 直接层级     //跳级
        * 属性：@ 属性访问
        * 函数：contains()     text() 
    3。示例讲解：
        //div[@class="opr-recommends-merge-content"]//div[contains(@class, "opr-recommends-merge-item")]
        拆解分析：
            * 首先：跳级选中： //div[@class="opr-recommends-merge-content"]
            * 然后，继续跳级选中：//div[contains(@class, "opr-recommends-merge-item")]
                其中，contains（）方法表示，class里只是包含了一段 "opr-recommends-merge-item"
    4。一个复杂的XPATH选择示例：：
        //div[@class="result-op xpath-log"]//div[@class="FYB_RD"]//tbody[1]/tr[3]/td[1]//a[contains(@target, "blank")]
    5。 复杂用法 -> 和 format 一起的综合使用方法：
        xpath_here = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]".format(weibo_no)   

### css Selector 语法简要

    1。CSS Selector 语法选择元素：例： .animal {color : red; background-color: red;} 
        * CSS selector的另一个强大之处在于： 选择语法 可以 联合使用
    2。要选择 所有的tag名为div的元素： elements = wd.find_elements_by_css_selector('div')
    3。根据id属性：<input  type="text" id='searchtext' /> 则：element = wd.find_element_by_css_selector('#searchtext')        
    4。 示例：直接找到对应的CSS属性
        A. wd.find_element_by_css_selector('span[class="m-wz-def"]').click()
        B. 根据属性选择元素：element = wd.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')
        C. 当然，前面可以加上标签名的限制，比如 div[class='SKnet'] 表示 选择所有 标签名为div，且class属性值为SKnet的元素。
    5。xpath 与 css 用法对比的进一步补充：
        * elements = driver.find_elements_by_xpath("//div//p") 等价于 elements = driver.find_elements_by_css_selector("div p")

### 本次任务的重难点再梳理
    
    1。使用 xpath 和 css selector 语法 选择到指定的元素，注意格式的书写。
    2。加关注，取消关注时 的弹窗处理要注意
    3。找指定微博时，对浏览器页面滑动到指定微博内容时的处理，要用到 javascript 交给 webdriver 去执行         

### 参考资源
    
    1。Python + Selenium Web自动化 全套教程：https://www.bilibili.com/video/av64421994
    2。 白月黑羽教Python：  http://www.python3.vip/doc/tutorial/selenium/01/
    3。 爬虫解析库：XPath： https://www.jianshu.com/p/85a3004b5c06
    4。 selenium--浏览器滚动条操作：  https://www.cnblogs.com/zouzou-busy/p/11179068.html
