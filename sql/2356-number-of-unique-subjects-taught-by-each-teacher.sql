# Write your MySQL query statement below
SELECT
    teacher_id,
    count(DISTINCT subject_id) AS cnt
FROM teacher
GROUP BY teacher_id;
