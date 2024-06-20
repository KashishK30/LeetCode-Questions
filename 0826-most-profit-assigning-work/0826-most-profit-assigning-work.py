class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into a list of tuples and sort by difficulty
        jobs = sorted(zip(difficulty, profit))
        # Sort workers by their ability
        worker.sort()
        
        max_profit = 0  # To keep track of the max profit we can get for the current difficulty
        total_profit = 0  # To accumulate the total profit
        job_index = 0  # Index to iterate over jobs

        for ability in worker:
            # Update the max_profit for the current worker's ability
            while job_index < len(jobs) and jobs[job_index][0] <= ability:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the best possible profit for this worker
            total_profit += max_profit
        
        return total_profit