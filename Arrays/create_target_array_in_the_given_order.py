class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l=len(index)
        target=[]
        for x in range(0,l):
            target.insert(index[x],nums[x])
        return target