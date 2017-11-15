'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if(index<=0):
            return 0
        uglyList = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for i in range(index-1):
            new = min(uglyList[index2]*2,uglyList[index3]*3,uglyList[index5]*5)
            uglyList.append(new)
            if(new%2 == 0):
                index2 += 1
            if (new%3 == 0):
                index3 += 1
            if (new%5 == 0):
                index5 += 1
        return uglyList[-1]
