# Write your MySQL query statement below
WITH bank_summary AS (
    SELECT
        u.user_id,
        u.user_name,
        u.credit
        + COALESCE(SUM(
            CASE WHEN u.user_id = t.paid_by THEN -t.amount END
        ), 0)
        + COALESCE(SUM(
            CASE WHEN u.user_id = t.paid_to THEN +t.amount END
        ), 0) AS final_credit
    FROM users AS u
    LEFT JOIN transactions AS t
        ON u.user_id = t.paid_by OR u.user_id = t.paid_to
    GROUP BY u.user_id, u.user_name, u.credit
    ORDER BY u.user_id
)

SELECT
    user_id,
    user_name,
    final_credit AS credit,
    CASE WHEN final_credit < 0 THEN 'Yes' ELSE 'No' END AS credit_limit_breached
FROM bank_summary
ORDER BY user_id;
