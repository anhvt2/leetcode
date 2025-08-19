WITH base_table AS (
    SELECT
        *,
        rank()
            OVER (PARTITION BY product_id ORDER BY change_date DESC)
            AS ranking
    FROM products
    WHERE change_date <= '2019-08-16'
),

b AS (SELECT * FROM base_table
WHERE ranking = 1)

SELECT
    a.product_id,
    COALESCE(new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM products) AS a
LEFT JOIN
    b
    ON a.product_id = b.product_id
