'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
首先排序，在取前几个
'''
def GetLeastNumbers_Solution(self, tinput, k):
        if k<=len(tinput):
            newdata = sorted(tinput)
            return newdata[:k]
        else:
            return []
