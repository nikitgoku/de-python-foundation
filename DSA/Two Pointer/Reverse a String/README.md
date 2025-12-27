**Problem Name**: Reverse a String

**Source**: https://leetcode.com/problems/reverse-string/

**Difficulty**: Easy

**Pattern**: Two Pointers / List Slicing

**Problem Type**: List/String


**Core Idea (2–3 lines)**:
Given a string, reverse the string in-place without using in-built functions.

**Approach1**:
1. Using list slicing reverse the string s[start:end:steps]

2. Python utilises list slicing to reverse the string by marking the steps section as -1

**Approach2**:
Using two pointer approach
1. Initialise two pointers, one at the far left and one at the far right

2. Using a while loop, swap the left and right elements with each other

3. After every iteration, move the left one place forward and right two place forward.

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Edge Cases**:


**Common Mistakes**:
- on the leetcode platform the list slicing method does not work, as we have to return the sliced list and the function is built to handle in-place edits

**Trigger Keywords (for interviews)**:
two-pointer, swap, list slicing by revesing

**Revision Hint (1 line)**:
two pointer left right, swap
reverse using slicing [-1::-1] or [::-1]