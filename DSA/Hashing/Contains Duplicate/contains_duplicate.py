from typing import List
from loguru import logger

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialise a Hash Set
        num_set = set()
        # Traverse the list, and check if the element exists in the set.
        # If yes, straightaway return True
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False
    
solution_object = Solution()
logger.info(f"Result Case 1: {solution_object.containsDuplicate([1, 2, 3, 1])}")            # Expected: True
logger.info(f"Result Case 2: {solution_object.containsDuplicate([1, 2, 3, 4])}")            # Expected: False
logger.info(f"Result Case 3: {solution_object.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")   # Expected: True