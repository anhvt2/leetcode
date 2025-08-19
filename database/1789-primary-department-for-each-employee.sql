# Write your MySQL query statement below

SELECT e.employee_id, e.department_id
FROM Employee e
JOIN (
    SELECT employee_id, COUNT(*) AS dept_count
    FROM Employee 
    GROUP BY employee_id
) as e2
ON e.employee_id = e2.employee_id
WHERE 
    (e2.dept_count = 1) OR
    (e2.dept_count > 1 and e.primary_flag = 'Y')