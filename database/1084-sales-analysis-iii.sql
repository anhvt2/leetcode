# Write your MySQL query statement below
SELECT
    s.product_id,
    p.product_name
FROM sales AS s
LEFT JOIN product AS p ON s.product_id = p.product_id
GROUP BY product_id
HAVING
    min(s.sale_date) >= '2019-01-01'
    AND max(s.sale_date) <= '2019-03-31';
