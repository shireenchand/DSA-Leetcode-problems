class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        lst=[]
        count=0
        for i in range(0,l):
            for j in range(0,l):
                if(nums[j]<nums[i] and j!=i):
                    count=count+1
            lst.append(count)
            count=0
        return lst