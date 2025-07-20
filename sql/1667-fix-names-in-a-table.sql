# Write your MySQL query statement below
SELECT
    user_id,
    concat(
        upper(left(name, 1)),
        lower(substring(name, 2))
    ) AS name
FROM users
ORDER BY user_id;
