# Write your MySQL query statement below
SELECT
    season_id,
    team_id,
    team_name,
    points,
    goal_difference,
    RANK() OVER (
        PARTITION BY season_id                          -- rank within each season
        ORDER BY points DESC, goal_difference DESC, team_name ASC  -- tie-breaking rules
    ) AS position
FROM (
    SELECT
        season_id,
        team_id,
        team_name,
        wins * 3 + draws AS points,
        goals_for - goals_against AS goal_difference    -- new column
    FROM SeasonStats
) t
ORDER BY season_id ASC, position ASC, team_name ASC;