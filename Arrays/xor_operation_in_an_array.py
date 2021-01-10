class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        xor=0
        for x in range(0,n):
            nums.append(start+2*x)
        for x in nums:
            xor=xor^x
        return xor