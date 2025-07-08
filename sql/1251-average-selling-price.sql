# Write your MySQL query statement below

WITH Average AS (
    SELECT p.product_id, p.start_date, p.end_date, p.price, u.purchase_date, u.units
    FROM Prices p
    LEFT JOIN UnitsSold u
    ON p.product_id = u.product_id 
        AND p.start_date <= u.purchase_date 
        AND u.purchase_date <= p.end_date
)

SELECT 
    product_id,
    ROUND(
        IFNULL(SUM(price*units) / NULLIF(sum(units), 0), 0),
        2
    ) AS average_price
FROM Average
GROUP BY product_id;
