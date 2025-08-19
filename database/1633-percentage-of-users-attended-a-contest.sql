# Write your MySQL query statement below
SELECT
    r.contest_id,
    round(
        count(DISTINCT r.user_id) * 100 / (SELECT count(user_id) FROM users), 2
    ) AS percentage
FROM register AS r
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC
