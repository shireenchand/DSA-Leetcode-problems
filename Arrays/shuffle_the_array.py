class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=len(nums)
        for x in range(0,l,2):
            nums.insert(x+1,nums[x+n])
        for x in range(0,n):
            nums.pop()
        return nums