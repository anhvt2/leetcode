# Write your MySQL query statement below
SELECT u.user_id as buyer_id, u.join_date,
       COUNT(CASE WHEN YEAR(o.order_date) = 2019 THEN 1 END) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o ON u.user_id = o.buyer_id
GROUP BY u.user_id, u.join_date
ORDER BY u.user_id;