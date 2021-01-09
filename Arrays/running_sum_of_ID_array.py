class Solution(object):
    def runningSum(self, nums):
        l = len(nums)
        lst=[]
        sum=0
        for x in range (0,l):
            sum = sum + nums[x]
            lst.append(sum)
        return lst