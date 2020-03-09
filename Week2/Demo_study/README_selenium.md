### Selenium Web自动化程序 的知识总结：

### Selenium 原理与安装

    1。 Selenium 原理：
        * Selenium 是一个 Web 应用的自动化框架。
        * 通过它，我们可以写出自动化程序，像人一样在浏览器里操作web界面。 比如点击界面按钮，在文本框中输入文字 等操作。
        * 而且还能从web界面获取信息。比如获取12306票务信息，招聘网站职位信息，财经网站股票价格信息 等等，然后用程序进行分析处理。
        * 自动化程序（Selenium客户端库）<-> 浏览器驱动 <-> 浏览器（CHROME,FOX等）
        * 总结一下，selenium 自动化流程：
            A. 自动化程序调用Selenium 客户端库函数（比如点击按钮元素）
            B. 客户端库会发送Selenium 命令 给浏览器的驱动程序
            C. 浏览器驱动程序接收到命令后 ,驱动浏览器去执行命令
            D. 浏览器执行命令
            E. 浏览器驱动程序获取命令执行的结果，返回给我们自动化程序
            F. 自动化程序对返回结果进行处理
        
    2。 Selenium 安装：
        * Selenium环境的安装主要就是安装两样东西： 客户端库 和浏览器 驱动
        * 安装客户端库：pip install selenium
        * 安装浏览器驱动：在 help -> about google chrome -> 查看对应版本号
            A.（例：Version 80.0.3987.132 (Official Build) (64-bit)）
            B. 再去下载对应版本的浏览器驱动：https://chromedriver.storage.googleapis.com/index.html

### Selenium 选择元素的基本方法 
 
    1。在网页中，操控界面元素：
        * 对于百度搜索页面，如果我们想自动化输入 白月黑羽 ，怎么做呢？这就是在网页中，操控界面元素。
        * web界面自动化，要操控元素，首先需要 选择 界面元素 ，或者说 定位 界面元素，
        * 就是 先告诉浏览器，你要操作 哪个 界面元素， 让它找到你要操作的界面元素。
        * 我们必须要让浏览器 先找到元素，然后，才能操作元素。
    2。选择元素的方法：
        * 方法就是：告诉浏览器，你要操作的这个 web 元素的 特征 。
            A. 就是告诉浏览器，这个元素它有什么与众不同的地方，可以让浏览器一下子找到它。
        * 元素的特征怎么查看？
            A. 可以使用浏览器的 开发者工具栏 帮我们查看、选择 web 元素。按 fn + f12
            B. 右键点击元素， 选择 inspect
    3。根据 元素的id 属性选择元素：
        * 浏览器，找到id为kw的元素后，将结果通过 浏览器驱动 返回给 自动化程序， 
            A. 所以 find_element_by_id 方法会 返回一个 WebElement 类型的对象。
        * 这个WebElement 对象可以看成是对应 页面元素 的遥控器。
        * 我们通过这个WebElement对象，就可以 操控 对应的界面元素。
        * 比如 ：调用这个对象的 send_keys 方法就可以在对应的元素中 输入字符串，调用这个对象的 click 方法就可以 点击 该元素。
    4。根据 class属性、tag名 选择元素：
        * 元素也有类型， class 属性就用来标志着元素 类型 ，
            A. find_elements_by_class_name 方法返回的是找到的符合条件的 所有 元素 (这里有3个元素)， 放在一个 列表 中返回。
            B. 而如果我们使用 find_element_by_class_name (注意少了一个s) 方法， 就只会返回 第一个 元素。
    5。find_element 和 find_elements 的区别：
            A. 使用 find_elements 选择的是符合条件的 所有 元素， 如果没有符合条件的元素， 返回空列表
            B. 使用 find_element 选择的是符合条件的 第一个 元素， 如果没有符合条件的元素， 抛出 NoSuchElementException 异常
    6。等待界面元素出现:NoSuchElementException 的意思就是在当前的网页上 找不到该元素， 就是找不到 id 为 1 的元素。
        * 为什么呢？因为我们的代码执行的速度比 百度服务器响应的速度 快
        * 设置最大等待时长为 10秒   wd.implicitly_wait(10)
        
### 操控元素的基本方法
    
    1. 选择到元素之后，我们的代码会返回元素对应的 WebElement对象，通过这个对象，我们就可以 操控 元素了。
    2. 操控元素通常包括:
        A. 点击元素: 调用元素WebElement对象的 click方法
        B. 在元素中输入字符串，通常是对输入框这样的元素: 调用元素WebElement对象的send_keys方法
        C. 获取元素包含的信息，比如文本内容，元素的属性: 
            通过WebElement对象的 text 属性，可以获取元素 展示在界面上的 文本内容。
            通过WebElement对象的 get_attribute 方法来获取元素的属性值，
            
### CSS  表达式选择元素
    
    1。 CSS Selector 语法选择元素原理： 例： .animal {color : red; background-color: red;} 
        * 既然 CSS Selector 语法 天生就是浏览器用来选择元素的，selenium自然就可以使用它用在自动化中，去选择要操作的元素了。
        * 只要 CSS Selector 的语法是正确的， Selenium 就可以选择到该元素。
    2. CSS Selector 选择子元素的语法: 元素1 > 元素2 > 元素3 > 元素4
    3. CSS Selector 选择后代元素的语法(中间是一个或者多个空格隔开,最终选择的元素是 元素4): 元素1   元素2   元素3  元素4

### 参考学习资源
    
    1。 （白月黑羽教Python：文本教程）http://www.python3.vip/doc/tutorial/selenium/01/
    2。 （爬虫解析库：XPath）https://www.jianshu.com/p/85a3004b5c06
    3。 （selenium--浏览器滚动条操作）https://www.cnblogs.com/zouzou-busy/p/11179068.html
