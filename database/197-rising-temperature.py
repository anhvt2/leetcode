# Write your MySQL query statement below
SELECT today.id
FROM weather as today
JOIN weather as yesterday
ON date_sub(today.recordDate,Interval 1 day) = yesterday.recordDate
WHERE today.temperature > yesterday.temperature;