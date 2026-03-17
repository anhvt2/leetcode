# Write your MySQL query statement below
SELECT
    team_id,
    team_name,
    points,
    rank() OVER (ORDER BY points DESC) AS position
FROM (
    SELECT
        team_id,
        team_name,
        3 * wins + 1 * draws + 0 * losses AS points
    FROM teamstats
) AS ranked
ORDER BY position, team_name;
