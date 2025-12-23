**Problem Name**: Two Sum

**Source**: https://leetcode.com/problems/two-sum/

**Difficulty**: Easy

**Pattern**: Hashing / Lookup

**Problem Type**: Array


**Core Idea (2–3 lines)**:
Check if the current elements different with the target exists in the dictionary.

**Approach**:

1. Traverse array

2. For each element, check target - current in dictionary (hashMap)

3. If found → return indices

4. Else store element

**Time Complexity**: O(n)
**Space Complexity**: O(n)

**Edge Cases**:
- Duplicate Numbers
- Negative Values.

**Common Mistakes**:
- Taking abs difference instead of normal difference when checking for complement in dictionary. Taking abs difference will give wrong pairs or miss valid ones.

**Trigger Keywords (for interviews)**:
pair, target, sum, indices

**Revision Hint (1 line)**:
Complement + Dictionary