# Write your MySQL query statement below
SELECT
    extra AS report_reason,
    count(DISTINCT post_id) AS report_count
FROM actions
WHERE action_date = '2019-07-04' AND action = 'report'
GROUP BY extra
ORDER BY report_reason;
