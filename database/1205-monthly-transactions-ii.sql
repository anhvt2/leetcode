# Write your MySQL query statement below
SELECT
    country,
    date_format(date_source, '%Y-%m') AS month,
    sum(approved_count) AS approved_count,
    sum(approved_amount) AS approved_amount,
    sum(chargeback_count) AS chargeback_count,
    sum(chargeback_amount) AS chargeback_amount
FROM (
    -- Approved transaction
    SELECT
        t.trans_date AS date_source,
        t.country,
        1 AS approved_count,
        t.amount AS approved_amount,
        0 AS chargeback_count,
        0 AS chargeback_amount
    FROM transactions AS t
    WHERE t.state = 'approved'

    UNION ALL

    -- Chargebacks
    SELECT
        c.trans_date AS date_source,
        t.country,
        0 AS approved_count,
        0 AS approved_amount,
        1 AS chargeback_count,
        t.amount AS chargeback_amount
    FROM chargebacks AS c
    INNER JOIN transactions AS t ON c.trans_id = t.id
) AS combined
GROUP BY month, country
ORDER BY month, country;
