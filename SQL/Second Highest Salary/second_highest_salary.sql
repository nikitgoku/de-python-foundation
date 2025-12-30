-- Write your PostgreSQL query statement below
-- Approach 1: Using DENSE_RANK() function
SELECT (
    SELECT
        DISTINCT salary
    FROM (
        SELECT
            id,
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
        FROM Employee
    ) AS ranked_salary
    WHERE salary_rank = 2
) AS SecondHighestSalary

-- Approach 2: Using MAX()
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);