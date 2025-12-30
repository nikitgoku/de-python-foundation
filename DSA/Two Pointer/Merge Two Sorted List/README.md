**Problem Name**: Merge Two Sorted List

**Source**: https://leetcode.com/problems/merge-two-sorted-lists/description/

**Difficulty**: Easy

**Pattern**: Two Pointers

**Problem Type**: Linked List


**Core Idea (2–3 lines)**:
Merges list1 into list2 so that it returns a single sorted list.

**Approach**:
1. Using two pointer approach and merging from the back (fill from the largest to the smallest)

**Time Complexity**: O(m + n) where m, n are lengths of input lists
**Space Complexity**: O(1) - only dummy node + pointers

**Edge Cases**:
1. Initialise a dummy head and a pointer to the dummy head from where the list will start

2. Use a while loop until one of the list reaches the end

3. Compare the value of list1 and list2 and take the smaller one and merge it into the final one, represented by current pointer
    Move the current node and the node takes from the list one place forward.

4. Before the above, check if any of the list is empty, if yes, return the non empty list as complete and break the loop

5. Return the dummy.next


**Common Mistakes**:
Trying to merge the lists into a single list1. Please be aware to use a dummy head to start building from that.

**Trigger Keywords (for interviews)**:
two-pointer

**Revision Hint (1 line)**:
two pointer one at the list1 and one at list 2
take the smaller and merge into the final list
If list1 or list2 remains, merge the entire list into the final one