-- Write your PostgreSQL query statement below
-- Approach 1: Window Function
WITH consecutive_nums AS (
    SELECT
        id,
        num,
        LAG(num) OVER (ORDER BY id) AS prev_num,
        LEAD(num) OVER (ORDER BY id) AS next_num
    FROM Logs
)
SELECT
    DISTINCT num AS ConsecutiveNums
FROM consecutive_nums
WHERE num = prev_num and num = next_num;

-- Approach 2: Self JOIN
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id+1
JOIN Logs l3 ON l1.id = l3.id+2
WHERE l1.num = l2.num and l1.num = l3.num;