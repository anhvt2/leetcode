-- # Write your MySQL query statement below
SELECT
    d.name AS department,
    e.name AS employee,
    e.salary
FROM (
    SELECT
        *,
        DENSE_RANK()
            OVER (PARTITION BY departmentid ORDER BY salary DESC)
            AS rnk
    FROM employee
) AS e
INNER JOIN department AS d
    ON e.departmentid = d.id
WHERE e.rnk <= 3;
