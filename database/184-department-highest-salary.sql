# Write your MySQL query statement below
SELECT
    d.name AS department,
    e.name AS employee,
    e.salary
FROM employee AS e
LEFT JOIN department AS d
    ON e.departmentid = d.id
WHERE (e.departmentid, e.salary) IN (
    SELECT
        departmentid,
        max(salary)
    FROM employee
    GROUP BY departmentid
);
