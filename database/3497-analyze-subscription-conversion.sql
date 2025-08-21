# Write your MySQL query statement below
# -- users who convert must have both trial (free) and paid rows
WITH
ft AS (
    SELECT
        user_id,
        round(avg(activity_duration), 2) AS trial_avg_duration
    FROM useractivity
    WHERE activity_type = 'free_trial'
    GROUP BY user_id
),

p AS (
    SELECT
        user_id,
        round(avg(activity_duration), 2) AS paid_avg_duration
    FROM useractivity
    WHERE activity_type = 'paid'
    GROUP BY user_id
)

SELECT
    ft.user_id,
    ft.trial_avg_duration,
    p.paid_avg_duration
FROM ft
INNER JOIN p ON ft.user_id = p.user_id
GROUP BY ft.user_id;
