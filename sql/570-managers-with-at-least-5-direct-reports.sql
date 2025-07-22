-- # Write your MySQL query statement below
SELECT m.name
FROM employee AS e
INNER JOIN employee AS m
    ON e.managerid = m.id
GROUP BY m.id, m.name
HAVING count(e.managerid) >= 5;
