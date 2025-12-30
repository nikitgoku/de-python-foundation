from typing import List
from loguru import logger

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """Using two pointer technique"""
        """
        Merges nums2 into nums1 in-place so that nums1 becomes a single
        sorted array in non-decreasing order.

        nums1 has length m + n; first m elements are valid, last n are 0 placeholders.
        nums2 has length n.
        """
        i = m - 1   # Pointer at the last valid element at nums1
        j = n - 1   # Pointer at the last element at nums2
        k = m + n - 1   # Pointer at the last element at nums1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # While nums2 is non-empty
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

solution_object = Solution()    
logger.info(f"Result Case 1: {solution_object.merge([1, 2, 3, 0, 0, 0], 3, [2, 4, 5], 3)}") # Expected: [1, 2, 2, 3, 4, 5]
logger.info(f"Result Case 2: {solution_object.merge([1, 4, 7, 0, 0, 0], 3, [2, 5, 6], 3)}") # Expected: [1, 2, 4, 5, 6, 7]
logger.info(f"Result Case 3: {solution_object.merge([1], 1, [], 0)}")   # Expected: [1]
logger.info(f"Result Case 3: {solution_object.merge([0], 0, [4], 1)}")  # Expected: [4]