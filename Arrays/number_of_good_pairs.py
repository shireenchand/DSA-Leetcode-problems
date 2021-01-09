class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good=0
        l = len(nums)
        for i in range(0,l):
            for j in range(i,l):
                if(nums[i]==nums[j] and i<j):
                    good=good+1
        return good