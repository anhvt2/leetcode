-- SELECT
--     query_name,
--     ROUND(AVG(rating/position), 2) AS quality,
--     ROUND(AVG(
--         CASE WHEN rating < 3 
--         THEN 1 ELSE 0 
--         END) * 100.0, 2) AS poor_query_percentage
-- FROM Queries
-- GROUP BY query_name;

SELECT 
    q.query_name, 
    round(avg(rating/position), 2) AS quality, 
    ifnull(poor.poor_query_percentage, 0) AS poor_query_percentage
FROM Queries q
LEFT JOIN (
    SELECT poor.query_name, round(count(*) / total.count * 100, 2) AS poor_query_percentage
    FROM Queries poor 
    JOIN (
        SELECT query_name, count(*) AS count FROM Queries GROUP BY query_name
    ) total
    ON poor.query_name = total.query_name AND poor.rating < 3
    GROUP BY poor.query_name
) poor
ON poor.query_name = q.query_name
GROUP BY query_name