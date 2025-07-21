# Write your MySQL query statement below
SELECT customer_id
FROM customer
GROUP BY customer_id
HAVING count(DISTINCT product_key) = (
    SELECT count(*) FROM product
);
