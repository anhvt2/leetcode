# Write your MySQL query statement below

SELECT e.employee_id, e.department_id
FROM Employee e
JOIN (
-- Count how many dept associated with each employee
    SELECT employee_id, COUNT(*) AS dept_count
    FROM Employee
    GROUP BY employee_id
) as c
ON e.employee_id = c.employee_id
WHERE 
    (c.dept_count = 1) OR
    (c.dept_count > 1 and e.primary_flag = 'Y')

-- SELECT employee_id, department_id
-- FROM Employee
-- WHERE (employee_id, primary_flag) IN (
--     SELECT 
--         employee_id,
--         CASE
--             WHEN COUNT(*) = 1 THEN "N"
--             ELSE "Y"
--         END AS required_flag
--     FROM Employee
--     GROUP BY employee_id
-- );
