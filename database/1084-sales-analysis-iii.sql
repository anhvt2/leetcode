# Write your MySQL query statement below
# First solution
SELECT
    s.product_id,
    p.product_name
FROM sales AS s
LEFT JOIN product AS p ON s.product_id = p.product_id
GROUP BY product_id
HAVING
    min(s.sale_date) >= '2019-01-01'
    AND max(s.sale_date) <= '2019-03-31';

-- # Second solution
-- SELECT DISTINCT
--     s.product_id,
--     p.product_name
-- FROM Sales s
-- JOIN Product p 
--     ON s.product_id = p.product_id
-- WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
--   AND NOT EXISTS (
--       SELECT NULL           # SELECT 1, NULL, or * all works
--       FROM Sales s2
--       WHERE s2.product_id = s.product_id
--         AND (s2.sale_date < '2019-01-01' OR s2.sale_date > '2019-03-31')
--   );
