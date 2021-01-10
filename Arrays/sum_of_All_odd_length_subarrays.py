class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l=len(arr)
        sum=0
        lst=[]
        for i in range(0,l):
            for x in range(i+1,l+1,2):
                lst.append(arr[i:x])
        for x in lst:
            for y in x:
                sum=sum+y
        return sum