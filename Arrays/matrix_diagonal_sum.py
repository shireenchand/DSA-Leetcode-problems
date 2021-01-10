class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row=0
        col=0
        d=0
        sum=0
        for x in mat:
            row+=1
        for y in mat[0]:
            col+=1
        for i in range (0,row):
            for j in range (0,col):
                if(i==j or abs(i+j)==row-1):
                    sum+=mat[i][j]
        return sum