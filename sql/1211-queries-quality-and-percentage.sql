SELECT
    query_name,
    round(avg(rating / position), 2) AS quality,
    round(sum(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 / count(*), 2)
        AS poor_query_percentage
FROM queries
GROUP BY query_name;
