# Write your MySQL query statement below
WITH temp AS (
  SELECT
    player_id,
    result = 'Win' AS win_cnt,                      -- 1 if Win, else 0
    SUM(result != 'Win')                            -- assign streak_id by counting non-'Win'
      OVER (PARTITION BY player_id
            ORDER BY match_day) AS streak_id
  FROM matches
)

temp2 AS (
    SELECT
        player_id,
        streak_id,
        sum(win_cnt) AS streak_wins
    FROM temp
    GROUP BY player_id, streak_id
)

SELECT
    player_id,
    max(streak_wins) AS longest_streak
FROM temp2
GROUP BY player_id
ORDER BY player_id
