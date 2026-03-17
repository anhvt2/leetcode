# Write your MySQL query statement below
SELECT
    id,
    company,
    salary
FROM
    (
        SELECT
            id,
            company,
            salary,
            row_number() OVER (PARTITION BY company ORDER BY salary) AS rn,
            count(*) OVER (PARTITION BY company) AS cnt
        FROM employee
    ) AS ranked
WHERE rn IN (ceil(cnt / 2.0), floor(cnt / 2.0) + 1)
ORDER BY company, salary;
