# Write your MySQL query statement below
SELECT
    p.product_id,
    COALESCE(ROUND(SUM(u.units * p.price) * 1.0 / SUM(u.units), 2),  0) AS average_price
FROM prices AS p
LEFT JOIN unitssold AS u
    ON
        p.product_id = u.product_id
        AND (u.purchase_date BETWEEN p.start_date AND p.end_date)
GROUP BY product_id;
