class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        increase = [0] * n 
        decrease = [0] * n
        days = []

        for i in range(1, n):
            if security[i] <= security[i-1]:
                increase[i] = increase[i-1] + 1

        for i in range(n-2,-1,-1):
            if security[i] <= security[i+1]:
                decrease[i] = decrease[i+1] + 1
        
        for i in range(time, n - time):
            if decrease[i] >= time and increase[i] >= time:
                days.append(i)
            
        return days
