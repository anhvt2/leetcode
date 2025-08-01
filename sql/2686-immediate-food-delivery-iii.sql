# Write your MySQL query statement below
SELECT
    order_date,
    round(sum(order_date = customer_pref_delivery_date) * 100 / count(*), 2)
        AS immediate_percentage
FROM Delivery
GROUP BY order_date
ORDER BY order_date;
