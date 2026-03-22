# Write your MySQL query statement below

SELECT u.user_id AS seller_id,
       CASE WHEN i.item_brand = u.favorite_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN (
    SELECT seller_id, item_id,
           ROW_NUMBER() OVER (PARTITION BY seller_id ORDER BY order_date) AS rn
    FROM Orders
) o ON u.user_id = o.seller_id AND o.rn = 2          -- only the 2nd sale
LEFT JOIN Items i ON o.item_id = i.item_id
ORDER BY seller_id;