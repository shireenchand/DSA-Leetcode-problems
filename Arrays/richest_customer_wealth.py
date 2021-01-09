class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        sum=0
        for account in accounts:
            for x in account:
                sum=sum+x
                if(max<sum):
                    max=sum
            sum=0
        return max