# Write your MySQL query statement below
SELECT player_id, device_id
FROM Activity 
WHERE (player_id, event_date) IN (
    SELECT player_id, MIN(event_date)
    FROM Activity
    GROUP BY player_id);


-- -----------------------------------------------
-- WITH cte AS (
--     SELECT player_id, MIN(event_date) AS "min_date"
--     FROM Activity
--     GROUP BY player_id
-- )

-- SELECT t.player_id, t.device_id
-- FROM Activity t
-- JOIN cte c
-- ON t.player_id = c.player_id AND t.event_date = c.min_date
