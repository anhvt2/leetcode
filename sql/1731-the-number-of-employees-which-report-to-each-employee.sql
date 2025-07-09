# Write your MySQL query statement below
WITH Management AS (
    SELECT 
        m.employee_id, 
        m.name, 
        e.age as "employee_age"
    FROM Employees m
    JOIN Employees e
    ON m.employee_id = e.reports_to
)

SELECT 
    employee_id,
    name,
    COUNT(*) AS "reports_count",
    ROUND(AVG(employee_age)) AS "average_age"
FROM Management
GROUP BY employee_id, name
ORDER BY employee_id;
