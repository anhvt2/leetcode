# Write your MySQL query statement below
WITH first_login_cte AS (
    SELECT
        user_id,
        min(activity_date) AS login_date
    FROM traffic
    WHERE activity = 'login'
    GROUP BY user_id
)

SELECT
    login_date,
    count(*) AS user_count
FROM first_login_cte
WHERE datediff('2019-06-30', login_date) <= 90 AND login_date <= '2019-06-30'
GROUP BY login_date
ORDER BY login_date;
