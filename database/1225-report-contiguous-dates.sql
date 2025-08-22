# Write your MySQL query statement below
WITH unioned AS (
    SELECT
        fail_date AS d,
        'failed' AS period_state
    FROM failed
    WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31'
    UNION ALL
    SELECT
        success_date AS d,
        'succeeded' AS period_state
    FROM succeeded
    WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31'
),

grp AS (
    SELECT
        period_state,
        d,
        /* same-state islands: date - row_number() is constant for a run */
        DATE_SUB(d, INTERVAL ROW_NUMBER() OVER (
            PARTITION BY period_state ORDER BY d
        ) DAY) AS island_key
    FROM unioned
)

SELECT
    period_state,
    MIN(d) AS start_date,
    MAX(d) AS end_date
FROM grp
GROUP BY period_state, island_key
ORDER BY start_date;
