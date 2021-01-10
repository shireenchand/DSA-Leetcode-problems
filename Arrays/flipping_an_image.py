class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        i=0
        res=[]
        lst=[]
        for x in A:
            x.reverse()
        for x in A:
            for y in x:
                if(y==0):
                    lst.append(1)
                else:
                    lst.append(0)
            res.append(lst)
            lst=[]
        return res

