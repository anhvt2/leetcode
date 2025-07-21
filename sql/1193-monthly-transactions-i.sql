# Write your MySQL query statement below
SELECT
    country,
    date_format(trans_date, '%Y-%m') AS month,
    count(*) AS trans_count,
    sum(state = 'approved') AS approved_count,
    sum(amount) AS trans_total_amount,
    sum(CASE WHEN state = 'approved' THEN amount ELSE 0 END)
        AS approved_total_amount
FROM Transactions
GROUP BY month, country
ORDER BY month, country;
