# Write your MySQL query statement below
SELECT
    t.request_at AS day,
    round(
        sum(
            CASE
                WHEN
                    t.status IN ('cancelled_by_driver', 'cancelled_by_client')
                    THEN 1
                ELSE 0
            END
        )
        / count(*),
        2
    ) AS "Cancellation Rate"
FROM trips AS t
INNER JOIN users AS c
    ON t.client_id = c.users_id AND c.banned = 'No' AND c.role = 'client'
INNER JOIN users AS d
    ON t.driver_id = d.users_id AND d.banned = 'No' AND d.role = 'driver'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
