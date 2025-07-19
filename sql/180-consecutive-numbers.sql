# Write your MySQL query statement below
SELECT DISTINCT l1.num AS consecutivenums
FROM logs AS l1
INNER JOIN logs AS l2 ON l1.id = l2.id - 1
INNER JOIN logs AS l3 ON l1.id = l3.id - 2
WHERE l1.num = l2.num AND l2.num = l3.num
