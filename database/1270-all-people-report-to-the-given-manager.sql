# Write your MySQL query statement below

SELECT employee AS employee_id
FROM (
    SELECT
        e1.employee_id AS employee,
        e1.manager_id AS manager1,
        e2.manager_id AS manager2,
        e3.manager_id AS manager3
    FROM employees AS e1
    LEFT JOIN employees AS e2 ON e1.manager_id = e2.employee_id
    LEFT JOIN employees AS e3 ON e2.manager_id = e3.employee_id
) AS m
WHERE employee <> 1 AND (manager1 = 1 OR manager2 = 1 OR manager3 = 1)
