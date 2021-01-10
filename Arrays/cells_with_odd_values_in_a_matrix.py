class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        lst=[]
        arr=[]
        odd=0
        for i in range(0,n):
            for j in range(0,m):
                lst.append(0)
            arr.append(lst)
            lst=[]
        for indice in indices:
            for j in range(0,m):
                    arr[indice[0]][j]+=1
            for i in range(0,n):
                    arr[i][indice[1]]+=1
        for i in range(0,n):
            for j in range(0,m):
                if(arr[i][j]%2!=0):
                    odd+=1
        return odd