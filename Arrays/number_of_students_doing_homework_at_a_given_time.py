class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        l=0
        busy=0
        for x in startTime:
            l+=1
        for x in range(0,l):
            if(queryTime>=startTime[x] and queryTime<=endTime[x]):
                busy+=1
        return busy