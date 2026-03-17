SELECT
    team_name,
    points,
    position,
    CASE
        WHEN position <= CEIL(total_teams / 3.0) THEN 'Tier 1'
        WHEN position <= CEIL(2 * total_teams / 3.0) THEN 'Tier 2'
        ELSE 'Tier 3'
    END AS tier
FROM (
    SELECT
        team_name,
        wins * 3 + draws AS points,
        RANK() OVER (ORDER BY wins * 3 + draws DESC) AS position,
        COUNT(*) OVER () AS total_teams
    FROM teamstats
) AS t
ORDER BY points DESC, team_name ASC;
