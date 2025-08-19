# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT
        person_name,
        turn,
        sum(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM queue
) AS cumulative
WHERE cumulative_weight <= 1000
ORDER BY turn DESC
LIMIT 1;
