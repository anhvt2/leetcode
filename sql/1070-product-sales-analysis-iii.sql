# Write your MySQL query statement below
WITH first_sales AS (
    SELECT
        product_id,
        min(year) AS first_year
    FROM sales
    GROUP BY product_id
)

SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM sales AS s
INNER JOIN first_sales
    ON s.product_id = first_sales.product_id AND s.year = first_sales.first_year;
