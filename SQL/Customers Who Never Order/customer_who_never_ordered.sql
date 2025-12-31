-- Write your PostgreSQL query statement below
SELECT
    name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT
        c.id
    FROM Orders o
    JOIN Customers c ON o.customerId = c.id
)