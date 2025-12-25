**Problem Name**: Valid Anagram

**Source**: https://leetcode.com/problems/valid-anagram/

**Difficulty**: Easy

**Pattern**: Frequency Counting

**Problem Type**: Hashing


**Core Idea (2–3 lines)**:
Given two strings, check if the two strings are anagram.
Anagram: two strings with same characters (including frequency) but different words

**Approach**:
Initialise an empty hash map.

1. Traverse string 1

2. For each element, check hash set.

3. If the element exists in the hash map, increment the count by 1

4. Else add the element in the hash set with count initialised to 1

5. Traverse string 2

6. For each element, check hash set.

7. If the element exists in the hash map, decrement the count by 1

9. After the traversal, if the hashmap's values are non-zero, return False

**Time Complexity**: O(n + n)
**Space Complexity**: O(n)

**Edge Cases**:


**Common Mistakes**:
- Forgetting the meaning of Anagram (rookie mistake)
- Using defaultdict, because you thought "Wasn't this the question that used defaultdict()". **Please do not.**
- in the second traversal, thinking if the value does not exist, let's return. Bud, we're anyways checking for non-zero values. Chill

**Trigger Keywords (for interviews)**:
hashing, two loops

**Revision Hint (1 line)**:
Hash Set + two loops, one to add frequency, another one to decrease frequency
last loop to check for dict.values() != 0