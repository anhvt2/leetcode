# Write your MySQL query statement below

-- Step ①: Join transaction records with product categories
WITH tx AS (
    SELECT
        t.*,                -- all transaction fields
        p.category          -- product category added from Products table
    FROM transactions AS t
    INNER JOIN products AS p
        ON t.product_id = p.product_id
),

-- Step ②: Compute per-customer aggregate metrics
sum_stat AS (
    SELECT
        customer_id,
        SUM(amount) AS total_amount,            -- total money spent
        COUNT(*) AS transaction_count,       -- number of transactions
        -- distinct categories bought
        COUNT(DISTINCT category) AS unique_categories,
        AVG(amount) AS avg_transaction_amount   -- average transaction amount
    FROM tx
    GROUP BY customer_id
),

-- Step ③: Rank each customer's categories by frequency and recency
cat_rank AS (
    SELECT
        customer_id,
        category,                               -- assign a unique, consecutive number to each category per customer
        ROW_NUMBER() OVER (
            -- ranking is reset for each customer
            PARTITION BY customer_id
            ORDER BY
                COUNT(*) DESC,                  -- most frequent category first
                MAX(transaction_date) DESC      -- tie-breaker: most recent
        ) AS rk
    FROM tx
    GROUP BY customer_id, category
)

-- Step ④: Final result combining metrics and top category
SELECT
    s.customer_id,
    s.transaction_count,
    s.unique_categories,
    c.category AS top_category,
    ROUND(s.total_amount, 2) AS total_amount,   -- most frequent & recent category
    ROUND(s.avg_transaction_amount, 2) AS avg_transaction_amount,
    ROUND(s.transaction_count * 10 + s.total_amount / 100, 2) AS loyalty_score          -- scoring formula
FROM sum_stat AS s
LEFT JOIN cat_rank AS c
    ON
        c.customer_id = s.customer_id           -- only keep the top-ranked category
        AND c.rk = 1
ORDER BY loyalty_score DESC, s.customer_id ASC;
