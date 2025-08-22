-- Write your MySQL query statement below
WITH ar AS (
    SELECT
        a.user_id,
        a.post_id,
        a.action_date,
        a.action,
        a.extra,
        r.remove_date
    FROM actions AS a
    LEFT JOIN removals AS r ON a.post_id = r.post_id
)

SELECT ROUND(AVG(daily_percent), 2) AS average_daily_percent
FROM (
    SELECT
        ar.action_date,
        100.0
        * COUNT(
            DISTINCT CASE WHEN ar.remove_date IS NOT NULL THEN ar.post_id END
        )
        / COUNT(DISTINCT ar.post_id) AS daily_percent
    FROM ar
    WHERE
        ar.action = 'report'
        AND ar.extra = 'spam'
    GROUP BY ar.action_date
) AS daily_ar;
