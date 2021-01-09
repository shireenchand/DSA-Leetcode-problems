class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max=0
        i=0
        for candy in candies:
            if(candy>max):
                max=candy
        for candy in candies:
            candy=candy+extraCandies
            if(candy>=max):
                candies[i]=True
            else:
                candies[i]=False
            i=i+1
        return candies