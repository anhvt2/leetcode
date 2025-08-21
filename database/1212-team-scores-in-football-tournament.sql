# Write your MySQL query statement below
WITH m_cte AS (
    SELECT
        m.match_id,
        m.host_team,
        m.guest_team,
        m.host_goals,
        m.guest_goals,
        ht.team_name AS host_team_name,
        gt.team_name AS guest_team_name,
        CASE
            WHEN m.host_goals > m.guest_goals THEN 3
            WHEN m.host_goals = m.guest_goals THEN 1
            WHEN m.host_goals < m.guest_goals THEN 0
        END AS host_team_points,
        CASE
            WHEN m.guest_goals > m.host_goals THEN 3
            WHEN m.guest_goals = m.host_goals THEN 1
            WHEN m.guest_goals < m.host_goals THEN 0
        END AS guest_team_points
    FROM matches AS m
    LEFT JOIN teams AS ht ON m.host_team = ht.team_id
    LEFT JOIN teams AS gt ON m.guest_team = gt.team_id
),

points_cte AS (
    SELECT
        host_team AS team_id,
        host_team_points AS points
    FROM m_cte
    UNION ALL
    SELECT
        guest_team AS team_id,
        guest_team_points AS points
    FROM m_cte
)

SELECT
    t.team_id,
    t.team_name,
    coalesce(sum(points_cte.points), 0) AS num_points
FROM teams AS t
LEFT JOIN points_cte ON t.team_id = points_cte.team_id
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC, t.team_id ASC;
