# Question Title:
180. Consecutive Numbers

# Platform & Link:
[LeetCode URL](https://leetcode.com/problems/consecutive-numbers/description/)

# Difficulty Level:
Intermediate/Medium

# Type:
Self-Join / Window Functions

# Pattern:
Gaps and Islands

# Core SQL Concepts Used:
LEAD() LAG()

SELF JOIN

# Expected Output Logic (Plain English):
Identify numbers appearing at least three times consecutively.

# Final SQL Approach (High-Level):
## Approach 1: Window Functions
Step 1: In a CTE, use a Window Function get the previous num and next num on the same row. Remember to order by id.

Step 2: Use that CTE to select the num column

Step 3: Filter to get the instances where num = next_num and num = prev_num

## Approach 2: Self-Join
Step 1: Join Logs to itself three times: previous, current, next.

Step 2: Force id to be the consecutive (id, id+1, id+2) and num to match all the three (Use filter)

# Common Pitfalls / Interviewer Traps:

When using LEAD() or LAG(), make sure that you ORDER BY id and not PARTITION BY num, as partitioning by num will
- Causes all the same nums to be grouped together even if there is a gap in them (another number in between)
- This crashes the order and returns a wrong number

Forgetting to filter

With Self-join, remember to JOIN on id = id+1 and id = id+2

# One-Liner Recall:
LEAD() LAG() to get prev and next num; order by id
SELF JOIN on on id = id+1 and id = id+2. Force id to be consecutive. Filter where num is same for both l2 and l3.