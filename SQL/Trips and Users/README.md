# Question Title:
262. Trips and Users

# Platform & Link:
[LeetCode URL](https://leetcode.com/problems/trips-and-users/description/)

# Difficulty Level:
Hard

# Type:
Aggregation + Conditional Logic

# Pattern:
Conditional Aggregation (CASE WHEN)

# Core SQL Concepts Used:
Multiple Joins using same table
Conditional Logic in Aggregation

# Expected Output Logic (Plain English):
Calculate daily cancellation rates excluding banned users.

# Final SQL Approach (High-Level):
Step 1: Decide the JOIN condition. First join the `users` with `trips` on `client_id`, then join `drivers` on `driver_id`
        For both JOINs also confirm if the roles are client and driver respectively.

Step 2: Filter with three condition, first condition checks if client is not banned, second condition checks if the driver is not banned, and
        the thrid filter if for the dates.

Step 3: Use Conditional Aggregation: We sum those cases where trips were either cancelled by driver or by client. Divide them by total trips that day

Step 4: Round the result to 2 dimensional places

Step 5: GROUP BY

# Common Pitfalls / Interviewer Traps:
1. Confusion with multiple JOIN condition or multi-join

2. If using PostgreSQL, make sure you use `::NUMERIC` with the division (for denominator) so the calculation happen

# One-Liner Recall:
Multi-JOIN -> Filter on 3 condition -> Select with conditional aggregation -> Group BY