# Question Title:
184. Department Highest Salary

# Platform & Link:
[LeetCode URL](https://leetcode.com/problems/department-highest-salary/description/)

# Difficulty Level:
Intermediate/Medium

# Type:
Joins + Window Functions

# Pattern:
Top-N per Group

# Core SQL Concepts Used:
RANK()

CTE

# Expected Output Logic (Plain English):
Return employees who earn the highest salary in each department.

# Final SQL Approach (High-Level):

Step 1: In a CTE, use a Window Function to rank salary separated by department and ordered by salary per deparment in desc order

Step 2: Use that CTE to select the relavant columns

Step 3: Filter to get the instances with rank as 1.

# Common Pitfalls / Interviewer Traps:

Incorrect join type

Missing partition in window function

# One-Liner Recall:
Top-N per group → CTE + window function + partition → filter