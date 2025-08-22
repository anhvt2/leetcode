# Write your MySQL query statement below
# First solution
SELECT DISTINCT s.buyer_id
FROM Sales s
WHERE EXISTS (
  SELECT seller_id
  FROM Sales s2
  JOIN Product p2 ON p2.product_id = s2.product_id
  WHERE s2.buyer_id = s.buyer_id AND p2.product_name = 'S8'
)
AND NOT EXISTS (
  SELECT seller_id
  FROM Sales s3
  JOIN Product p3 ON p3.product_id = s3.product_id
  WHERE s3.buyer_id = s.buyer_id AND p3.product_name = 'iPhone'
);

# Second solution
-- SELECT s.buyer_id
-- FROM sales AS s
-- LEFT JOIN product AS p ON s.product_id = p.product_id
-- GROUP BY s.buyer_id
-- HAVING
--     sum(p.product_name = 'S8') > 0
--     AND sum(p.product_name = 'iPhone') = 0;
