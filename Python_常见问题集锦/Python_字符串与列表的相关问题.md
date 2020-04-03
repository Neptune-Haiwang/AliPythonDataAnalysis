### 字符串操作

    1。unicode数字转换为字符：把 unicode数字转换为字符， 使用chr()
                chr(50) # '2'       chr(0x4e2d)  # 0x开头表示数字是16进制 # '中'
    2。字符转换为unicode数字：反过来，要把 字符转换为对应的unicode数字，使用 ord() 该函数参数字符串里面只能有一个字符
                ord('2') # 50       ord('中') # 20013
    3。字符串编码为 unicode转义数字：
                '白月黑羽'.encode('unicode-escape') # b'\\u767d\\u6708\\u9ed1\\u7fbd'
    4。字符串常用方法：
        * split（）：我们可以指定任何的分隔符来分割字符串 
        * strip（）：方法可以将 字符串前面和后面的空格删除，但是不会删除字符串中间的空格
        * lstrip（）：方法 将 字符串前面 (左边) 的空格删除，但是不会删除字符串中间和右边的空格
        * rstrip（）：方法 将 字符串后面 (右边) 的空格删除，但是不会删除字符串中间和左边的空格
        * replace（）：用来 替换 字符串里面 所有指定的 子字符串 为另一个 字符串
                str1 = str1.replace('我们', '他们')  
        * startswith（） 和 endswith（）：检查字符串是否以参数指定的字符串 开头/结尾，如果是，返回True，否则返回False
        * isdigit（）：检查字符串是否全部由数字构成，如果是，返回True，否则返回False
                str1.isdigit()        
    5。使用正则表达式切割字符串：当你需要更加灵活的切割字符串的时候
                import re
                names = '关羽; 张飞, 赵云,   马超, 黄忠  李逵'  
                #正则表达式 [;,\s]\s* 指定了，分割符为 分号、逗号、空格 里面的任意一种均可，并且 该符号周围可以有不定数量的空格。
                namelist = re.split(r'[;,\s]\s*', names) 
                print(namelist)
                
    6。使用split函数从字符串中提取内容：比如：从下面格式的字符串中提取出 UID号
                添加用户 byhy(UID 5533)成功   
                uid = content.split('(UID ')[1].split(')')[0]
                print(f'uid is :{uid}')
    7。使用正则表达式从字符串中提取内容：使用正则表达，可以从多种可能格式的字符串中，提取我们想要的内容 
        比如，我们想要从下面这几种可能格式的字符串中提取 用户对应的UID号
                # 其中 \(UID\W*(\d*)\) 是正则表达式， 
                # content 是被搜索的字符串 findall 方法会获取所有匹配该正则表达式的 子字符串，所以返回的是一个列表
                uid =  re.findall(r'\(UID\W*(\d*)\)', content)[0]
    8。字符串替换时忽略大小写：
                text = 'UPPER PYTHON, lower python, Mixed Python'
                print(re.sub('python', 'snake', text, flags=re.IGNORECASE))
    9。json格式字符串处理：
        * 我们如果需要将一个json格式的字符串转换为 Python中的对象进行处理：
                jsonStr = '''{
                    "account1": 13, 
                    "account2": 12, 
                    "account3": 15}
                '''
                import json
                membersObj = json.loads(jsonStr)
        * 反之，可以这样将一个Python中的对象转换为 一个 json格式的字符串：
                members = {
                    'account1'  : 13 ,
                    'account2'  : 12 ,
                    'account3'  : 15 ,
                }
                import json
                jsonStr = json.dumps(members)
    10。要得到一个字符串的 倒序字符串，只需要使用切片操作 [::-1]
        :: 表示切片字符串的从头到尾，也就是全部内容， 而 步长 为 -1 表示，颠倒过来取元素
                str1 = '字符串的倒序'
                reverse = str1[::-1]
                print(reverse)


### 列表的相关操作

    1。append（）：append方法就会改变列表的内容，在后面添加一个元素
                a = [1, 2, 3.14, 'hello'] 
                a.append([7,8]])
    2。insert（）：如果我们 不是要在后面 添加一个元素， 而是在 指定位置插入一个元素，就可以使用insert方法
                a.insert(2, '黑羽')   # 插入到索引2的位置，也是插到第3个元素的位置上
    3。pop（）：如果我们要从列表 取出并删除 一个元素，就可以使用pop方法。该方法的参数就是要取出的元素的索引，
        注意，取出后，该元素就从列表中删除了。所以pop也经常用来删除某个元素
                a = [1, 2, 3.14, 'python3.vip']  
                poped = a.pop(3)    # 取出索引为3 的元素，也就是第4个元素
                print(a)    # 取出后，a列表对象内容就变成了 [ 1, 2, 3.14]
                print(poped)    # 而取出的元素赋值给变量poped， poped的内容就是 'python3.vip' 
    4。remove（）：而 remove方法的参数就是要删除元素的 值。remove从第1个元素开始，寻找 和参数对象 相等的元素，如果找到了，就删除。
        找到后，不会继续往后寻找其它相等的元素。也就是说remove 最多只会删除1个元素。
    5。reverse（）：reverse方法将列表元素倒过来
    6。sort(): 排序方法，把列表元素从小到大排列
