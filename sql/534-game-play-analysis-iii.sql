# Write your MySQL query statement below
SELECT
    player_id,
    event_date,
    sum(games_played) OVER (
        PARTITION BY player_id
        ORDER BY event_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS games_played_so_far
FROM activity;
