"""
给定一个整数数组nums， 大小为n。现在需要找到nums中的三个整数a1, a2, a3， 使得a1+a2+a3=0。请找到nums符合条件的所有三元组。

举例 nums=[-1,0,1,2.-1,-4], 你需要输出的是[[-1,0,1],[-1,-1,2]]

"""
nums=[-1,0,1,2,-1,-4]

def add_three_nums(nums):
    # 对列表数字大小进行排序
    nums.sort()
    # 构建一个空列表
    result = []

    for i in range(len(nums)):
        # 三个整数相加和为0，则至少有一个整数为负数
        if nums[i] > 0:
            break
        # 两个下标 向中间逼近
        j = i + 1
        k = len(nums) - 1
        while j < k:
            sum_three = nums[i] + nums[j] + nums[k]
            if sum_three == 0:
                temp = [nums[i], nums[j], nums[k]]
                if temp not in result:
                    result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif sum_three < 0:
                j += 1
            else:
                k -= 1
    return list(result)

print(add_three_nums(nums))

