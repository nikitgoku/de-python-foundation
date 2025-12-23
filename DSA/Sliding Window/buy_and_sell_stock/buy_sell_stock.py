from typing import List
from loguru import logger

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialise min value to be the first price from the prices list
        min_value = prices[0]
        # Initialise max_profit to  0
        max_profit = 0
        # Iterate from the 2nd element till the last
        for i in range(1, len(prices)):
            # If the current value is smaller than the min value
            # replace the min with current value and skip the current iteration
            if prices[i] < min_value:
                min_value = prices[i]
                continue
            # If not, calculate the profit and max_profit
            profit = prices[i] - min_value
            max_profit = max(max_profit, profit)

        return max_profit
    
solution = Solution()
logger.info(f"Result Case 1: {solution.maxProfit([7,1,5,3,6,4])}")  # Expected: 5
logger.info(f"Result Case 2: {solution.maxProfit([7,6,5,3,1])}")    # Expected: 0
logger.info(f"Result Case 3: {solution.maxProfit([7,2,5,6,1,9])}")  # Expected: 8