# Write your MySQL query statement below
SELECT DISTINCT viewer_id AS id
FROM views
GROUP BY viewer_id, view_date        -- group by person and day
HAVING count(DISTINCT article_id) > 1  -- more than one article that day
ORDER BY id;
