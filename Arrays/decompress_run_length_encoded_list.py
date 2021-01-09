class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lst=[]
        for x in range(0,l,2):
            for y in range(nums[x]):
                lst.append(nums[x+1])
        return lst