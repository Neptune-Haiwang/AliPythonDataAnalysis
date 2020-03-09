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
    
### xpath 语法简要
   
    3。根据 xpath 方法：XPath，全称 XML Path Language，即 XML 路径语言，它是一门在 XML 文档中查找信息的语言。最初是用来搜寻 XML 文档的，但同样适用于 HTML 文档的搜索。
        * 安装方法： pip install lxml
        * 常用规则：   表达式	          描述
                    nodename        选取此节点的所有子节点
                    /	            从当前节点选区直接子节点
                    //	            从当前节点选取子孙节点
                    .	            选取当前节点
                    ..	            选取当前节点的父节点
                    @	            选取属性
        * 绝对路径： elements = driver.find_elements_by_xpath("/html/body/div")
        * 相对路径： elements = driver.find_elements_by_xpath("//div//p")
        * 根据属性选择：根据属性来选择元素 是通过 这种格式来的 [@属性名='属性值']
            如果一个元素class 有多个，比如：<p id="beijing" class='capital huge-city'>北京 </p>
            如果要选 它， 对应的 xpath 就应该是 //p[@class="capital huge-city"]
        * 属性值包含字符串：
            A. 要选择 style属性值 包含 color 字符串的 页面元素 ，可以这样 //*[contains(@style,'color')]
            B. 要选择 style属性值 以 color 字符串 开头 的 页面元素 ，可以这样 //*[starts-with(@style,'color')]
        * 范围选择：xpath还可以选择子元素的次序范围。
            选择class属性为multi_choice的后3个子元素：//*[@class='multi_choice']/*[position()>=last()-2]
            要选所有的 class 为 single_choice 和 class 为 multi_choice 的元素：//*[@class='single_choice'] | //*[@class='multi_choice']
                        等同于CSS选择器：  .single_choice , .multi_choice
        
        * 例子：//title[@lang='eng']       这是一个 XPath 规则，代表的是选择所有名称为 title，同时属性 lang 的值为 eng 的节点，
                后面会通过 Python 的 lxml 库，利用 XPath 进行 HTML 的解析。
        * 补充：* 代表匹配所有节点，返回的结果是一个列表
        * 复杂用法展示：
            A. 有重复的class属性无法区分时，选择对应的顺序（1，2，3,,）满足的 element返回：  wd.find_element_by_xpath('//div[@class="toolbar_menu_list m-box-col m-box-center m-box-center-a"][1]').click()
            B. 从一个大的div层级下进行选择后，再继续向下选择：    wd.find_element_by_xpath('//div[@class="m-pop m-pop-s"]//ul/li[2]/div[@class="m-diy-btn m-box-col m-box-center m-box-center-a"]').click()
            C. 和 format 一起的综合使用方法：  xpath_here = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]".format(weibo_no)
        * 等待界面元素出现的方法： 
            A. # 设置最大等待时长为 5 秒：     wd.implicitly_wait(5)
            B. 设置延时操作：      time.sleep(1)    

### css 语法简要

    1。CSS Selector 语法选择元素：例： .animal {color : red; background-color: red;} 
        * CSS selector的另一个强大之处在于： 选择语法 可以 联合使用
        * 要选择 所有的tag名为div的元素： elements = wd.find_elements_by_css_selector('div')
        * 根据id属性：<input  type="text" id='searchtext' /> 则：element = wd.find_element_by_css_selector('#searchtext')
        * 要选择 网页 html 中的元素 <span class='copyright'>版权</span>
                <div id='bottom'>
                    <div class='footer1'>
                        <span class='copyright'>版权</span>
                        <span class='date'>发布日期：2018-03-03</span>
                    </div>
                    <div class='footer2'>
                        <span>备案号
                            <a href="http://www.miitbeian.gov.cn">苏ICP备88885574号</a>
                        </span>
                    </div>        
                </div>    
            A. CSS selector 表达式 可以这样写：  div.footer1 > span.copyright
            B. 也可以更简单：  .footer1 > .copyright
        
        * 示例：直接找到对应的CSS属性
            A. wd.find_element_by_css_selector('span[class="m-wz-def"]').click()
            B. 根据属性选择元素：element = wd.find_element_by_css_selector('[href="http://www.miitbeian.gov.cn"]')
            C. 当然，前面可以加上标签名的限制，比如 div[class='SKnet'] 表示 选择所有 标签名为div，且class属性值为SKnet的元素。
    
    2。xpath 与 css 用法对比的进一步补充：
        * elements = driver.find_elements_by_xpath("//div//p") 等价于 elements = driver.find_elements_by_css_selector("div p")
    
### 补充：浏览器滚动条操作
    
    1。浏览器滚动条操作：在进行web自动化的时候，selenium只能找当前屏幕上的标签，
        如果标签在当前页面没显示下，需要拖动滚动条才能查看到这个元素，这时候就要操作浏览器的滚动条，让当前页面显示这个元素才可以操作
            xpath_here = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]".format(weibo_no)
            specific_weibo = wd.find_element_by_xpath(xpath_here)
            js = 'arguments[0].scrollIntoView();'   # 操作浏览器向下滑动到指定的div区域
            wd.execute_script(js, specific_weibo)       

### 本次任务的重难点再梳理
    
    1。使用 xpath 和 css selector 语法 选择到指定的元素，注意格式的书写。
    2。加关注，取消关注时 的弹窗处理要注意
    3。找指定微博时，对浏览器页面滑动到指定微博内容时的处理，要用到 javascript 交给 webdriver 去执行         

### 参考资源
    
    1。Python + Selenium Web自动化 全套教程：https://www.bilibili.com/video/av64421994
    2。 白月黑羽教Python：  http://www.python3.vip/doc/tutorial/selenium/01/
    3。 爬虫解析库：XPath： https://www.jianshu.com/p/85a3004b5c06
    4。 selenium--浏览器滚动条操作：  https://www.cnblogs.com/zouzou-busy/p/11179068.html
