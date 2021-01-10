class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l=len(arr)
        triplets=0
        for x in range(0,l):
            for y in range(0,l):
                for z in range(0,l):
                    if(0<=x and x<y and y<z and z<l):
                        if(abs(arr[x]-arr[y])<=a and abs(arr[y]-arr[z])<=b and abs(arr[x]-arr[z])<=c):
                            triplets=triplets+1
        return triplets