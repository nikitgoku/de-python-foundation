# Question Title:
183. Customers Who Never Order

# Platform & Link:
[LeetCode URL](https://leetcode.com/problems/customers-who-never-order/description/)

# Difficulty Level:
Easy

# Type:
Subquery (Column)
LEFT JOIN

# Pattern:
Column Subquery

# Core SQL Concepts Used:
Filtering with SubQuery

# Expected Output Logic (Plain English):
Identify customers with zero orders.

# Final SQL Approach (High-Level):
Step 1: LEFT join the customers table on orders table. This will act as a column subquery, which can used with WHERE clause

Step 2: The table returns a single column with customer_id. Apply a filter where id from outer query does not exist in subquery
        NOT IN

Step 3: Get only the name of customer

# Common Pitfalls / Interviewer Traps:

Edge Case: Where name of two or more customers are same
Customers:
id | name
1  | James
2  | James

For this case you cannot filter with **WHERE name NOT IN ...**
So use **id** which works even if we are not selecting the column.

# One-Liner Recall:
Filter with WHERE clause using COLUMN Subquery which returns a single column, which can be used to check the membership
Use id column to filter.