# Write your MySQL query statement below
SELECT
    id,
    count(*) AS num
FROM (
    SELECT requester_id AS id FROM requestaccepted
    UNION ALL
    SELECT accepter_id AS id FROM requestaccepted
) AS allfriends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
