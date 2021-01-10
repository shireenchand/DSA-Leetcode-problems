class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        r=[]
        count=0
        res=0
        for num in nums:
            while num!=0:
                r.append(num%10)
                num=int(num/10)
                for n in r:
                    count+=1
                r=[]
            if(count%2==0):
                    res+=1
            count=0
        return res