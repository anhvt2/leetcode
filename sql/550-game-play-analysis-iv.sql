# Write your MySQL query statement below
WITH f AS (
    SELECT
        player_id,
        min(event_date) AS first_login
    FROM activity
    GROUP BY player_id
)

SELECT
    round(
        count(DISTINCT a.player_id)
        / (SELECT count(DISTINCT player_id) FROM activity
        ),
        2
    ) AS fraction
FROM activity AS a
INNER JOIN f
    ON
        a.player_id = f.player_id
        AND a.event_date = date_add(f.first_login, INTERVAL 1 DAY);
