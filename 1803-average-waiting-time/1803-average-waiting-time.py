class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avg_wait = 0
        start = customers[0][0]
        
        for arrival, prep in customers:
            if start < arrival:
                start = arrival
            finish = start + prep
            avg_wait += (finish - arrival)
            start = finish

        return float(avg_wait/len(customers))