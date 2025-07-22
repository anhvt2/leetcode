# Write your MySQL query statement below
SELECT
    'High Salary' AS category,
    count(*) AS accounts_count
FROM accounts
WHERE income > 50000

UNION ALL

SELECT
    'Average Salary',
    count(*)
FROM accounts
WHERE income BETWEEN 20000 AND 50000

UNION ALL

SELECT
    'Low Salary',
    count(*)
FROM accounts
WHERE income < 20000;
