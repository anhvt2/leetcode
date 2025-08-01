# Write your MySQL query statement below
SELECT 
    m.employee_id,
    m.name,
    COUNT(*) AS "reports_count",
    ROUND(AVG(e.age)) AS "average_age"
FROM Employees AS m
JOIN Employees AS e
ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;