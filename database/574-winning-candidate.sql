# Write your MySQL query statement below
SELECT c.name
FROM candidate AS c
INNER JOIN vote AS v
    ON c.id = v.candidateid
GROUP BY c.id, c.name
ORDER BY count(*) DESC
LIMIT 1;
