from selenium import webdriver
import time

# 实例化浏览器驱动
wd = webdriver.Chrome(r'/Users/haiwangluo/Downloads/chromedriver')
# 设置最大等待时长为 5 秒
wd.implicitly_wait(5)


def login_weibo(usr_name, usr_passwd):
    """1. 登录微博的方法

    @param usr_name: 登录微博的用户名
    @param usr_passwd: 登录微博的密码
    """
    # 给定访问目标
    wd.get('https://passport.weibo.cn/signin/login')

    # 根据id查找文本输入框，并填入内容
    wd.find_element_by_id('loginName').send_keys(usr_name)
    wd.find_element_by_id('loginPassword').send_keys(usr_passwd)
    # 根据id查找登录按钮，并执行点击登录操作
    wd.find_element_by_id('loginAction').click()


def follow_comment_a_user(keyword_id, weibo_no, comment_content):
    """2。关注用户，处理弹窗，找到对应的微博，定位到对应评论区并添加评论

    @param keyword_id: 需要查找的用户的微博主页的编号
    @param weibo_no: 需要回复的对应的第几条微博编号
    @param comment_content: 需要添加评论的内容
    """
    wd.get('https://m.weibo.cn/u/' + keyword_id)
    # 关注该用户， 使用xpath定位路径，xpath的使用方法见 README_WEEK2.md
    wd.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]').click()
    time.sleep(1)

    # 处理弹窗,点击对应的取消按钮
    wd.find_element_by_xpath('//a[@class="m-btn m-btn-white m-btn-text-black"]').click()
    time.sleep(1)

    # 找到此用户 的第 weibo_no 条微博
    xpath_here = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]".format(weibo_no)
    specific_weibo = wd.find_element_by_xpath(xpath_here)

    # 操作浏览器向下滑动到指定的div区域, 操纵滑动条的实现方法见 README_WEEK2.md
    js = 'arguments[0].scrollIntoView();'
    wd.execute_script(js, specific_weibo)

    # 定位到对应微博并定位到评论的按钮，并点击进入评论区， \ 符号为转义字符
    xpath_selector = "//div[@class='card m-panel card9 weibo-member card-vip'][{}]" \
                     "//footer/div[@class='m-diy-btn m-box-col m-box-center m-box-center-a'][2]".format(weibo_no)
    comment_element = wd.find_element_by_xpath(xpath_selector)
    comment_element.click()

    # 发表评论
    # 使用 CSS选择器 定位到 发表评论 的位置，并点击
    wd.find_element_by_css_selector('span[class="m-box-center-a main-text m-text-cut focus"]').click()
    # 点击评论
    comment = wd.find_element_by_tag_name('textarea')
    comment.click()
    # 输入评论内容
    comment.send_keys(comment_content)
    # 定位到发送按钮,并点击 发表评论
    wd.find_element_by_class_name('btn-send').click()


def unfollow_a_user(keyword_id):
    """3.  取关用户

    @param keyword_id: 与关注某用户的id 一致，是该用户的微博主页的编号
    """
    # 进入到该用户的微博主页
    wd.get('https://m.weibo.cn/u/' + keyword_id)
    # 取关该用户， 使用xpath定位路径，找到已关注按钮
    wd.find_element_by_xpath('//div[@class="toolbar_menu_list m-box-col m-box-center m-box-center-a"][1]').click()
    time.sleep(1)

    # 处理弹窗,点击 取消关注
    wd.find_element_by_xpath(
        '//div[@class="m-pop m-pop-s"]//ul/li[2]/div[@class="m-diy-btn m-box-col m-box-center m-box-center-a"]').click()
    time.sleep(1)
    # 处理弹窗,点击  确定
    wd.find_element_by_xpath('//a[@class="m-btn m-btn-white m-btn-text-orange"]').click()


def post_a_new_weibo(blog_content, blog_link):
    """4. 返回到自己主页撰写微博的地方，填写内容，然后发表微博

    @param blog_content: 想发微博的内容
    @param blog_link: 想在微博中添加的链接
    """
    # 使用HTTP GET请求 跳转到 对应的写微博页面的内容
    wd.get('https://m.weibo.cn/compose')
    blog = '[测试]' + blog_content + blog_link
    time.sleep(2)
    # 找到 输入的位置点击一下
    wd.find_element_by_css_selector('span[class="m-wz-def"]').click()
    # 找到 文本区，填入内容
    wd.find_element_by_css_selector('textarea').send_keys(blog)
    time.sleep(1)
    # 找到发送的按钮的类名属性， 选择后，点击
    wd.find_element_by_class_name('m-send-btn').click()


if __name__ == "__main__":
    login_weibo('*****', '*****')
    follow_comment_a_user('6060307497', 3, '有意思～')
    unfollow_a_user('6060307497')
    post_a_new_weibo('这是一个来自自动化测试所给出的测试内容', 'www.baidu.com')
    # 完成所有操作后返回到微博主页
    wd.get('https://m.weibo.cn')
