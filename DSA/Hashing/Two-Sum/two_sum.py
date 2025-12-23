from typing import List
from loguru import logger

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialise a dictionary to store "element:index"
        num_dictionary = {}
        # loop through the list
        for i in range(len(nums)):
            # Check if the different is in the dictionary
            diff = target - nums[i]
            if diff in num_dictionary:
                return [i, num_dictionary[diff]]    # Returns the current index and stored index
            # If not, update the dictionary with the current element as key and current index as value
            num_dictionary[nums[i]] = i

        # Assumption is that we'll find exactly one solution
        return -1
    
solution_object = Solution()
logger.info(f"Result Case 1: {solution_object.twoSum([2, 7, 11, 15], 9)}")  # Expected: [0, 1]  (Order does not matter)
logger.info(f"Result Case 2: {solution_object.twoSum([3, 2, 4], 6)}")       # Expected: [2, 3]  (Order does not matter)
logger.info(f"Result Case 3: {solution_object.twoSum([3, 3], 6)}")          # Expected: [0, 1]  (Order does not matter)
logger.info(f"Result Case 4: {solution_object.twoSum([-3, 4, 3, 90], 0)}")  # Expected: [2, 0]  (Order does not matter)