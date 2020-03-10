### Python开发常见问题集锦

### 基本操作
    
    1. 合并2个列表: 列表中要添加另外一个列表的内容很简单，用加号就可以了.               
                a += [4,5,6]
    2. 合并2个字典: 字典x 中要添加 另外一个字典y的内容，可以使用字典的update方法。(如果有重复的key， 会被字典y中的内容取代)       
                x.update(y)
    3. 列表中去掉 重复的元素:
        * 循环遍历法:定义一个新列表，依次循环旧列表，如果没在新列表中，就插入，如果在，则不插入.
                for item in list1:
                    if item not in list2:
                        list2.append(item)
        * set方法:set集合的元素是唯一的、不重复的，所以可以直接使用set转换list列表去重。要注意的是，这种方法，原列表的元素顺序可能会发生改变.
                list2 = list(set(list1))
    4. 从列表中过滤元素:
        * 列表推导式: 将该列表中所有的正数提取出来放到一个新的列表中.
                positives = [num for num in numbers if num > 0]
        * 如果过滤的处理比较复杂，可以自己定义一个 函数用来判断 参数 是否符合过滤条件。
    5. 从字典中过滤元素:从一个字典中，根据某些条件过滤掉一些元素，生成一个新的字典.使用字典生成式.
    
    6. 产生随机数:想产生某个范围内的随机数字，可以使用random库里面的randint方法。比如，要在0,9之间产生一个随机数：
                from random import randint 
                print randint(0,9)
    7. 产生随机字符串: 
        * 要产生一个随机的字符串，里面可以有大写字母和数字:
                import string,random 
                ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        * 如果随机字符串里面，可以有小写字母和数字:
                ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    8. 列表排序sort和sorted:
        * sort：该方法对列表进行永久性排序
        * sorted：对列表进行临时性排序
    9. 判断等价的两种表达的比较：
        * is:   是比较两个对象的地址，及id()的返回值
        * ==:   是判读两个对象的内容是否相等，
        * 通过切片赋值，虽然内容相同，但因其地址不一样，所以返回的结果也不一样。
    10. for循环得到索引:
                alist = ['a','b','c','d']
                for idx, val in enumerate(alist):
                    print(idx, val)



