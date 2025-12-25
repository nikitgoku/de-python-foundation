**Problem Name**: Contains Duplicate

**Source**: https://leetcode.com/problems/contains-duplicate/

**Difficulty**: Easy

**Pattern**: Hashing / Lookup

**Problem Type**: Array


**Core Idea (2–3 lines)**:
Check any value appears twice in an array. If yes, return true

**Approach**:
Initialise an empty hash set.

1. Traverse array

2. For each element, check hash set.

3. If the element exists, return True

4. Else add the element in the hash set

**Time Complexity**: O(n)
**Space Complexity**: O(n)

**Edge Cases**:


**Common Mistakes**:
- Initialising a Hash Map and maintaining a count. Then whichever element has count 2, return True.
- This is an acceptable solution, but we are only asked if the array contains any duplicates. So no need to maintain count
  and increasing code complexity.

**Trigger Keywords (for interviews)**:
hashing, O(1) lookup. Set only stores unique values.

**Revision Hint (1 line)**:
Hash Set + Checking if the value exists in the Hash Set.