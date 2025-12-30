**Problem Name**: Merge Two Sorted Array

**Source**: https://leetcode.com/problems/merge-sorted-array/

**Difficulty**: Easy

**Pattern**: Two Pointers

**Problem Type**: List


**Core Idea (2–3 lines)**:
Merges nums2 into nums1 in-place so that nums1 becomes a single sorted array in non-decreasing order.

**Approach1**:
1. Using two pointer approach and merging from the back (fill from the largest to the smallest)

**Approach2**:
Using two pointer approach
1. Initialise the tree pointers, i = m - 1, j = n - 1 and k = m + n - 1

2. Now using a while loop and until i and j are greater than or equal to 0, check if

3. nums1[i] > nums2[j], if yes, replace nums1[k] with nums1[i]; move k and i one place to the left

4. Else, replace nums1[k] with nums2[j]; move k and j one place to the lest

5. Handling edge case; if nums2 is still not completely traversed, then merge the remaining elements from nums2 to nums1
    This can be done using a while loop where j >= 0

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Edge Cases**:
1. When nums1 has only zeroes: This is the case where nums2 is still not completely traversed

2. When nums2 is empty, this is already handled using the first while loop. Because we won't have to merge anything from nums2


**Common Mistakes**:
Swap from front idea. It destroyes the sorted nature of the nums2

**Trigger Keywords (for interviews)**:
two-pointer, reverse swap

**Revision Hint (1 line)**:
two pointer one at the valid end of nums1, other at the valid end at nums2
Another pointer at the end of nums1, where the largest element is placed