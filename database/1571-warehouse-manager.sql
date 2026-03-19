# Write your MySQL query statement below
SELECT
    w.name AS warehouse_name,
    sum(p.width * p.length * p.height * w.units) AS volume
FROM warehouse AS w
INNER JOIN products AS p ON w.product_id = p.product_id
GROUP BY w.name
ORDER BY volume DESC;
