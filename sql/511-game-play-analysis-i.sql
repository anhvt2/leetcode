# Write your MySQL query statement below

SELECT DISTINCT
    player_id,
    min(event_date) OVER (PARTITION BY player_id) AS first_login
FROM Activity;

SELECT DISTINCT
    player_id,
    min(event_date) AS first_login
FROM Activity
GROUP BY player_id;


-- WITH cte AS (
--     SELECT player_id, MIN(event_date) AS "min_date"
--     FROM Activity
--     GROUP BY player_id
-- )

-- SELECT t.player_id, t.event_date AS "first_login"
-- FROM Activity t
-- JOIN cte c
-- ON t.player_id = c.player_id AND t.event_date = c.min_date

