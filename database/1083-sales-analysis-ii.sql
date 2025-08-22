# Write your MySQL query statement below
SELECT s.buyer_id
FROM sales AS s
LEFT JOIN product AS p ON s.product_id = p.product_id
GROUP BY s.buyer_id
HAVING
    sum(p.product_name = 'S8') > 0
    AND sum(p.product_name = 'iPhone') = 0;
