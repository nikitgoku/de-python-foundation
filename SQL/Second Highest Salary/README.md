# Question Title:
176. Second Highest Salary

# Platform & Link:
[LeetCode URL](https://leetcode.com/problems/second-highest-salary/description/)

# Difficulty Level:
Intermediate/Medium

# Type:
Subqueries + Window Functions

# Pattern:
Top-K Filtering

# Core SQL Concepts Used:
DENSE_RANK()

SubQuery

# Expected Output Logic (Plain English):
Return the second-highest distinct salary.

# Final SQL Approach (High-Level):
## Approach 1: Using DENSE_RANK() and Subquery
Step 1: Rank the salaries in DESC order using the DENSE_RANK() function

Step 2: Use the above as subquery to get DISTINCT salary with rank=2

Step 3: Use the above to use SELECT again. This is done becuase if there are no salaries with rank=2,
        Leetcode expect us to return NULL.

## Approach 2: Using MAX() in a subquery
Step 1: We can use MAX to get the highest salary.

Step 2: We can use the above as filter to get salaries smaller than highest salary

Step 3: This is where it gets smart. We can use MAX() again to get the highest salaries among the salaries smaller than highest one.

# Common Pitfalls / Interviewer Traps:

Using CTE instead of Subquery, this traps us becuase we cannot solve the edge case where there are no 2nd higghest salary

# One-Liner Recall:
Top-K Filtering → Subquery + window function → filter
Max to get highest salary → filter using the highest salary to get salaries lower than highest → Get the highest among them