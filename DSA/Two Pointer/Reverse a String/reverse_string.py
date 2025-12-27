from typing import List
from loguru import logger

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """Using Two pointer method"""
        # Initialise the two pointer at start of the list and end of the list
        left = 0
        right = len(s) - 1
        # Use a while loop until left and right and not equal
        while right > left:
            # Swap the two elements, one at the
            s[left], s[right] = s[right], s[left]
            # Move the two pointers forward and reverse respectively
            left += 1
            right -= 1
        
        return s
        """Using List Slicing"""
        # return s[::-1]
    
solution_object = Solution()
inputs = [['h', 'e', 'l', 'l', 'o'], 
         ['n', 'i', 'k', 'i', 't', 'G', 'o', 'k', 'h', 'a', 'l', 'e'],
         ['s', 't', 'a', 't', 'i', 'n', 'g', 'A', 'g', 'a', 'i', 'n']]
case_count = 1
for input in inputs:
    logger.info(f"Result Case {case_count}: {solution_object.reverseString(input)}")
    case_count += 1