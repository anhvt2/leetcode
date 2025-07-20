# Write your MySQL query statement below
SELECT
    sell_date,
    COUNT(*) AS num_sold,
    GROUP_CONCAT(
        product
        ORDER BY product
        separator ',')
        AS products
FROM (
    SELECT DISTINCT
        sell_date,
        product
    FROM activities
) AS unique_sales
GROUP BY sell_date;
