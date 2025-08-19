# Write your MySQL query statement below
SELECT max(num) AS num
FROM (
    SELECT num
    FROM mynumbers
    GROUP BY num
    HAVING count(num) = 1
) AS singles;
