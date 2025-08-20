WITH RECURSIVE visitsPerTrans AS (
    SELECT 
        num_transactions AS transactions_count, 
        COUNT(user_id) AS visits_count
    FROM (
        SELECT 
            v.user_id, 
            v.visit_date,
            SUM(CASE WHEN t.transaction_date IS NULL THEN 0 ELSE 1 END) AS num_transactions
        FROM visits v
        LEFT JOIN Transactions t 
            ON t.transaction_date = v.visit_date 
           AND t.user_id = v.user_id
        GROUP BY v.user_id, v.visit_date
    ) cnt
    GROUP BY num_transactions
),
series AS (
    SELECT 0 AS n
    UNION ALL
    SELECT n+1 
    FROM series 
    WHERE n < (SELECT MAX(transactions_count) FROM visitsPerTrans)
)
SELECT 
    ts.n AS transactions_count,  
    CASE 
        WHEN vpt.transactions_count IS NULL THEN 0 
        ELSE visits_count 
    END AS visits_count
FROM series ts 
LEFT JOIN visitsPerTrans vpt 
    ON ts.n = vpt.transactions_count
ORDER BY ts.n;
