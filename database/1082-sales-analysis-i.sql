# Write your MySQL query statement below
SELECT seller_id
FROM (
    SELECT
        seller_id,
        sum(price) AS revenue
    FROM sales
    GROUP BY seller_id
) AS t
WHERE
    revenue = (
        SELECT max(revenue)
        FROM (
            SELECT
                seller_id,
                sum(price) AS revenue
            FROM sales
            GROUP BY seller_id
        ) AS x
    )
GROUP BY seller_id
ORDER BY seller_id;
