-- Write your PostgreSQL query statement below
WITH ranked_salary AS (
SELECT
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS salary_rank
FROM Employee e
JOIN Department d ON e.departmentId = d.id
)
SELECT 
    Department,
    Employee,
    Salary
FROM ranked_salary
WHERE salary_rank = 1